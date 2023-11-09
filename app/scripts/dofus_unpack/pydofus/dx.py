#!/usr/bin/python3
# -*- coding: utf-8 -*-

from ._binarystream import _BinaryStream

class InvalidDXFile(Exception):
    def __init__(self, message):
        super(InvalidDXFile, self).__init__(message)
        self.message = message

class DX:
    def __init__(self, stream):
        self._stream = stream

    def read(self, out_stream):
        raw = _BinaryStream(self._stream, True)
        _out = _BinaryStream(out_stream, True)

        file = raw.read_char()
        version = raw.read_char()
        keyLen = raw.read_int16()
        key = raw.read_bytes(keyLen)

        swfDataPosition = self._stream.tell()
        swfData = raw.read_bytes()
        swfLenght = self._stream.tell() - swfDataPosition

        for i in range(0, swfLenght):
            _out.write_uchar(swfData[i] ^ key[i % keyLen])

    def write(self, in_stream):
        raw = _BinaryStream(self._stream, True)
        _in = _BinaryStream(in_stream, True)

        key = 0 # WE DON'T NEED THIS FUCKING KEY, LET'S XOR WITH 0 !! :D

        raw.write_char(83)
        raw.write_char(0)
        raw.write_int16(1)
        raw.write_char(key)

        swfData = _in.read_bytes()
        swfLenght = in_stream.tell()

        for i in range(0, swfLenght):
            raw.write_uchar(swfData[i] ^ key)
