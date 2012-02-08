from hex import Hex

# Contains information about all supported micros
micro_info = {}

class ProtoError(Exception):
    pass

class IspTimeoutError(Exception):
    pass

class IspChecksumError(Exception):
    pass

class IspProgError(Exception):
    pass

class HexDispData(Hex):
    def __init__(self, start, end):
        """Create a data display command.

        Args:
        start -- the 16bit start address to display
        end -- the 16bit end address to display

        Raises:
        ValueError -- if start or end is invalid
        """
        if start & 0xFFFF != start:
            raise ValueError("data start address 0x%x out of range" % start)
        elif end & 0xFFFF != end:
            raise ValueError("data end address 0x%x out of range" % end)

        cmd = ":05000004%04x%04x00" % (start, end)
        self.hex = self.append_checksum(cmd)

class HexBlankCheck(Hex):
    def __init__(self, start, end):
        """Create a blank check command.

        Args:
        start -- the start address to check
        end -- the end address to check

        Raises:
        ValueError -- if start or end is invalid
        """
        if start & 0xFFFF != start:
            raise ValueError("check start address 0x%x out of range" % start)
        elif end & 0xFFFF != end:
            raise ValueError("check end address 0x%x out of range" % end)
        
        cmd = ":05000004%04x%04x01" % (start, end)
        self.hex = self.append_checksum(cmd)

class Micro(object):
    RESP_OK = "."
    RESP_CSUM_ERR = "X"
    RESP_PROG_ERR = "R"
    RESP_PROG2_ERR = "P"
    responses = [RESP_OK, RESP_CSUM_ERR, RESP_PROG_ERR, RESP_PROG2_ERR]
    
    def __init__(self, micro, freq, serial):
        """Intialize from micro type, frequency and serial device file.

        Args:
        micro -- the type string of micro to index micro_info
        freq -- the oscillator frequency
        serial -- the serial device filename to access the micro-controller
        """
        self.micro = micro
        self.freq = freq
        self.serial = serial
        self.cache = {}
        self.clear_stats()

    def clear_stats(self):
        self.retry_stats = 0
        self.timeo_stats = 0
        self.cksum_stats = 0
        self.proto_stats = 0
        self.proge_stats = 0

    def retry(self, tries, func, args):
        ex = None
        while tries > 0:
            try:
                return func(*args)
            except IspTimeoutError, e:
                ex = e
                self.timeo_stats += 1
            except IspProgError, e:
                ex = e
                self.proge_stats += 1
            except IspChecksumError, e:
                ex = e
                self.cksum_stats += 1
            except ProtoError, e:
                ex = e
                self.proto_stats += 1
            tries -= 1
            self.retry_stats += 1

        raise e

    def _sync_baudrate(self):
        # The binary representation of U is 10101010. This character
        # has to be sent first to the micro, so that the micro can
        # calculate the baudrate. Atleast two 'U's have to be sent for
        # proper baudrate identification.
        
        sync = "U"
        self.serial.write(sync)
        self.serial.wait_for("U")

        # Read and discard the other Us
#         for i in range(2):
#             try:
#                 self.serial.wait_for("U", 0.5)
#             except IspTimeoutError, e:
#                 pass
            
    def sync_baudrate(self):
        """Synchronize baudrate with micro.

        Raises:
        OSError, IOError -- if reading from/writing to device fails.
        IspTimeoutError -- if no response for command from micro.
        """
        self.retry(8, self._sync_baudrate, ())

    def __send_cmd(self, cmd, timeo=None):
        self.serial.write(cmd)
        if timeo == None:
            resp = self.serial.wait_for(Micro.responses)
        else:
            resp = self.serial.wait_for(Micro.responses, timeo)

        if resp == Micro.RESP_OK:
            return
        elif resp == Micro.RESP_CSUM_ERR:
            raise IspChecksumError("checksum error during comm., recovery failed")
        elif resp == Micro.RESP_PROG_ERR:
            raise IspProgError("programming failed")

        elif resp == Micro.RESP_PROG2_ERR:
            raise IspProgError("programming failed")        
        
    def _send_cmd(self, cmd, timeo=None):
        self.retry(8, self.__send_cmd, (cmd, timeo))

    def prog_file(self, fname, complete_func=None):
        """Program the specified file into the micro.

        Args:
        fname -- the filename to be programmed.
        complete_func -- completer function called to indicate
        percentage of completion.

        Raises:
        OSError, IOError -- if hex file open/read/write fails.
        OSError, IOError -- if read write from serial device failed.
        IspTimeoutError -- if no response for command from micro.
        IspChecksumError -- if checksum error occured during communication.
        IspProgError -- if flash programming failed.
        """
        hex_file = file(fname)
        lines = hex_file.readlines()
        last = float(len(lines) - 1)

        if complete_func:
            complete_func(0)
            
        for i, line in enumerate(lines):
            line = line.strip()
            try:
                self._send_cmd(line)
            except IspProgError, e:
                h = Hex(line)
                raise IspProgError("programming %d bytes at 0x%04x failed, flash likely to be worn out"
                                   % (h.datalen(), h.addr()))
            if complete_func:
                complete_func(i / last)

        try:
            self.erase_status_boot_vector()
        finally:
            self.prog_boot_vector(0xFC)

    def _update_cache_with_line(self, line):
        """Update the cache with a single data line from micro.

        The data line should contain 16 bytes.

        Raises:
        ProtoError -- if the line is not in correct format or is not
        sufficiently long.
        """
        try:
            addr, data = line.split("=")
        except ValueError, e:
            raise ProtoError("invalid data line format")
            
        cache_line = []
        for i in range(0, len(data), 2):
            try:
                byte = data[i:i+2]
                cache_line.append(int(byte, 16))
            except IndexError, e:
                raise ProtoError("data line is not of sufficient length")
            except ValueError, e:
                raise ProtoError("invalid bytes in data line")

        try:
            addr = int(addr, 16)
        except ValueError, e:
            raise ProtoError("invalid bytes in data line")
            
        self.cache[addr] = tuple(cache_line)

    def _update_cache_with_data(self, dbuf):
        """Update the cache with the data buffer.

        Raises:
        ProtoError -- if the data buffer contains invalid data lines.
        """
        lines = dbuf.split("\r")
        
        for l in lines:
            l = l.strip()
            # Clean up any echoes
            if ":" in l or len(l) == 0: 
                continue            
            self._update_cache_with_line(l)

    def _update_cache(self, align16):
        """Update the cache with data read from micro.

        Raises:
        OSError, IOError -- if reading/writing to serial device fails.
        ProtoError -- if invalid data lines are read from micro.
        """
        start = align16
            
        end = align16 + 1024 - 1
        if end > 0xFFFF:
            end = 0xFFFF

        cmd = HexDispData(start, end)
        self.serial.write(cmd)
        self.serial.write("\r")

        dbuf_list = []
        
        while True:
            dbuf = self.serial.read_timeo(256, 0.1)
            if dbuf == "":
                break
            dbuf_list.append(dbuf)
            
        dbuf = "".join(dbuf_list)

        self._update_cache_with_data(dbuf)

    def _getitem(self, addr):
        align16 = addr & 0xFFF0
        offset  = addr & 0x000F

        if align16 not in self.cache:
            self._update_cache(align16)

        try:
            byte = self.cache[align16][offset]
        except KeyError, e:
            raise ProtoError("micro has not provided the required data line: %x"
                             % align16)
        
        return byte
        
    def __getitem__(self, addr):
        """Return the byte at specified address.

        Raises:
        OSError, IOError -- if reading/writing to serial device fails.
        ProtoError -- if invalid data lines are read from micro.
        """
        return self.retry(8, self._getitem, (addr,))

    def reset(self, isp):
        raise NotImplementedError("reset")

    def set_osc_freq(self):
        raise NotImplementedError("set_osc_freq")

    def read_sec(self):
        raise NotImplementedError("read_sec")

    def read_clock6(self):
        raise NotImplementedError("read_clock6")

    def erase_block(self, block):
        raise NotImplementedError("erase_block")

    def erase_status_boot_vector(self):
        raise NotImplementedError("erase_status_boot_vector")

    def erase_chip(self):
        raise NotImplementedError("erase_chip")

    def prog_status(self):
        raise NotImplementedError("prog_status")

    def prog_boot_vector(self, addr):
        raise NotImplementedError("prog_boot_vector")

    def prog_clock6(self):
        raise NotImplementedError("prog_clock6")

    def prog_sec(self, *args):
        raise NotImplementedError("prog_sec")

