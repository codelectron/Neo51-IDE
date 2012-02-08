import time

from hex import Hex
from micro import Micro, micro_info
from micro import ProtoError, IspTimeoutError, IspChecksumError, IspProgError

class HexOscFreq(Hex):
    def __init__(self, freq):
        """Create a osc. freq set command from provided freq.

        Args:
        freq -- the freq to be set.

        Raises:
        ValueError -- if frequency is out of range
        """
        if freq & 0xFF != freq:
            raise ValueError("frequency 0x%x is out of range" % freq)
        
        cmd = ":01000002%02x" % freq
        self.hex = self.append_checksum(cmd)

class HexEraseBlock(Hex):
    def __init__(self, block):
        """Create an erase block command from provided block address.

        Args:
        block -- the block address MSB to be erased.

        Raises:
        ValueError -- if the block no. is out of range.
        """
        if block & 0xFF != block:
            raise ValueError("block address 0x%x out of range" % block)
        
        cmd = ":0200000301%02x" % block
        self.hex = self.append_checksum(cmd)

class HexEraseBootVecStatus(Hex):
    def __init__(self):
        """Create a boot vector status read command."""
        cmd = ":020000030400"
        self.hex = self.append_checksum(cmd)

class HexProgSecBit(Hex):
    [W, R, X] = range(0, 3)
    
    def __init__(self, bit):
        """Create a securtiy bit program command.

        Args:
        bit -- the security bit to be programmed.

        Raises:
        ValueError -- if security bit is invalid.
        """
        if bit & 0xFF != bit:
            raise ValueError("security bit 0x%x out of range" % bit)

        cmd = ":0200000305%02x" % bit
        self.hex = self.append_checksum(cmd)

class HexProgBootVec(Hex):
    def __init__(self, val):
        """Create a boot vector program command.

        Args:
        val -- the boot vector location MSB to be programmed.

        Raises:
        ValueError -- if val is out of range.
        """
        if val & 0xFF != val:
            raise ValueError("vector byte 0x%x out of range" % val)
        
        cmd = ":030000030601%02x" % val
        self.hex = self.append_checksum(cmd)

class HexProgStatus(Hex):
    def __init__(self):
        """Create a program status command.
        """

        cmd = ":020000030600"
        self.hex = self.append_checksum(cmd)

class HexProgVec(Hex):
    def __init__(self, val):
        """Create a program vector command.

        Args:
        val -- the status byte to be programmed.

        Raises:
        ValueError -- if val is out of range.
        """
        if val & 0xFF != val:
            raise ValueError("status byte 0x%x out of range" % val)

        cmd = ":030000030601%02x" % val
        self.hex = self.append_checksum(cmd)

class HexProg6Clock(Hex):
    def __init__(self):
        """Create a 6x/12x bit command.
        """

        cmd = ":020000030602"
        self.hex = self.append_checksum(cmd)

class HexReadInfo(Hex):
    [MFG_ID, DEV_ID1, DEV_ID2, CLOCK_6x] = [0x0, 0x1, 0x2, 0x3]
    [SEC_BITS, STATUS, BOOT_VEC] = [0x700, 0x701, 0x702]
    
    def __init__(self, what):
        """Create a read info command.

        Args:
        what -- the information to be read.

        Raises:
        ValueError -- if what is out of range.
        """
        if what & 0xFFFF != what:
            raise ValueError("info to read 0x%x out or range" % what)
        
        cmd = ":02000005%04x" % what
        self.hex = self.append_checksum(cmd)

class HexChipErase(Hex):
    def __init__(self):
        cmd = ":0100000307"
        self.hex = self.append_checksum(cmd)

class P89V66x(Micro):
    def _set_reset(self, val):
        """Set/clear the reset line.

        Raises:
        OSError, IOError -- if setting the RESET line fails.
        """
        self.serial.set_dtr(val)

    def _set_psen(self, val):
        """Set/clear the reset line.

        Raises:
        OSError, IOError -- if setting the PSEN line fails.
        """
        self.serial.set_rts(val)

    def reset(self, isp):
        """Reset the micro-controller.

        If isp is set, the micro-controller is switched into ISP mode.

        Raises:
        OSError, IOError -- if toggling RESET and PSEN line fails
        """
        if isp == 1:
            self._set_reset(1)
            self._set_psen(1)
            time.sleep(0.25)
            self._set_reset(0)
            time.sleep(0.25)
            self._set_psen(0)
        else:
            self._set_reset(1)
            time.sleep(0.25)
            self._set_reset(0)

    def _sync_baudrate(self):
        # The binary representation of U is 10101010. This character
        # has to be sent first to the micro, so that the micro can
        # calculate the baudrate. Atleast two 'U's have to be sent for
        # proper baudrate identification.
        
        sync = "UUU"
        self.serial.write(sync)
        self.serial.wait_for("U")

        # Read and discard the other Us
        for i in range(2):
            try:
                self.serial.wait_for("U", 0.5)
            except IspTimeoutError, e:
                pass
            
    def sync_baudrate(self):
        """Synchronize baudrate with micro.

        Raises:
        OSError, IOError -- if reading from/writing to device fails.
        IspTimeoutError -- if no response for command from micro.
        """
        self.retry(8, self._sync_baudrate, ())

    def set_osc_freq(self):
        """Set the oscillator frequency in the micro.

        Raises:
        ValueError -- if frequency is invalid.
        OSError, IOError -- if reading from/writing to serial device fails.
        IspTimeoutError -- if no response for command from micro.
        IspChecksumError -- if checksum error occured during communication.
        """
        cmd = HexOscFreq(self.freq)
        self._send_cmd(cmd)

    def _read_info(self, info):
        cmd = HexReadInfo(info)
        self.serial.write(cmd)

        self.serial.wait_for(":")
        self.serial.read_timeo(len(cmd.hex) - 1)
        
        data = self.serial.read_timeo(3)
        if len(data) != 3:
            raise IspTimeoutError("timed out reading info bytes")
        
        try:
            return int(data[-3:-1], 16)
        except ValueError, e:
            raise ProtoError("invalid info string")

    def read_info(self, info):
        """Read micro-controller information. (and discard).

        Raises:
        OSError, IOError -- if reading from/writing to serial device fails.
        IspTimeoutError -- if no response for command from micro.
        IspChecksumError -- if checksum error occured during communication.
        ProtoError -- if invalid data lines are read from micro.        
        """
        return self.retry(8, self._read_info, (info,))

    def read_sec(self):
        data = self.read_info(HexReadInfo.SEC_BITS)
        return [bool(data & 0x2), bool(data & 0x4), bool(data & 0x8), None]

    def read_clock6(self):
        data = self.read_info(HexReadInfo.CLOCK_6x)
        return bool(data)
        
    def _block_to_hex(self, block):
        """Returns the byte used in hex commands to denote a block.

        Args:
        block -- the index of the block
        """
        mi = micro_info[self.micro]
        brange = mi["block_range"][block]
        bstart = brange[0]
        return (bstart >> 8) & 0xFF

    def erase_block(self, block):
        """Erase the block specified.

        Args:
        block -- the index of the block to be erased.

        Raises:
        OSError, IOError -- if reading from/writing to serial device fails.
        IspTimeoutError -- if no response for command from micro.
        IspChecksumError -- if checksum error occured during communication.        
        """
        try:
            bhex = self._block_to_hex(block)
        except IndexError, e:
            raise ValueError("invalid erase block")
        cmd = HexEraseBlock(bhex)

        # Some crazy micro-controllers take as much as 30 seconds to
        # erase a block.
        self._send_cmd(cmd, 5)

    def erase_status_boot_vector(self):
        cmd = HexEraseBootVecStatus()
        self._send_cmd(cmd)

    def erase_chip(self):
        cmd = HexChipErase()
        self._send_cmd(cmd)

    def prog_status(self):
        cmd = HexProgStatus()
        self._send_cmd(cmd)

    def prog_boot_vector(self, addr):
        cmd = HexProgVec(addr)
        self._send_cmd(cmd)

    def prog_clock6(self):
        cmd = HexProg6Clock()
        self._send_cmd(cmd)

    def prog_sec(self, w=False, r=False, x=False, p=False):
        if w:
            cmd = HexProgSecBit(HexProgSecBit.W)
            self._send_cmd(cmd)            
        if r:
            cmd = HexProgSecBit(HexProgSecBit.R)
            self._send_cmd(cmd)            
        if x:
            cmd = HexProgSecBit(HexProgSecBit.X)
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
    "P89V660" : {
    "mfg": "NXP",
    "block_range": ((0x0, 0x1FFF), (0x2000, 0x3FFF)),
    "sparams": common_sparams,
    "class": P89V66x,
    "security": ( "r", "w", "x" )
    },
    "P89V662" : {
    "mfg": "NXP",
    "block_range": ((0x0, 0x1FFF), (0x2000, 0x3FFF), (0x4000, 0x7FFF)),
    "sparams": common_sparams,
    "class": P89V66x,
    "security": ( "r", "w", "x" )
    },
    "P89V664" : {
    "mfg": "NXP",
    "block_range": ((0x0, 0x1FFF), (0x2000, 0x3FFF), (0x4000, 0x7FFF),
                    (0x8000, 0xBFFF), (0xC000, 0xFFFF)),
    "sparams": common_sparams,
    "class": P89V66x,
    "security": ( "r", "w", "x" )
    }
})
