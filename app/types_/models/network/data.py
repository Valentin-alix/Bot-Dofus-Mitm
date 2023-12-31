"""
Replicate com.ankamagames.jerakine.network.CustomDataWrapper
"""
import struct
from bz2 import decompress
from dataclasses import dataclass
from typing import TypedDict


class Data:
    def __init__(self, data=None):
        if data is None:
            data = bytearray()
        self.data = data
        self.pos = 0

    def __len__(self):
        return len(self.data)

    def __add__(self, byte):
        return self.data + byte

    def __radd__(self, byte):
        return byte + self.data

    def __iadd__(self, by):
        self.data += by
        return self

    def __str__(self):
        return str.format(
            "{}(bytearray.fromhex('{}'))", self.__class__.__name__, self.data.hex()
        )

    def __repr__(self):
        return str.format("{}({!r})", self.__class__.__name__, self.data)

    def remaining(self):
        return len(self) - self.pos

    def hex(self):
        return self.data.hex()

    @classmethod
    def fromhex(cls, _hex):
        return cls(bytearray.fromhex(_hex))

    def verif(self, l):
        if len(self) < self.pos + l:
            raise IndexError(self.pos, l, len(self))

    def reset_pos(self):
        self.pos = 0

    def read(self, l):
        self.verif(l)
        pos = self.pos
        self.pos += l
        return self.data[pos: pos + l]

    def write(self, l):
        self.data += l

    def uncompress(self):
        self.data = bytearray(decompress(self.data))

    def readBoolean(self):
        ans = self.read(1)
        assert ans[0] in [0, 1]
        return bool(ans[0])

    def writeBoolean(self, b):
        self.data += b"\x01" if b else b"\x00"

    def readByte(self):
        return int.from_bytes(self.read(1), "big", signed=True)

    def writeByte(self, b):
        self.data += b.to_bytes(1, "big", signed=True)

    def readByteArray(self):
        lon = self.readVarInt()
        return self.read(lon)

    def writeByteArray(self, ba):
        self.writeVarInt(len(ba))
        self.data += ba

    def readDouble(self):
        return struct.unpack("!d", self.read(8))[0]

    def writeDouble(self, d):
        self.data += struct.pack("!d", d)

    def readFloat(self):
        return struct.unpack("!f", self.read(4))[0]

    def writeFloat(self, f):
        self.data += struct.pack("!f", f)

    def readInt(self):
        return int.from_bytes(self.read(4), "big", signed=True)

    def writeInt(self, i):
        self.data += i.to_bytes(4, "big", signed=True)

    def readShort(self):
        return int.from_bytes(self.read(2), "big", signed=True)

    def writeShort(self, s):
        self.data += s.to_bytes(2, "big", signed=True)

    def readUTF(self):
        lon = self.readUnsignedShort()
        return self.read(lon).decode()

    def writeUTF(self, ch):
        dat = ch.encode()
        self.writeUnsignedShort(len(dat))
        self.data += dat

    def readUnsignedByte(self):
        return int.from_bytes(self.read(1), "big")

    def writeUnsignedByte(self, b):
        self.data += b.to_bytes(1, "big")

    def readUnsignedInt(self):
        return int.from_bytes(self.read(4), "big")

    def writeUnsignedInt(self, ui):
        self.data += ui.to_bytes(4, "big")

    def readUnsignedShort(self):
        return int.from_bytes(self.read(2), "big")

    def writeUnsignedShort(self, us):
        self.data += us.to_bytes(2, "big")

    def _writeVar(self, i):
        if not i:
            self.writeUnsignedByte(0)
        while i:
            b = i & 0b01111111
            i >>= 7
            if i:
                b |= 0b10000000
            self.writeUnsignedByte(b)

    def readVarInt(self):
        ans = 0
        for i in range(0, 32, 7):
            b = self.readUnsignedByte()
            ans += (b & 0b01111111) << i
            if not b & 0b10000000:
                return ans
        raise ValueError("Too much data")

    def writeVarInt(self, i):
        assert i.bit_length() <= 32
        self._writeVar(i)

    def readVarUhInt(self):
        return self.readVarInt()

    def writeVarUhInt(self, i):
        self.writeVarInt(i)

    def readVarLong(self):
        ans = 0
        for i in range(0, 64, 7):
            b = self.readUnsignedByte()
            ans += (b & 0b01111111) << i
            if not b & 0b10000000:
                return ans
        raise ValueError("Too much data")

    def writeVarLong(self, i):
        assert i.bit_length() <= 64
        self._writeVar(i)

    def readVarUhLong(self):
        return self.readVarLong()

    def writeVarUhLong(self, i):
        self.writeVarLong(i)

    def readVarShort(self):
        ans = 0
        for i in range(0, 16, 7):
            b = self.readByte()
            ans += (b & 0b01111111) << i
            if not b & 0b10000000:
                return ans
        raise ValueError("Too much data")

    def writeVarShort(self, i):
        assert i.bit_length() <= 16
        self._writeVar(i)

    def readVarUhShort(self):
        return self.readVarShort()

    def writeVarUhShort(self, i):
        self.writeVarShort(i)

    def end(self):
        del self.data[: self.pos]
        self.pos = 0


class SplittedPacket(TypedDict):
    id: int
    length: int
    count: int | None


@dataclass
class BufferInfos:
    header: int | None = None
    data: Data = Data()
    splitted_packet: SplittedPacket | None = None

    def reset(self):
        self.header = None
        self.data = Data()
        self.splitted_packet = None
