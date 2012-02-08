### Hex File Parsing ###

class HexError(Exception):
    def __init__(self, msg, filename = None, lineno = None):
        self.msg = msg
        self.filename = filename
        self.lineno = lineno

class Hex(object):
    def __init__(self, hex_line):
        """Creates a hex record from the provided string.

        Args:
        hex_line -- the hex record as a string
        """
        self.hex = hex_line
        
    def checksum(self, hex_line):
        """Returns the checksum of a hex line.

        Args:
        hex_line -- the hex line without the ':' prefix, and the
        checksum suffix.

        Raises:
        HexError -- when the hex line contains invalid characters
        """
        csum = 0
        nbytes = len(hex_line) / 2      # A byte consitutes two hex characters.
        for i in range(nbytes):
            pos = i * 2
            try:
                hex_byte = hex_line[pos:pos+2] 
                byte = int(hex_byte, 16)
            except IndexError:
                raise HexError("insufficient bytes in hex line")
            except ValueError:
                raise HexError("invalid hex value %s in hex line" % hex_byte)

            # Add to checksum, and shave off all other bytes except LSByte
            csum += byte
            csum &= 0xFF 

        # Calculate 2's complement
        csum ^= 0xFF  
        csum += 1
        csum &= 0xFF

        return csum
        
    def append_checksum(self, hex_line):
        """Returns the hex line appended with checksum.

        Args:
        hex_line -- the hex line without the checksum suffix.

        Raises:
        HexError -- when the hex line contains fewer bytes or invalid
        characters.
        """
        try:
            csum = self.checksum(hex_line[1:]) # Strip the colon off
        except IndexError:
            raise HexError("insufficient bytes in hex line")

        csum_str = "%02x" % csum
        return hex_line + csum_str

    def get_type(self):
        """Returns the type portion of hex line

        Raises:
        HexError -- when the hex line has insufficient bytes
        """
        try:
            return self.hex[7:9];
        except IndexError, e:
            raise HexError("insufficient bytes in hex line")

    def is_data(self):
        """Returns True if the hex record type is data. Raises HexError."""
        return self.get_type() == "00"

    def is_eof(self):
        """Returns True if the hex record type is EOF. Raises HexError."""
        return self.get_type() == "01"

    def addr(self):
        """Returns the address portion of hex record. Raises HexError."""
        try:
            return int(self.hex[3:7], 16)
        except IndexError, e:
            raise HexError("insufficient bytes in hex line")
        except ValueError, e:
            raise HexError("invalid address in hex line")

    def data(self):
        dlen = self.datalen()
        shex = 9
        ehex = shex + (dlen * 2)
        data = self.hex[shex:ehex]

        byte_list = []
        for i in range(0, dlen, 2):
            try:
                byte = data[i:i+2]
                byte_list.append(int(byte, 16))
            except IndexError, e:
                raise HexError("insufficient no. of bytes in record")
            except ValueError, e:
                raise HexError("invalid bytes in record")

        return tuple(byte_list)

    def datalen(self):
        """Returns the length of the data portion of the record. Raises HexError."""
        try:
            return int(self.hex[1:3], 16)
        except IndexError, e:
            raise HexError("insufficient bytes in hex line")
        except ValueError, e:
            raise HexError("invalid length specified in hex line")

    def get_hex(self):
        """Returns the hex record as a string."""
        return self.hex

    def __str__(self):
        """Returns the hex record as a string."""
        return self.hex

class HexFile(object):
    def __init__(self, filename):
        """Create a HexFile object from the filename.

        Args:
        filename - the filename to create a HexFile obect from.
        
        Raises:
        IOError, OSError - if file open fails
        """
        self.hexfile = file(filename)

    def __iter__(self):
        return self

    def rewind(self):
        self.hexfile.seek(0)

    def next(self):
        """Returns the next line as Hex object.

        Raises:
        HexError -- if the hex line is malformed
        StopException -- when EOF is reached
        """
        h = Hex(self.hexfile.next())
        if h.is_eof():
            raise StopIteration("read EOF record")
        return h

    def block_from_addr(self, addr, ranges):
        """Returns the block index corresponding to the addr.

        Args:
        addr -- the address to look for.
        ranges -- the address ranges of blocks as a list of (start,
        end) tuples.
        """
        for i, br in enumerate(ranges):
            if addr >= br[0] and addr <= br[1]:
                return i
        return None

    def count_data_bytes(self):
        """Returns the no. of data bytes in the hex file.

        The file offset pointer will be modified.
        
        Raises:
        OSError, IOError -- if file open/read fails
        HexError -- if the file contains malformed hex records
        """
        self.hexfile.seek(0)
        
        try:
            total = 0
            for lineno, record in enumerate(self):
                if record.is_data():
                    total += len(record.data())
        except HexError, e:
            raise HexError(e.msg, self.hexfile.name, lineno)
        
        return total

    def data_bytes(self):
        self.hexfile.seek(0)

        try:
            for lineo, record in enumerate(self):
                if not record.is_data():
                    continue
                addr = record.addr()
                data = record.data()
                for i in range(len(data)):
                    yield (addr + i, data[i])
        except HexError, e:
            raise HexError(e.msg, self.hexfile.name, lineno)
            
        return

    def used_blocks(self, block_ranges):
        """Returns the blocks used by the file.

        The file offset pointer will be modified.

        Args:
        block_ranges -- the address ranges for the blocks as a list of
        (start, end) tuples

        Raises:
        OSError, IOError -- if file open/read fails
        HexError -- if the file contains malformed hex records
        """
        blocks = []

        self.hexfile.seek(0)
        
        for i, record in enumerate(self):
            try:
                if record.is_eof():
                    break
                if not record.is_data():
                    continue
                addr = record.addr()
            except HexError, e:
                raise HexError(e.msg, self.hexfile.name, i)

            b = self.block_from_addr(addr, block_ranges)
            if b == None:
                raise HexError("address out of device address range",
                               self.hexfile.name, i)
            
            if b not in blocks:
                blocks.append(b)

        blocks.sort()
        return blocks

