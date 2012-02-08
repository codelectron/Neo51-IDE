#!/usr/bin/env python
# smash.py - smash library
# Copyright (C) 2008, 2009 Zilogic Systems
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import logging
from logging import error
import struct
import os
import os.path
import traceback
import string
from optparse import OptionParser
import ConfigParser
import time
import serial
import itertools
import tempfile
xserial = serial

gui_available = True
x_available = True
dbus_available = True
winreg_available = True

try:
    import gobject
    import gtk
    import gtk.glade
    import pango
except ImportError, e:
    gui_available = False
except RuntimeError, e:
    x_available = False

try:
    import dbus
    import dbus.glib
except ImportError, e:
    dbus_available = False

try:
    import _winreg as winreg
except ImportError, e:
    winreg_available = False

# For Help System
import thread
import webbrowser
import tempfile
import atexit

from hex import Hex, HexFile, HexError
from micro import ProtoError, IspTimeoutError, IspChecksumError, IspProgError
from micro import micro_info
from p89v66x import P89V66x
from p89v51rx2 import P89V51Rx2

__version__ = "1.9.0"

timeo_msg = """Communication with device timed out. Please ensure the following
1. The device is connected to the serial port.
2. The baudrate and the oscillator frequency parameter are correct."""

config_filename = os.path.expanduser("~/.smashrc")
cfname = config_filename

# Class Hierarchy:
#
# object
# +- sobject
#    +- Combo
#       +- ConfigCombo
#    +- SerialComboEntry
#    +- ConfigEntry
#    +- StatusBar
#    +- Eavesdrop
#    +- EraseList
#    +- GuiApp
#

### Configuration ###

class ConfigInfo(object):
    """Describes a configuration parameter.

    Attrs:
    transform -- callable the transforms the value from string to
    required type
    ctype -- the type of the config parameter
    allowed -- list of allowed values for the parameter, None if no
    restriction
    default -- the default value for the parameter
    """
    def __init__(self, transform, ctype, allowed, default):
        self.transform = transform
        self.ctype = ctype
        self.allowed = allowed
        self.default = default
    
class Config(object):
    type_allowed = micro_info.keys()
    bps_allowed = [0,     50,     75,
                   110,   134,    150,
                   200,   300,    600,
                   1200,  1800,   2400,
                   4800,  9600,   19200,
                   38400, 57600,  115200,
                   230400]
    data_bits_allowed = [5, 6, 7, 8]
    stop_bits_allowed = [1, 2]
    
    def __init__(self):
        self.config_info = {
            "type":       ConfigInfo(str, str, Config.type_allowed,
                                     "P89V664"),
            "osc-freq":   ConfigInfo(int, int, None, 18),
            "bps":        ConfigInfo(int, int, Config.bps_allowed, 9600),
            "auto-isp":   ConfigInfo(Config.boolean, bool, None, False),
        }
        
        defaults = dict([ (key, value.default)
                          for key, value in self.config_info.iteritems() ])

        self.parser = ConfigParser.RawConfigParser(defaults)
        self.parser.add_section("micro")

        self.conf = {}

        for key, info in self.config_info.iteritems():
            self[key] = self.parser.get("micro", key)

    def __setitem__(self, key, value):
        """Set a configuration parameter from appropriate type or string.
        Args:
        key -- the configuration parameter to be set.
        value -- the value to be set. Is of appropriate type or
        string. If string it is converted to appropriate type before
        setting the parameter.

        Raises:
        ValueError -- if the string value cannot be converted to
        required type, or specified value is not one of the allowed
        values.
        """
        ci = self.config_info[key]

        if type(value) == str:
            try:
                value = ci.transform(value)
            except ValueError, e:
                raise ValueError("invalid config value '%s' for '%s'" % (value, key))
        elif type(value) != ci.ctype:
            raise TypeError("invalid config type for '%s'" % key)

        if ci.allowed == None or (ci.allowed != None and value in ci.allowed):
            self.conf[key] = value
        else:
            raise ValueError("invalid config value '%s' for '%s'" % (value, key))
    
    def __getitem__(self, key):
        return self.conf[key]

    def get_allowed(self, key):
        return self.config_info[key].allowed

    def read(self, filename):
        """Set configuration parameters by reading config file.

        Raises:
        ValueError -- if configuration values are invalid
        ConfigParser.ParsingError -- if error occurs while parsing file
        MissingSectionHeaderError -- if no section headers are present in file
        """
        self.parser.read(filename)
        for key, info in self.config_info.iteritems():
            self[key] = self.parser.get("micro", key)

    @classmethod
    def boolean(cls, string):
        if string.lower() == "true" or string == "1":
            return True
        elif string.lower() == "false" or string == "0":
            return False
        else:
            raise ValueError("expected true or false")

    def write(self, fname):
        f = file(fname, "w")
        f.write("[micro]\n")
        for key, value in self.conf.iteritems():
            f.write("%s=%s\n" % (key, value))
            
### Serial Interface and ISP protocol ###

class Serial(object):
    """Class through which serial port can be configured and accessed.

    Serial Parameters:
    Serial parameter is a dictionary mapping from parameter names to
    their values. The parameters and their type are given below.

    bps -- int
    data_bits -- int
    parity -- bool
    odd_parity -- bool
    soft_fc -- bool
    hard_fc -- bool

    Eavesdropping:
    When the data is sent to or received from the serial port, the
    data can be logged using a eavesdrop function. The function is
    passed the data string as argument.
    """

    def __init__(self, device, sparams, eavesdrop_func = None):
        """Initializes serial device file, with provided parameters.

        Args:
        device -- the device filename.
        sparams -- the serial parameters as a dict. 
        eavesdrop_func -- the eavesdrop callback function. (Optional)

        Raises:
        OSError, IOError -- if the device file open fails.
        ValueError -- if the serial port parameters are out of range.
        xserial.SerialException -- if setting/getting parameters to device fails.
        """
        self.eavesdrop_func = eavesdrop_func

        parity_map = { (False, False): xserial.PARITY_NONE,
                       (False, True): xserial.PARITY_NONE,
                       (True, False): xserial.PARITY_EVEN,
                       (True, True): xserial.PARITY_ODD }
        parity = parity_map[(sparams["parity"], sparams["odd_parity"])]

        stop_bits_map = { 1: xserial.STOPBITS_ONE,
                          2: xserial.STOPBITS_TWO }
        stop_bits = stop_bits_map[sparams["stop_bits"]]
        
        self.serial = xserial.Serial(port = device,
                                     baudrate = sparams["bps"],
                                     bytesize = sparams["data_bits"],
                                     parity = parity,
                                     stopbits = stop_bits,
                                     timeout = None,
                                     xonxoff = 0,
                                     rtscts = 0)

    def __del__(self):
        """Release resources when the object is destroyed."""
        # if __del__ is called before the constructor completes,
        # (incase of exceptions within the constructor), the serial
        # object would not have been define and will trigger an
        # attribute error
        try:
            self.close()
        except AttributeError, e:
            pass

    def close(self):
        """Close serial device if it is opened."""
        self.serial.close()

    def set_timeout(self, timeout):
        self.serial.timeout = timeout

    def read_char(self):
        """Read and return a character from serial device.

        Raises:
        OSError, IOError -- if reading the character from serial device fails.
        """
        string = self.serial.read(1)
        if self.eavesdrop_func:
            self.eavesdrop_func("in", string)
        return string        

    def wait_for(self, chars, timeout=2):
        """Wait for specified characters on serial port for a timeout
        period. Returns the character that matched.

        Args:
        chars -- a list of characters to wait for
        timeout -- the timeout till the function waits, before giving
        up and returning. (Optional, 2 sec if not specified.)

        Raises:
        OSError, IOError -- if reading from serial device fails
        ValueError -- if timeout is out of range
        """
        self.set_timeout(timeout)
        while True:
            sin = self.read_char()
            if sin == "":
                raise IspTimeoutError("did not receive response from device")
            if sin in chars:
                return sin        

    def read_timeo(self, size, timeout=1):
        """Read a block of size specified from the serial port.

        Args:
        size -- the max. size of data to be read.
        timeout -- the timeout in seconds to wait till no response is
        received. (Option, default is 1 second.)

        Raises:
        OSError, IOError -- if reading from serial device fails
        """
        self.set_timeout(timeout)
        data = self.serial.read(size)
        if self.eavesdrop_func:
            self.eavesdrop_func("in", data)
        return data        

    def set_eavesdropper(self, func):
        self.eavesdrop_func = func        

    def write(self, string):
        """Write string to serial device.

        Args:
        string -- object of any type that can be converted to a string
        
        Raises:
        OSError, IOError -- if writing to serial device fails
        """

        self.serial.write(str(string))
        if self.eavesdrop_func:
            self.eavesdrop_func("out", str(string))        

    def set_dtr(self, val):
        """Sets or clears the DTR line of the serial device.

        Raises:
        OSError, IOError -- if setting the DTR line fails.
        """
        self.serial.setDTR(val)

    def set_rts(self, val):
        """Sets or clears the RTS line of the serial device.

        Raises:
        OSError, IOError -- if setting the RTS line fails.
        """
        self.serial.setRTS(val)

class SimMicro(object):
    flash = {}
    w, r, x = (False, False, False)
    clock6 = False
    
    def __init__(self, micro, freq, serial):
        pass

    def clear_stats(self):
        pass

    def reset(self, isp):
        print "reseting isp=%s" % isp

    def retry(self, tries, func, args):
        return func(*args)

    def sync_baudrate(self):
        pass

    def set_osc_freq(self):
        pass

    def read_info(self, what):
        return 0

    def read_sec(self):
        return [SimMicro.w, SimMicro.r, SimMicro.x]

    def read_clock6(self):
        return SimMicro.clock6

    def erase_block(self, block):
        time.sleep(0.1)

    def erase_status_boot_vector(self):
        pass

    def erase_chip(self):
        SimMicro.w = False
        SimMicro.r = False
        SimMicro.x = False
        SimMicro.clock6 = False
        print "Erase chip"

    def prog_status(self):
        pass

    def prog_boot_vector(self, addr):
        pass

    def prog_sec(self, w=None, r=None, x=None):
        if w == True:
            SimMicro.w = w
        if r == True:   
            SimMicro.r = r
        if x == True:
            SimMicro.x = x
        print "Sec Bit (wrx): %s %s %s" % (w, r, x)

    def prog_clock6(self):
        SimMicro.clock6 = True
        print "6 Clock"

    def prog_file(self, fname, complete_func=None):
        hex_file = HexFile(fname)

        count = float(hex_file.count_data_bytes())
        complete_func(0)
        i = 0;

        for addr, data in hex_file.data_bytes():
            SimMicro.flash[addr] = data
            i += 1
            
            if complete_func:
                complete_func(i / count)

            time.sleep(0.01)

    def __getitem__(self, addr):
        try:
            return SimMicro.flash[addr]
        except KeyError, e:
            return 0xFF

### GUI and CLI Interface ###

def catch(func):
    """Decorator that displays exceptions in a dilaog."""
    
    def myfunc(self, *args, **kw):
        try:
            return func(self, *args, **kw)
        except KeyboardInterrupt, e:
            sys.exit(1)
        except:
            self.gexcept()

    return myfunc

def finally_statusbar_clear(func):
    """Decorator clears that status whether or not exception occurs."""
    
    def myfunc(self, *args, **kw):
        try:
            return func(self, *args, **kw)
        finally:
            self.statusbar.clear()

    return myfunc

def catch_timeo(func):
    """Decorator that displays IspTimeOutError in a dilaog."""
    
    def myfunc(self, *args, **kw):
        try:
            return func(self, *args, **kw)
        except IspTimeoutError, e:
            self.gtimeo()
        except IspChecksumError, e:
            self.gerror(str(e))
        except IspProgError, e:
            self.gerror(str(e))

    return myfunc

class sobject(object):
    """Base class for all GUI objects.

    Defines methods and attributes that are used by all GUI objects.
    """
    
    def __init__(self, gmap):
        self.gmap = gmap

    def flush_updates(self):
        while gtk.events_pending():
            gtk.main_iteration_do(False)
            
    def gexcept(self):
        """Displays an exception dialog with the current exception."""
        type, value, tb = sys.exc_info()
        
        self.gmap.exc_label.set_text(str(value))
        buf = self.gmap.traceback_textview.get_buffer()
        buf.set_text(traceback.format_exc())

        self.gmap.exc_expander.set_expanded(False)
        
        self.gmap.exc_dialog.run()
        self.gmap.exc_dialog.hide()

    def gmesg(self, str):
        """Display a info message dialog.

        Args:
        str -- message string to be displayed.
        """
        dialog = gtk.MessageDialog(self.gmap.main_win,
                                   gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                                   gtk.MESSAGE_INFO,
                                   gtk.BUTTONS_OK,
                                   str)
        dialog.run()
        dialog.destroy()

    def gerror(self, str, no_parent = False):
        """Display a error message dialog.

        Args:
        str -- error string to be displayed.
        no_parent -- True if no parent window. False if main_win is
        parent. Default is False.
        """

        if no_parent:
            parent = None
        else:
            parent = self.gmap.main_win
                    
        dialog = gtk.MessageDialog(parent,
                                   gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                                   gtk.MESSAGE_ERROR,
                                   gtk.BUTTONS_OK, str)
        dialog.run()
        dialog.destroy()

    def goserror(self, fmt, e):
        """Display a dialog for handled OSError and IOError exceptions.

        Args:
        str -- error string to be displayed.
        e -- the exception instance of OSError or IOError
        """
        self.gerror(fmt % {"filename": e.filename, "strerror": e.strerror})

    def ghexerror(self, fmt, e):
        """Display a dialog for HexError exception.

        Args:
        str -- error string to be displated.
        e -- HexError exception instance
        """
        self.gerror(fmt % {"filename": e.filename, "lineno": e.lineno, "msg": e.msg})

    def gtimeo(self):
        global timeo_msg
        self.gerror(timeo_msg)
                    
class GladeMap(object):
    def __init__(self, xml):
        """
        Intialize with a glade xml object.

        Args:
        xml -- glade xml object.
        """
        self.xml = xml

    def __getattr__(self, name):
        """Allow widgets to be accessed as attributes of this class."""
        
        w = self.xml.get_widget(name)
        if not w:
            raise AttributeError, name
        return w

class Combo(sobject):
    def __init__(self, combo, gmap):
        """Initialize combo wrapper for combobox widget.

        Args:
        combo -- gtk.ComboBox widget to be wrapped
        gmap -- GladeMap object
        """
        sobject.__init__(self, gmap)
        self.combo = combo
        
    def set_items(self, list, default):
        """Set items in the combo box.

        Args:
        list -- list of string items
        default -- item string to be selected by default
        """
        store = gtk.ListStore(gobject.TYPE_STRING)
        for item in list:
            item_str = str(item)
            store.append([item_str])

        self.combo.set_model(store)

        cell = gtk.CellRendererText()
        self.combo.pack_start(cell, True)
        self.combo.add_attribute(cell, 'text', 0)

        self.combo.show_all()

        if default:
            default_index = list.index(default)
            self.combo.set_active(default_index)

class ConfigCombo(Combo):
    def __init__(self, combo, gmap, conf, key):
        """Initialize config combo wrapper for combobox widget.

        Args:
        combo -- gtk.ComboBox widget to be wrapped
        gmap -- GladeMap object
        conf -- the config dict
        key -- the config parameter (key) associated with the combo
        """
        Combo.__init__(self, combo, gmap)
        self.key = key
        self.conf = conf
        self.cb = None
        self.cb_data = None
        combo.connect("changed", self.on_changed)

        cdefault = conf[key]
        self.clist = conf.get_allowed(key)
        self.set_items(self.clist, cdefault)

    def set_change_callback(self, cb, data=None):
        """Set a callback, called when combobox selection is changed.

        Args:
        cb -- the callable to be called
        data -- data that will passed to the callback (Optional, default is None)
        """
        self.cb = cb
        self.cb_data = data

    def refresh(self):
        i = self.clist.index(self.conf[self.key])
        self.combo.set_active(i)
        
    @catch
    def on_changed(self, *args):
        """Updates the config parameter from the item selected in combobox.

        Invoked on combobox entry changed.
        """
        self.conf[self.key] = self.combo.get_active_text()
        if self.cb:
            self.cb(self.cb_data)

class ConfigEntry(sobject):
    def __init__(self, entry, gmap, conf, key):
        """Initialize config entry wrapper for entry widget.

        Args:
        entry -- gtk.Entry widget to be wrapped
        gmap -- GladeMap object
        conf -- the config dict
        key -- the config parameter (key) associated with the entry
        """
        sobject.__init__(self, gmap)
        self.entry = entry
        self.key = key
        self.conf = conf
        entry.connect("value_changed", self.on_focus)

        cdefault = conf[key]
        entry.set_value(cdefault)

    @catch
    def on_focus(self, *args):
        """Updates the config parameter from the entered value.

        Invoked on focus out of entry widget.
        """
        val = self.entry.get_text()
        try:
            self.conf[self.key] = val
        except ValueError, e:
            self.gerror("Invalid value for '%s'. '%s'." % (self.key, val))
            self.entry.set_text(str(self.conf[self.key]))

class ConfigCheck(sobject):
    def __init__(self, check, gmap, conf, key):
        """Initialize config entry wrapper for entry widget.

        Args:
        check -- gtk.CheckBox widget to be wrapped
        gmap -- GladeMap object
        conf -- the config dict
        key -- the config parameter (key) associated with the entry
        """
        sobject.__init__(self, gmap)
        self.check = check
        self.key = key
        self.conf = conf
        self.check.connect("toggled", self.on_toggled)

        cdefault = conf[self.key]
        self.check.set_active(cdefault)

    @catch
    def on_toggled(self, *args):
        self.conf[self.key] = self.check.get_active()

class SerialComboEntry(sobject):
    def __init__(self, centry, gmap):
        """Initialize from wrapper from serial combobox widget.

        Args:
        combo -- gtk.ComboBox widget to be wrapped
        gmap -- GladeMap object

        Raises:
        dbus.DBusException -- if dbus or hal service is not available
        """
        self.centry = centry
        self.gmap = gmap
        if dbus_available:
            self.init_dbus()
        self.init_combo()

    def init_dbus(self):
        """Initialize dbus and hal interface.

        Raises:
        dbus.DBusException -- if dbus or hal service is not available
        """
        try:
            self.bus = dbus.SystemBus()
            hal_obj = self.bus.get_object('org.freedesktop.Hal',
                                          '/org/freedesktop/Hal/Manager')
            self.hal = dbus.Interface(hal_obj, 'org.freedesktop.Hal.Manager')
        except dbus.DBusException, e:
            self.gerror("It seems that DBUS or HAL service is not available. "
                        "These services are required for smash to function properly."
                        "Please start these service and restart smash.")
            sys.exit(1)
            
    def init_combo(self):
        """Initialize combobox widget items."""
        self.store = gtk.ListStore(gobject.TYPE_STRING, gobject.TYPE_STRING)

        # In Windoze, it is not very obvious which is the USB
        # serial port. A comments column with device name, can be
        # used to identify which of them are USB
        
        comments = gtk.CellRendererText()
        self.centry.pack_start(comments, True)
        self.centry.add_attribute(comments, "text", 1)
          
        self.centry.set_model(self.store)
        self.centry.set_text_column(0)

        if dbus_available:
            self.hal.connect_to_signal("DeviceAdded", self.update)
            self.hal.connect_to_signal("DeviceRemoved", self.update)
        elif winreg_available:
            # Inefficient ... but works!
            self.centry.connect("popup", self.update)

        self.update()

    def serial_devices(self):
        """Returns a list of serial device files available."""

        if dbus_available:
            return self.dbus_serial_devices()
        elif winreg_available:
            return self.winreg_serial_devices()
        else:
            return []

    def winreg_serial_devices(self):
        """Returns a list of serial devices, obtained from Windows registry."""
        
        serial_list = []

        path = 'HARDWARE\\DEVICEMAP\\SERIALCOMM'
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
        except WindowsError, e:
            return serial_list

        for i in itertools.count():
            try:
                val = winreg.EnumValue(key, i)
                comport = str(val[1])
                devname = str(val[0])
                devname = devname.split("\\")[-1]
                serial_list.append((comport, devname))
            except WindowsError, e:
                winreg.CloseKey(key)
                return serial_list
            
        winreg.CloseKey(key)
        return serial_list

    def dbus_serial_devices(self):
        serial_list = []
        
        udis = self.hal.FindDeviceByCapability('serial')
        for udi in udis:
            try:
                dev_obj = self.bus.get_object('org.freedesktop.Hal', udi)
                dev = dbus.Interface(dev_obj, 'org.freedesktop.Hal.Device')
                serial_list.append((dev.GetProperty('serial.device'), ""))
            except dbus.DBusException, e:
                # There is a possibility of race over here.  If
                # there is a device while we get the list, which
                # disappears when we try to do a get_object,
                # DBusException is raised, we silently ignore it.
                #
                # FIXME: Is there a better method to handle this?
                pass

        return serial_list

    @catch
    def update(self, *args):
        """Update the serial combo with current list of serial devices.

        Invoked when device is added or removed in the HAL.
        """
        # Update combo store
        serial_list = self.serial_devices()
        serial_list.sort()
        self.store.clear()
        for item in serial_list:
            self.store.append(item)

    def get_devicefile(self):
        """Returns the selected device file."""
        return self.centry.child.get_text()

class StatusBar(sobject):
    def __init__(self, sb, gmap):
        """Initialize with statusbar widget to be wrapped.

        Args:
        sb -- status bar widget to be wrapped.
        gmap -- GladeMap object
        """
        sobject.__init__(self, gmap)
        self.sb = sb
        self.sbcontext = sb.get_context_id("global")

    def set_text(self, text):
        """Set status bar message with text.

        Args:
        text -- the mesage to be displayed on status bar.
        """
        self.sb.pop(self.sbcontext)
        self.sb.push(self.sbcontext, text)
        self.flush_updates()
        
    def clear(self):
        """Clear the status bar message."""
        self.set_text("")

class Eavesdrop(sobject):
    def __init__(self, textview, gmap):
        """Initialize from textview widget to be wrapped.

        Args:
        textview -- the gtk.TextView widget to be wrapped.
        gmap - GladeMap object
        """
        sobject.__init__(self, gmap)

        self.textview = textview
        self.textbuf = textview.get_buffer()

        self.lastdirection = "out"
        self.textbuf.create_tag("in", foreground="red")
        self.textbuf.create_tag("out", foreground="blue")

    def append_text(self, direction, text):
        """Append text to text view widget.

        Args:
        direction -- specifies what highlighting has to be used, it is
        either 'in' or 'out'.
        text -- the text to be appended.
        """
        end_iter = self.textbuf.get_end_iter()

        # Gobble up the carriage returns, cause eavesdrop to look
        # sparse and ugly.
        text = "".join(text.split("\r"))

        text = "\n".join(text.split("\n\n"))

        if self.lastdirection != direction and self.last_inserted != "\n":
            self.textbuf.insert(end_iter, "\n")
            
        self.textbuf.insert_with_tags_by_name(end_iter, text, direction)

        self.lastdirection = direction 
        self.last_inserted = text[-1:]

    def saveas(self, filename):
        """Save contents of text buffer to file.

        Args:
        filename -- the name of the file where contents are to be
        stored.
        """
        start = self.textbuf.get_start_iter()
        end = self.textbuf.get_end_iter()
        data = self.textbuf.get_text(start, end)

        try:
            f = file(filename, "w")
            f.write(data)
            f.close()
        except (OSError, IOError), e:
            self.goserror("Could not save eavesdrop to file %(filename)s: %(strerror)s", e)

    def clear(self):
        """Clear contents of buffer."""
        self.textbuf.set_text("")

class EraseList(sobject):
    def __init__(self, treeview, gmap, block_ranges):
        """Initialize from treeview widget to be wrapped.

        Args:
        treeview - the gtk.TreeView widget to be wrapped.
        gmap - GladeMap object
        block_ranges - a list of erase block range tuples.
        """
        sobject.__init__(self, gmap)
        self.treeview = treeview

        self.treesel = treeview.get_selection()
        self.treesel.set_mode(gtk.SELECTION_MULTIPLE)

        self.set_block_ranges(block_ranges)

        col = gtk.TreeViewColumn("Block")
        self.treeview.append_column(col)

        cell = gtk.CellRendererText()
        col.pack_start(cell, True)
        col.add_attribute(cell, "text", 0)

        self.treeview.show_all()

    def set_block_ranges(self, block_ranges):
        """Set erase block range list.

        Args:
        block_ranges - a list of erase block range tuples.
        """
        store = gtk.ListStore(gobject.TYPE_STRING)
        for i, br in enumerate(block_ranges):
            store.append(["Block %d (0x%04X - 0x%04X)" % (i, br[0], br[1])])
        self.treeview.set_model(store)

    def unselect_all(self):
        self.treesel.unselect_all()

    def select_blocks(self, block_list):
        """Select block indexes specified in block_list."""
        for block in block_list:
            self.treesel.select_path(block)

    def get_selected_blocks(self):
        """Return a list of block indexes, selected by user."""
        (model, pathlist) = self.treesel.get_selected_rows()
        block_list = []
        for path in pathlist:
            block_list.append(path[0])

        return block_list

class GuiApp(sobject):
    printable = string.digits + string.letters + string.punctuation + " "

    def __init__(self, conf):
        self.conf = conf

        # DBusGMainLoop(set_as_default=True)

        try:
            from smashlib.resources import smash_glade
            self.xml = gtk.glade.xml_new_from_buffer(smash_glade.data, len(smash_glade.data))
        except ImportError, e:
            self.gerror("Please check your installation. Auxillary file "
                        "required for execution of program is missing!",
                        no_parent = True)
            sys.exit(1)
            
        self.xml.signal_autoconnect(self)

        self.gmap = GladeMap(self.xml)

        # Initialize exception dialog 
        self.gmap.exc_dialog.hide()
        self.gmap.exc_dialog.set_transient_for(self.gmap.main_win)

        # Create logo pixbuf from SVG
        # pixbuf = gtk.gdk.pixbuf_new_from_file("icons/logo.svg")
        from smashlib.resources import logo_svg
        logo_dname = tempfile.mkdtemp()
        logo_fname = os.path.join(logo_dname, "logo.svg")
        pixbuf = None
        try:
            file(logo_fname, "w").write(logo_svg.data)
            pixbuf = gtk.gdk.pixbuf_new_from_file(logo_fname)
        except Exception, e:
            pass
        os.remove(logo_fname)
        os.rmdir(logo_dname)
        
        # Initialize main dialog
        self.gmap.main_win.set_icon(pixbuf)
                
        # Initialize about dialog
        self.gmap.aboutdialog.hide()
        self.gmap.aboutdialog.set_transient_for(self.gmap.main_win)
        self.gmap.aboutdialog.set_version(__version__)
        self.gmap.aboutdialog.set_logo(pixbuf)
        self.gmap.aboutdialog.set_icon(pixbuf)

        # Initialize configuration widgets
        self.micro_combo = ConfigCombo(self.gmap.type_combo, self.gmap,
                                  self.conf, "type")
        self.micro_combo.set_change_callback(self.micro_changed)
        self.bps_combo = ConfigCombo(self.gmap.bps_combo, self.gmap,
                                     self.conf, "bps")
        self.osc_freq_entry = ConfigEntry(self.gmap.osc_freq_entry, self.gmap,
                                          self.conf, "osc-freq")
        ConfigCheck(self.gmap.auto_isp_check, self.gmap,
                    self.conf, "auto-isp")

        self.init_hex_fdialog_filters()
        self.used_blocks = []

        micro_default = self.conf["type"]

        # Initialize erase block list
        block_ranges = micro_info[micro_default]["block_range"]
        self.erase_list = EraseList(self.gmap.erase_treeview, self.gmap, block_ranges)

        # Initialize security UI
        self.init_security_ui(micro_info[micro_default]["security"])

        # Initialize flash dump text view
        font_desc = pango.FontDescription("monospace")
        self.gmap.dump_textview.modify_font(font_desc)


        # Initialize status bar, serial combo and eavesdrop
        self.statusbar = StatusBar(self.gmap.statusbar, self.gmap)
        self.serial_combo = SerialComboEntry(self.gmap.serial_centry, self.gmap)
        self.eavesdrop = Eavesdrop(self.gmap.ed_textview, self.gmap)
        
    def init_hex_fdialog_filters(self):
        """Set file hex file dialog filters"""
        hfilt = gtk.FileFilter()
        hfilt.set_name("Intel Hex Files (*.hex, *.ihx)")
        hfilt.add_pattern("*.hex")
        hfilt.add_pattern("*.ihx")

        afilt = gtk.FileFilter()
        afilt.set_name("All Files (*)")
        afilt.add_pattern("*")
        
        self.gmap.hex_file_cbutton.add_filter(hfilt)
        self.gmap.hex_file_cbutton.add_filter(afilt)

    def main(self):
        gtk.main()

    def init_security_ui(self, caps):
        rprotect = "r" in caps
        wprotect = "w" in caps
        xprotect = "x" in caps
        pprotect = "p" in caps
        serialno = "serial" in caps
        
        self.gmap.rprotect_label.set_sensitive(rprotect)
        self.gmap.rprotect_button.set_sensitive(rprotect)
        
        self.gmap.wprotect_label.set_sensitive(wprotect)
        self.gmap.wprotect_button.set_sensitive(wprotect)
        
        self.gmap.xprotect_label.set_sensitive(xprotect)
        self.gmap.xprotect_button.set_sensitive(xprotect)
        
        self.gmap.pprotect_label.set_sensitive(pprotect)
        self.gmap.pprotect_label.set_sensitive(pprotect)

        self.gmap.serial_entry.set_sensitive(serialno)
        self.gmap.serial_button.set_sensitive(serialno)

    def micro_changed(self, data):
        """Update erase list from the currently selected micro."""
        
        micro = self.conf["type"]
        
        block_ranges = micro_info[micro]["block_range"]
        self.erase_list.set_block_ranges(block_ranges)

        security = micro_info[micro]["security"]
        self.init_security_ui(security)

    def on_erase_blocks_check_toggled(self, *args):
        erase_hex_blocks = self.gmap.erase_blocks_check.get_active()
        if erase_hex_blocks:
            self.gmap.erase_treeview.set_sensitive(False)
        else:
            self.gmap.erase_treeview.set_sensitive(True)

    @catch
    def on_hex_file_selection_changed(self, *args):
        """Select erase blocks used by newly selected file.

        Called when the user selects a different file in the file
        selection combobox.
        """
        self.erase_list.unselect_all()

        hex_filename = self.gmap.hex_file_cbutton.get_filename()
        try:
            hex_file = HexFile(hex_filename)
        except (OSError, IOError), e:
            self.goserror("Unable to open hex file %(filename)s: %(strerror)s", e)
            return

        micro = self.conf["type"]
        block_ranges = micro_info[micro]["block_range"]
        try:
            blocks = hex_file.used_blocks(block_ranges)
        except HexError, e:
            self.ghexerror("Error processing hex file %(filename)s at "
                           "lineno %(lineno)d: %(msg)s", e)
            return
        self.erase_list.select_blocks(blocks)
        self.used_blocks = blocks

    def update_program_pbar(self, frac):
        """Set the program progress bar to specified fraction.

        Called by prog_file() as to update flashing progress.
        """
        self.gmap.program_pbar.set_fraction(frac)
        self.flush_updates()

    def update_dump_pbar(self, frac):
        """Set the dump progress bar to specified fraction."""

        self.gmap.dump_pbar.set_fraction(frac)
        self.flush_updates()

    def serial_setup(self):
        """Open serial device and setup serial port parameters."""
        
        serial_filename = self.serial_combo.get_devicefile()
        if not serial_filename:
            self.gerror("Serial device file not selected.")
            return None

        micro = self.conf["type"]
        mi = micro_info[micro]

        sparams = mi["sparams"]        
        sparams["bps"] = self.conf["bps"]

        try:
            serial = Serial(serial_filename, sparams, self.eavesdrop.append_text)
        except (OSError, IOError), e:
            self.gerror("Unable to open serial device %s: %s"
                        % (serial_filename, e.strerror))
            return None
        except xserial.SerialException, e:
            self.gerror("Setting serial parameters failed: %s" % e.args[0])
            return None

        return serial

    def micro_setup(self, serial):
        """Initialize micro-controller communication.

        Returns a Micro object, with baudrate synced and osc-freq set.
        
        Args:
        serial - Serial object to use for communication
        """

        cls = micro_info[self.conf["type"]]["class"]
        micro = cls(self.conf["type"], self.conf["osc-freq"], serial)
        try:
            if self.conf["auto-isp"]:
                micro.reset(isp=1)
            micro.sync_baudrate()
        except (OSError, IOError), e:
            self.goserror("Syncing baudrate failed: %(strerror)s", e)
            return None

        try:
            micro.set_osc_freq()
        except (OSError, IOError), e:
            self.goserror("Setting oscillator freq. failed: %(strerror)s", e)
            return None

        return micro

    def verify(self, micro, hex_filename):
        """Check if the contents of the micro matches that of the file."""
        
        self.update_program_pbar(0)
        self.statusbar.set_text("Verifying ...")

        try:
            hfile = HexFile(hex_filename)
        except (OSError, IOError), e:
            self.goserror("Opening %(filename)s for verification failed: %(strerror)s", e)
            return

        try:
            total = float(hfile.count_data_bytes())
            
            for i, addr_data in enumerate(hfile.data_bytes()):
                addr, data = addr_data
                if micro[addr] != data:
                    self.gerror("Verify failed at %x! "
                                "Please try re-programming." % addr + i)
                    return
                self.update_program_pbar((i+1) / total)
        except HexError, e:
            self.ghexerror("Reading hex file %(filename)s failed "
                           "at lineno %(lineno)d", e);
        except (OSError, IOError), e:
            self.goserror("Reading/writing to device failed, during "
                          "verification: %(strerror)s", e)
        except ProtoError, e:
            self.gerror("Protocol error occured during "
                        "verification: %s" % e.args[0])

    @catch
    @finally_statusbar_clear
    @catch_timeo
    def on_program_button_clicked(self, *args):
        """Program the selected file to micro.

        Called when the program button is clicked.
        """
        self.update_program_pbar(0)
                
        hex_filename = self.gmap.hex_file_cbutton.get_filename()
        if not hex_filename:
            self.gerror("Hex file not selected")
            return

        if self.gmap.erase_blocks_check.get_active():
            block_list = self.used_blocks
        else:
            block_list = self.erase_list.get_selected_blocks()

        serial = self.serial_setup()
        if serial == None:
            return

        micro = self.micro_setup(serial)
        if micro == None:
            return
            
        self.statusbar.set_text("Erasing ...")
        for block in block_list:
            self.statusbar.set_text("Erasing block %d ..." % block)
            try:
                micro.erase_block(block)
            except (OSError, IOError), e:
                self.goserror("Erasing block failed: %(strerror)s",
                              {"strerror": e})
                return

        self.statusbar.set_text("Programming file ...")
        try:
            micro.prog_file(hex_filename, self.update_program_pbar)
        except (OSError, IOError), e:
            self.goserror("Prog. file %(filename)s failed: %(strerror)s",
                          {"filename": hex_filename, "strerror": e})
            return

        # FIXME: There is no way to differentiate between serial I/O
        # error and File I/O error

        verify = self.gmap.verify_prog_check.get_active()
        if verify:
            self.verify(micro, hex_filename)

        if self.conf["auto-isp"]:
            micro.reset(isp=0)

    def do_micro(self, cb, *args, **kwargs):
        serial = self.serial_setup()
        if serial == None:
            return

        micro = self.micro_setup(serial)
        if micro == None:
            serial.close()
            return

        try:
            ret = cb(micro, *args, **kwargs)
        finally:
            serial.close()

        return ret

    def prog_serial(self, micro, serialno):
        micro.prog_serial(serialno)

    def prog_sec(self, micro, w=False, r=False, x=False, p=False):
        micro.prog_sec(w, r, x, p)

    def prog_clock6(self, micro):
        micro.prog_clock6()

    def erase_chip(self, micro):
        micro.erase_chip()

    def read_sec(self, micro):
        return micro.read_sec()

    def read_clock6(self, micro):
        return micro.read_clock6()

    def read_bits(self):
        ret = self.do_micro(self.read_sec)
        if ret == None:
            return
        
        wprotect, rprotect, xprotect, pprotect = ret
            
        ret = self.do_micro(self.read_clock6)
        if ret == None:
            return

        clock6 = not ret

        yesno = { True: ("Yes", gtk.STOCK_YES),
                  False: ("No", gtk.STOCK_NO) }

        label, img = yesno[wprotect]
        self.gmap.wprotect_label.set_text(label)
        self.gmap.wprotect_img.set_from_stock(img, gtk.ICON_SIZE_BUTTON)
    
        label, img = yesno[rprotect]
        self.gmap.rprotect_label.set_text(label)
        self.gmap.rprotect_img.set_from_stock(img, gtk.ICON_SIZE_BUTTON)

        label, img = yesno[xprotect]
        self.gmap.xprotect_label.set_text(label)
        self.gmap.xprotect_img.set_from_stock(img, gtk.ICON_SIZE_BUTTON)

        label, img = yesno[pprotect]
        self.gmap.pprotect_label.set_text(label)
        self.gmap.pprotect_img.set_from_stock(img, gtk.ICON_SIZE_BUTTON)
        
        label, img = yesno[clock6]
        self.gmap.clock6_label.set_text(label)
        self.gmap.clock6_img.set_from_stock(img, gtk.ICON_SIZE_BUTTON)        

    @catch
    @catch_timeo
    def on_serial_button_clicked(self, *args):
        serialno = self.gmap.serial_entry.get_text()
        serial_max = 31
        if len(serialno) > (2 * serial_max):
            self.gerror("Serial no. should be 31 bytes or less.")
            return
        
        for d in serialno:
            if d not in string.hexdigits:
                self.gerror("Serial no. should be in hex.")
                return
        
        self.do_micro(self.prog_serial, serialno)

    @catch
    @catch_timeo
    def on_read_bits_button_clicked(self, *args):
        self.read_bits()
        
    @catch
    @catch_timeo    
    def on_wprotect_button_clicked(self, *args):
        self.do_micro(self.prog_sec, w=True)
        self.gmap.wprotect_label.set_text("Yes")
        self.gmap.wprotect_img.set_from_stock(gtk.STOCK_YES,
                                              gtk.ICON_SIZE_BUTTON)

    @catch
    @catch_timeo
    def on_rprotect_button_clicked(self, *args):
        self.do_micro(self.prog_sec, r=True)
        self.gmap.rprotect_label.set_text("Yes")
        self.gmap.rprotect_img.set_from_stock(gtk.STOCK_YES,
                                              gtk.ICON_SIZE_BUTTON)

    @catch
    @catch_timeo
    def on_xprotect_button_clicked(self, *args):
        self.do_micro(self.prog_sec, x=True)
        self.gmap.xprotect_label.set_text("Yes")
        self.gmap.xprotect_img.set_from_stock(gtk.STOCK_YES,
                                              gtk.ICON_SIZE_BUTTON)

    @catch
    @catch_timeo
    def on_pprotect_button_clicked(self, *args):
        self.do_micro(self.prog_sec, p=True)
        self.gmap.pprotect_label.set_text("Yes")
        self.gmap.pprotect_img.set_from_stock(gtk.STOCK_YES,
                                              gtk.ICON_SIZE_BUTTON)

    @catch
    @catch_timeo
    def on_clock6_button_clicked(self, *args):
        self.do_micro(self.prog_clock6)
        self.gmap.clock6_label.set_text("Yes")
        self.gmap.clock6_img.set_from_stock(gtk.STOCK_YES,
                                            gtk.ICON_SIZE_BUTTON)

    @catch
    @catch_timeo
    def on_erase_chip_button_clicked(self, *args):
        self.do_micro(self.erase_chip)
        self.gmap.wprotect_label.set_text("No")
        self.gmap.wprotect_img.set_from_stock(gtk.STOCK_NO,
                                              gtk.ICON_SIZE_BUTTON)
        self.gmap.rprotect_label.set_text("No")
        self.gmap.rprotect_img.set_from_stock(gtk.STOCK_NO,
                                              gtk.ICON_SIZE_BUTTON)
        self.gmap.xprotect_label.set_text("No")
        self.gmap.xprotect_img.set_from_stock(gtk.STOCK_NO,
                                              gtk.ICON_SIZE_BUTTON)
        self.gmap.pprotect_label.set_text("No")
        self.gmap.pprotect_img.set_from_stock(gtk.STOCK_NO,
                                              gtk.ICON_SIZE_BUTTON)        
        self.gmap.clock6_label.set_text("No")
        self.gmap.clock6_img.set_from_stock(gtk.STOCK_NO,
                                            gtk.ICON_SIZE_BUTTON)

        self.read_bits()

    @catch
    def on_config_save_button_clicked(self, *args):
        cfname = config_filename
        try:
            self.conf.write(cfname)
        except IOError, e:
            self.gerror("Error writing configuration: %s" % e)
        except OSError, e:
            self.gerror("Error writing configuration: %s" % e)

    @catch
    def on_config_revert_button_clicked(self, *args):
        cfname = config_filename
        try:
            self.conf.read(cfname)
        except IOError, e:
            self.gerror("Error reading configuration: %s" % e)
        except OSError, e:
            self.gerror("Error reading configuration: %s" % e)
        self.micro_combo.refresh()

    @catch
    def on_ed_clear_button_clicked(self, *args):
        self.eavesdrop.clear()

    def get_saveas_filename(self):
        """Prompt user for a filename for saving to with a file dialog box."""
        filename = None
        dialog = gtk.FileChooserDialog(title = "Save eavesdrop as ...",
                                       action = gtk.FILE_CHOOSER_ACTION_SAVE,
                                       buttons = (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                                  gtk.STOCK_SAVE, gtk.RESPONSE_OK))
        response = dialog.run()
        if response == gtk.RESPONSE_OK:
            filename = dialog.get_filename()

        dialog.destroy()

        return filename

    @catch
    def on_ed_saveas_button_clicked(self, *args):
        """Save eavesdrop to a file.

        Called when the user clicks the saveas button in the eavesdrop
        tab.
        """
        filename = self.get_saveas_filename()
        if filename == None:
            return
        
        self.eavesdrop.saveas(filename)
        
    def on_main_win_destroy(self, *args):
        sys.exit(0)

    def on_program_tlb_clicked(self, *args):
        self.gmap.notebook.set_current_page(0)

    def on_dump_tlb_clicked(self, *args):
        self.gmap.notebook.set_current_page(1)

    def on_security_tlb_clicked(self, *args):
        self.gmap.notebook.set_current_page(2)

    def on_config_tlb_clicked(self, *args):
        self.gmap.notebook.set_current_page(3)

    def on_eavesdrop_tlb_clicked(self, *args):
        self.gmap.notebook.set_current_page(4)

    def show_help(self):
        url = "http://code.google.com/p/smash-tool/wiki/Help?show=content"
        webbrowser.open(url)

    @catch
    def on_help_tlb_clicked(self, *args):
        thread.start_new_thread(self.show_help, ())
        
    def on_about_tlb_clicked(self, *args):
        self.gmap.aboutdialog.run()
        self.gmap.aboutdialog.hide()

    @catch
    @catch_timeo
    def on_dump_button_clicked(self, *args):
        self.update_dump_pbar(0)
        
        start_addr = self.gmap.dump_start_entry.get_text()
        try:
            start_addr = int(start_addr, 0)
        except ValueError, e:
            self.gerror("Invalid start address '%s'." % start_addr)
            return

        end_addr = self.gmap.dump_end_entry.get_text()
        try:
            end_addr = int(end_addr, 0)
        except ValueError, e:
            self.gerror("Invalid end address '%s'." % end_addr)
            return

        serial = self.serial_setup()
        if serial == None:
            return

        micro = self.micro_setup(serial)
        if micro == None:
            return

        total_bytes = float(end_addr - start_addr + 1)

        dl = []
        ascii = []
        try:
            for i, addr in enumerate(range(start_addr, end_addr + 1)):
                if i % 16 == 0:
                    dl.append("%04X" % addr)

                if i % 8 == 0:
                    dl.append(" ")

                dl.append("%02X" % (micro[addr]))

                asc = chr(micro[addr])
                if asc not in self.printable:
                    asc = "."
                ascii.append(asc)
                
                if i % 16 == 15:
                    dl.append(" |")
                    dl.append("".join(ascii))
                    dl.append("|\n")
                    ascii = []

                progress = (i + 1) / total_bytes
                self.update_dump_pbar(progress)
        except ProtoError, e:
            self.gerror("Protocol Error: %s" % e.args[0])
            return
        except (OSError, IOError), e:
            self.goserror("Reading data from flash failed: %(strerror)s", e)
            return

        data = "".join(dl)

        textbuf = self.gmap.dump_textview.get_buffer()
        textbuf.set_text(data)

#
# Based on whether the user specifies -q option, the appropriate
# print function will be chosen
#
def real_print(*args):
    for a in args:
        sys.stdout.write(a)

def quiet_print(*args):
    pass

qprint = real_print

class CmdProgressBar(object):
    """ Creates a text-based progress bar. Call the object to update
    and print the progress bar. The progress will look as shown below.

    22% [========                             ]
    
    The progress bar's width is specified on init.
    """

    def __init__(self, total_width=80, prefix=""):
        self.prog_bar = "[]"   
        self.width = total_width
        self.prefix = prefix
        self.amount = 0       
        self.update_amount(0)  

    def update_amount(self, new = 0):
        """Update the progress bar with the new amount."""
        self.amount = new
        percent = int(round(self.amount * 100))
        full = self.width - 2
        complete = (percent / 100.0) * full
        complete = int(round(complete))
        
        self.prog_bar = "%3d%% [%s%s]" % (percent, '=' * complete, ' ' * (full - complete))

    def __str__(self):
        return str(self.prog_bar)
            
    def __call__(self, value):
        """Update the amount, and draw the progress bar."""
        qprint('\r')
        self.update_amount(value)
        qprint(self.prefix)
        qprint(str(self))
        sys.stdout.flush()

class SOptionParser(OptionParser):
    def set_trail(self, trail):
        self.trail = trail
    
    def print_help(self, file=None):
        OptionParser.print_help(self, file)
        qprint(self.trail, "\n")

class CmdApp(object):
    def __init__(self, conf, parser, options, args):
        self.conf = conf
        self.parser = parser
        self.options = options
        self.args = args
        
    def serial_setup(self, serial_filename):
        """Open serial device and setup serial port parameters.

        Args:
        serial_filename - the filename of the serial device.

        Returns Serial object with serial parameters configured."""
        mtype = self.conf["type"]
        mi = micro_info[mtype]

        sparams = mi["sparams"]
        sparams["bps"] = self.conf["bps"]

        try:
            serial = Serial(serial_filename, sparams)
        except (OSError, IOError), e:
            error("unable to open serail device '%s': %s"
                  % (serial_filename, e.strerror))
            sys.exit(1)
        except xserial.SerialException, e:
            error("setting serial parameters failed: %s" % e.args[0])
            sys.exit(1)

        return serial

    def micro_setup(self, serial):
        """Initialize micro-controller communication.

        Returns a Micro object, with baudrate synced and osc-freq set.

        Args:
        serial -- Serial object to use for communication
        """

        cls = micro_info[self.conf["type"]]["class"]
        micro = cls(self.conf["type"], self.conf["osc-freq"], serial)
        try:
            if self.conf["auto-isp"]:
                micro.reset(isp=1)
            micro.sync_baudrate()
        except (OSError, IOError), e:
            error("syncing baudrate failed: %s" % e.strerror)
            sys.exit(1)

        try:
            micro.set_osc_freq()
        except (OSError, IOError), e:
            error("setting oscillator freq. failed: %s" % e.strerror)
            sys.exit(1)

        return micro

    def erase_progress(self, micro, blocks):
        pbar = CmdProgressBar(40, "Erase  : ")
        pbar(0)

        try:
            nblocks = float(len(blocks))
            for i, b in enumerate(blocks):
                try:
                    micro.erase_block(b)
                    pbar((i + 1) / nblocks)
                except (OSError, IOError), e:
                    qprint("\n")
                    error("erasing block failed: %s", e.strerror)
                    sys.exit(1)
                except ValueError, e:
                    qprint("\n")
                    error("invalid erase block: %d", b)
                    sys.exit(1)
        finally:
            qprint("\n")

    def erase(self, micro, hex_filename):
        """Erase the flash blocks that are used by the file.
        
        Args:
        micro -- the Micro object whose contents are to be erased.
        hex_filename -- the hex file whose data is to be flashed.
        """
        try:
            hex_file = HexFile(hex_filename)
        except (OSError, IOError), e:
            error("opening file %s failed: %s" % (hex_filename, e.strerror))
            sys.exit(1)

        mtype = self.conf["type"]
        block_ranges = micro_info[mtype]["block_range"]
        try:
            blocks = hex_file.used_blocks(block_ranges)
        except HexError, e:
            error("error processing hex file %s at lineno %d: %s"
                  % (e.filename, e.lineno, e.msg))
            sys.exit(1)

        self.erase_progress(micro, blocks)

    def program(self, micro, hex_filename):
        """Program data from hex file into micro's flash.

        Args:
        micro -- the Micro object in which the data is to be flashed.
        hex_filename -- the hex file's filename whose data is to be flashed.
        """
        pbar = CmdProgressBar(40, "Program: ")
        pbar(0)

        try:
            try:
                micro.prog_file(hex_filename, pbar)
            except (OSError, IOError), e:
                qprint("\n")
                error("programming file %s failed: %s",
                      hex_filename, e.strerror)
                sys.exit(1)
            except HexError, e:
                qprint("\n")
                error("error processing hex file %s at lineno %d: %s"
                      % (e.filename, e.lineno, e.msg))                
                sys.exit(1)
        finally:
            qprint("\n")

    def verify(self, micro, hex_filename):
        """Verify the contents of flash against a hex file.

        Args:
        micro -- the Micro object whose contents are to be verified.
        hex_filename -- the hex file's filename against which the
        content is to be verified.
        """
        try:
            hfile = HexFile(hex_filename)
        except (OSError, IOError), e:
            error("opening %s for verification failed: %s", e.filename)                
            sys.exit(1)

        pbar = CmdProgressBar(40, "Verify : ")
        pbar(0)

        try:
            try:
                total = float(hfile.count_data_bytes())

                for i, addr_data in enumerate(hfile.data_bytes()):
                    addr, data = addr_data
                    if micro[addr] != data:
                        qprint("\n")
                        error("verify failed at %x" % addr)
                        sys.exit(1)
                    pbar((i+1) / total)
            except HexError, e:
                qprint("\n")
                error("reading hex file %s failed "
                      "at lineno %d" % (e.filename, e.lineo));
            except (OSError, IOError), e:
                qprint("\n")
                error("reading/writing to device failed, during "
                      "verification: %s", e.strerror)
            except ProtoError, e:
                qprint("\n")
                error("protocol error occured during "
                      "verification: %s", e.args[0])
        finally:
            qprint("\n")

    def display_info(self, micro):
        w, r, x, p = micro.read_sec()
        clock6 = not micro.read_clock6()

        def bool2str(b):
            if b:
                return "Yes"
            else:
                return "No"
            
        print "Write Protected:", bool2str(w)
        print "Read Protected:", bool2str(r)
        print "External Execution Inhibited:", bool2str(x)
        print "Parallel Program Inhibited:", bool2str(x)
        print "Clock Mode:",
        if clock6:
            print "6x"
        else:
            print "12x"
            
    def parse_blocks(self, block_list):
        blocks = block_list.split(",")
        try:
            blocks = [int(b) for b in blocks]
        except ValueError, e:
            error("invalid block no. %s" % b)
        return blocks

    def do_isp(self):
        """Program the specified file into the micro-controller."""
        
        if len(self.args) != 1:
            self.parser.error("required arguments not specified")

        serial_filename = self.args[0]

        serial = self.serial_setup(serial_filename)
        micro = self.micro_setup(serial)

        if self.options.erase_chip:
            micro.erase_chip()
        elif self.options.erase_blocks:
            blocks = self.parse_blocks(self.options.erase_blocks)
            self.erase_progress(micro, blocks)
        elif self.options.prog != None:
            self.erase(micro, self.options.prog)

        if self.options.prog != None:
            self.program(micro, self.options.prog)

        if self.options.prog != None and self.options.verify:
            self.verify(micro, self.options.prog)

        if self.options.prog_sec != None:
            if "W" in self.options.prog_sec:
                micro.prog_sec(w=True)
            if "R" in self.options.prog_sec:
                micro.prog_sec(r=True)
            if "X" in self.options.prog_sec:
                micro.prog_sec(x=True)
            if "P" in self.options.prog_sec:
                micro.prog_sec(p=True)

        if self.options.prog_clock6:
            micro.prog_clock6()
            
        if self.options.display_info:
            self.display_info(micro)

        # if micro.retry_stats != 0:
        #    print "Programming complete. Retry statistics:"
        #    print "R: %02d T: %02d" % (micro.retry_stats, micro.timeo_stats),
        #    print "C: %02d E: %02d" % (micro.cksum_stats, micro.proge_stats),
        #    print "P: %02d" % (micro.proto_stats)

        if self.conf["auto-isp"]:
            micro.reset(isp=0)
        
    def main(self):
        global timeo_msg
        
        try:
            self.do_isp()
        except IspTimeoutError, e:
            error(timeo_msg)
            sys.exit(1)
        except IspChecksumError, e:
            error(str(e))
            sys.exit(1)
        except IspProgError, e:
            error(str(e))
            sys.exit(1)
        except KeyboardInterrupt, e:
            sys.exit(1)

def init_opt_parser(conf):
    usage = "%prog [options] <serial-dev>"
    parser = SOptionParser(usage=usage, version=__version__)
    parser.add_option("-m", "--micro", dest="micro",
                      help="set the microcontroller type to M. "
                      "Default is %default.",
                      metavar="M",
                      default=conf["type"])
    parser.add_option("-f", "--osc-freq", dest="freq",
                      help="set the oscillator frequency to F MHz. "
                      "Default is %default.",
                      metavar="F",
                      type=int,
                      default=conf["osc-freq"])
    parser.add_option("-b", "--bps", dest="bps",
                      help="set the baudrate to B bits per second. "
                      "Default is %default.",
                      metavar="B",
                      type=int,
                      default=conf["bps"])
    parser.add_option("-V", "--verify", action="store_true",
                      dest="verify",
                      help="verify after programming. Default is %default.",
                      default=False)
    parser.add_option("-d", "--auto-isp", action="store_true",
                      dest="auto_isp",
                      help="auto reset and ISP entry using DTR RTS toggling. Default is %default.",
                      default=conf["auto-isp"])
    parser.add_option("-P", "--prog", dest="prog",
                      help="program the hex file F into the micro.",
                      metavar="F",
                      default=None)
    parser.add_option("-B", "--erase-blocks", dest="erase_blocks",
                      help="erase a comma separated list of blocks B",
                      metavar="B",
                      default=None)
    parser.add_option("-C", "--erase-chip", action="store_true",
                      dest="erase_chip",
                      help="erase code memory and security bits.",
                      default=False)
    parser.add_option("-I", "--display-info", action="store_true",
                      dest="display_info",
                      help="display security bits, clock mode and status bits",
                      default=False)
    parser.add_option("-S", "--prog-sec", dest="prog_sec",
                      help="program security bits S. (Combination of WRX)",
                      metavar="S",
                      default=None)
    parser.add_option("-L", "--prog-clock6", action="store_true",
                      dest="prog_clock6",
                      help="enable 6x clock mode.",
                      default=False)
    parser.add_option("-q", "--quiet", action="store_true",
                      dest="quiet",
                      help="do not show progress.")

    trail = \
"""
Supported micro-controllers: %(micros)s

Example: %(prog)s --prog=myfile.hex /dev/ttyUSB0""" \
    % { "prog": os.path.basename(sys.argv[0]),
        "micros": ", ".join(conf.get_allowed("type")) }
        
    parser.set_trail(trail)
    
    return parser


def main_cli():
    progname = os.path.basename(sys.argv[0])
    logging.basicConfig(level=logging.DEBUG,
                        format=progname + ': %(message)s')

    conf = Config()
    cfname = config_filename
    try:
        conf.read(cfname)
    except ValueError, e:
        error("error parsing '%s': %s" % (cfname, e.args[0]))
        sys.exit(1)
    except ConfigParser.ParsingError, e:
        error("parsing config file '%s' failed: %s" % (cfname, e.args[0]))
        sys.exit(1)
    except ConfigParser.MissingSectionHeaderError, e:
        error("section header not present in file '%s': %s" % (cfname, e.args[0]))
        sys.exit(1)

    # Command line options override the values in the configuration
    # file.
    parser = init_opt_parser(conf)
    (options, args) = parser.parse_args()

    try:
        conf["type"] = options.micro
        conf["osc-freq"] = options.freq
        conf["bps"] = options.bps
        conf["auto-isp"] = options.auto_isp
    except ValueError, e:
        parser.error(e.args[0])

    if options.quiet:
        global qprint
        qprint = quiet_print

    app = CmdApp(conf, parser, options, args)
    app.main()
    sys.exit(0)

def gerror(str):
    dialog = gtk.MessageDialog(None, 0,
                               gtk.MESSAGE_ERROR,
                               gtk.BUTTONS_OK, str)    

def main_gui():
    if not (gui_available and x_available):
        if not gui_available:
            error("required GUI modules not available")
        if not x_available:
            error("cannot connect to X server")
        sys.exit(1)

    gtk.threads_init()

    conf = Config()
    cfname = config_filename
    try:
        conf.read(cfname)
    except ValueError, e:
        gerror("error parsing '%s': %s" % (cfname, e.args[0]))
    except ConfigParser.ParsingError, e:
        gerror("parsing config file '%s' failed: %s" % (cfname, e.args[0]))
    except ConfigParser.MissingSectionHeaderError, e:
        gerror("section header not present in file '%s': %s" % (cfname, e.args[0]))

    app = GuiApp(conf)
    app.main()
    sys.exit(0)
