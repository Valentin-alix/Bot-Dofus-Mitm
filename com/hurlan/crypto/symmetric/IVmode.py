from random import Random
from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray
from com.hurlan.crypto.symmetric.IPad import IPad
from com.hurlan.crypto.symmetric.ISymetricKey import ISymmetricKey
from com.hurlan.crypto.symmetric.PKCS5 import PKCS5


class IVMode:
    def __init__(self, key: ISymmetricKey, padding: IPad = None):
        self.key = key
        self.blockSize = key.getBlockSize()
        if padding == None:
            padding = PKCS5(self.blockSize)
        else:
            padding.setBlockSize(self.blockSize)
        self.padding = padding
        self.prng = Random()
        self.iv = ByteArray()
        self.lastIV = ByteArray()

    def getBlockSize(self):
        return self.key.getBlockSize()

    def dispose(self):
        if self.iv is not None:
            for i in range(len(self.iv)):
                self.iv[i] = self.prng.getrandbits(8)
            self.iv.length = 0
            self.iv = None

        if self.lastIV is not None:
            for i in range(len(self.lastIV)):
                self.lastIV[i] = self.prng.getrandbits(8)
            self.lastIV.length = 0
            self.lastIV = None

        self.key.dispose()
        self.key = None
        self.padding = None
        self.prng = None

    @property
    def IV(self) -> ByteArray:
        return self.lastIV

    @IV.setter
    def IV(self, value: ByteArray):
        self.iv = value
        self.lastIV.length = 0
        self.lastIV.writeByteArray(self.iv)

    def getIV4e(self) -> ByteArray:
        vec: ByteArray = ByteArray()
        if self.iv:
            vec.writeByteArray(self.iv)
        else:
            vec = ByteArray(
                self.prng.getrandbits(8 * self.blockSize).to_bytes(
                    self.blockSize, "big"
                )
            )
        self.lastIV.length = 0
        self.lastIV.writeByteArray(vec)
        return vec

    def getIV4d(self) -> ByteArray:
        vec: ByteArray = ByteArray()
        if self.iv:
            vec.writeByteArray(self.iv)
            return vec
        raise Exception("an IV must be set before calling decrypt()")
