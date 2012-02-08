import time

from hex import Hex
from micro import Micro, micro_info
from micro import ProtoError, IspTimeoutError, IspChecksumError, IspProgError

class HexEraseBlock(Hex):
    def __init__(self):
        """Create an erase block command.
        """
        cmd = ":0100000301"
        self.hex = self.append_checksum(cmd)

class HexChipErase(Hex):
    def __init__(self):
        self.hex = ":00000007F9"

class HexProg6Clock(Hex):
    def __init__(self):
        cmd = ":020000030505"
        self.hex = self.append_checksum(cmd)

class HexProgSecBit(Hex):
    def __init__(self):
        cmd = ":020000030501"
        self.hex = self.append_checksum(cmd)

class HexReadInfo(Hex):
    def __init__(self):
        cmd = ":020000050700"
        self.hex = self.append_checksum(cmd)

class HexProgSerial(Hex):
    def __init__(self, serialno):
        cmd = ":%02x000009%s" % (len(serialno)/2, serialno)
        self.hex = self.append_checksum(cmd)

class HexReadSerial(Hex):
    def __init__(self):
        cmd = ":0000000A"
        self.hex = self.append_checksum(cmd)

class P89V51Rx2(Micro):
    def sync_baudrate(self):
        """Synchronize baudrate with micro.

        Raises:
        OSError, IOError -- if reading from/writing to device fails.
        IspTimeoutError -- if no response for command from micro.
        """
        
        # The binary representation of U is 10101010. This character
        # has to be sent first to the micro, so that the micro can
        # calculate the baudrate.
        
        sync = "U"
        self.serial.write(sync)
        self.serial.wait_for("U")
        
    def _set_reset(self, val):
        """Set/clear the reset line.

        Raises:
        OSError, IOError -- if setting the RESET line fails.
        """
        self.serial.set_dtr(val)
        
    def reset(self, isp):
        self._set_reset(1)
        time.sleep(0.25)
        self._set_reset(0)
        time.sleep(0.1)

    def set_osc_freq(self):
        pass

    def _read_info(self):
        cmd = HexReadInfo()
        self.serial.write(cmd)

        # Read and discard
        self.serial.wait_for(":")
        self.serial.read_timeo(len(cmd.hex) - 1)

        # Info bytes
        data = self.serial.read_timeo(3)
        if len(data) != 3:
            raise IspTimeoutError("timed out reading info bytes")

        try:
            return int(data[-3:-1], 16)
        except ValueError, e:
            raise ProtoError("invalid info string")

    def read_sec(self):
        info = self._read_info()
        # print info

        pprotect = False
        if info & 0x4:
            pprotect = True
        
        return (False, False, False, pprotect)

    def read_clock6(self):
        info = self._read_info()

        clock6 = False
        if info & 0x1:
            clock6 = True

        return not clock6

    def erase_block(self, block):
        cmd = HexEraseBlock()
        self._send_cmd(cmd, 5)

    def erase_status_boot_vector(self):
        pass

    def erase_chip(self):
        cmd = HexChipErase()
        self._send_cmd(cmd)        

    def prog_status(self):
        pass

    def prog_boot_vector(self, addr):
        pass

    def prog_clock6(self):
        cmd = HexProg6Clock()
        self._send_cmd(cmd)

    def prog_sec(self, w=False, r=False, x=False, p=False):
        if p:
            cmd = HexProgSecBit()
            self._send_cmd(cmd)

    def prog_serial(self, serialno):
        cmd = HexProgSerial(serialno)
        self._send_cmd(cmd)

common_sparams = {
    "data_bits": 8,
    "parity": False,
    "odd_parity": False,
    "stop_bits": 1,
    "soft_fc": False,
    "hard_fc": False,
}

micro_info.update({
    "P89V51RD2" : {
    "mfg": "NXP",
    "block_range": ((0x0, 0xFFFF),),
    "sparams": common_sparams,
    "class": P89V51Rx2,
    "security": ( "p", "serial" )
    },
    "P89V51RC2" : {
    "mfg": "NXP",
    "block_range": ((0x0, 0xEFFF),),
    "sparams": common_sparams,
    "class": P89V51Rx2,
    "security": ( "p", "serial" )    
    }, 
    "P89V51RB2" : {
    "mfg": "NXP",
    "block_range": ((0x0, 0x3FFF),),
    "sparams": common_sparams,
    "class": P89V51Rx2,
    "security": ( "p", "serial" )    
    } 
})

