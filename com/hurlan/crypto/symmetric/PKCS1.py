import os
from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray
from com.hurlan.crypto.symmetric.IPad import IPad


class PKCS1(IPad):
    blockSize: int

    def __init__(self, blockSize: int = 0):
        super().__init__()
        self.blockSize = blockSize

    def unpad(self, m, type=2):
        """removes padding returns none if padding is invalid"""
        if len(m) != self.blockSize:
            return
        if m[0] != 0 or m[1] != type:
            return
        # first nonzero byte (after 00 02) marks end of padding
        i = 2
        while i < len(m) and m[i] != 0:
            i += 1
        # check that 00 byte was actually found
        if i >= len(m):
            return
        pad_len = i - 2
        # must have at least 8 bytes of random padding
        if pad_len < 8:
            return
        return m[3 + pad_len :]

    def pad(self, message: ByteArray) -> bytes:
        """Pads the message for encryption, returning the padded message.
        :return: 00 02 RANDOM_DATA 00 MESSAGE
        """
        max_msglength = self.blockSize - 11
        msglength = len(message)
        if msglength > max_msglength:
            raise OverflowError(
                "%i bytes needed for message, but there is only"
                " space for %i" % (msglength, max_msglength)
            )
        padding = b""
        padding_length = self.blockSize - msglength - 3
        while len(padding) < padding_length:
            needed_bytes = padding_length - len(padding)
            new_padding = os.urandom(needed_bytes + 5)
            new_padding = new_padding.replace(b"\x00", b"")
            padding = padding + new_padding[:needed_bytes]
        assert len(padding) == padding_length
        return b"".join([b"\x00\x02", padding, b"\x00", message])

    def setBlockSize(self, bs: int) -> None:
        self.blockSize = bs
