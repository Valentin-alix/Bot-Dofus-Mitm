#!/usr/bin/python3
# -*- coding: utf-8 -*-

import io
from struct import *


class BinaryStream:
    """Allow some binary operations on a stream opened in binary mode"""

    def __init__(self, base_stream: io.BytesIO = None, big_endian=False):
        if not base_stream:
            self._stream = io.BytesIO()
        self._stream = base_stream
        self._big_endian = big_endian

    @property
    def position(self):
        return self._stream.tell()

    @position.setter
    def position(self, value):
        self._stream.seek(value)

    def seek(self, value: int):
        self._stream.seek(value)

    def close(self):
        self._stream.close()

    def remaining(self):
        position = self._stream.tell()
        self._stream.seek(0, 2)
        eof = self._stream.tell()
        self._stream.seek(position, 0)
        return eof - position

    def readByte(self):
        return self._stream.read(1)

    def readBytes(self, length=None):
        if length is None:
            bytes = self._stream.read()
        else:
            bytes = self._stream.read(length)
        return bytes

    def readByte(self):
        return self._unpack("b")

    def readUnsignedByte(self) -> int:
        return int.from_bytes(self.readBytes(1), "big")

    def readUchar(self):
        return self._unpack("B")

    def readbool(self) -> bool:
        return self._unpack("?")

    def readShort(self):
        return self._unpack("h", 2)

    def readUnsignedShort(self):
        return self._unpack("H", 2)

    def readInt(self) -> int:
        return self._unpack("i", 4)

    def readUnsignedInt(self) -> int:
        return self._unpack("I", 4)

    def readInt64(self) -> int:
        return self._unpack("q", 8)

    def readUint64(self) -> int:
        return self._unpack("Q", 8)

    def readFloat(self) -> float:
        return self._unpack("f", 4)

    def readDouble(self) -> float:
        return self._unpack("d", 8)

    def readUTF(self) -> str:
        length = self.readUnsignedShort()
        return self._unpack(str(length) + "s", length).decode("utf-8")

    def readUTFBytes(self, length) -> str:
        return self._unpack(str(length) + "s", length)

    def _unpack(self, fmt, length=1):
        bytes = self.readBytes(length)
        if self._big_endian:
            fmt = ">" + fmt
        else:
            fmt = "<" + fmt
        return unpack(fmt, bytes)[0]
