from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray
from com.hurlan.crypto.symmetric.IPad import IPad
from com.hurlan.crypto.symmetric.ISymetricKey import ISymmetricKey
from com.hurlan.crypto.symmetric.IVmode import IVMode


class CBCMode(IVMode):
    def __init__(self, key: ISymmetricKey, padding: IPad = None):
        super(CBCMode, self).__init__(key, padding)

    def encrypt(self, src: ByteArray):
        j = 0
        self.padding.pad(src)
        vector: ByteArray = self.getIV4e()
        for i in range(0, len(src), self.blockSize):
            for j in range(self.blockSize):
                src[i + j] ^= vector[j]
            self.key.encrypt(src, i)
            vector.position = 0
            vector.writeByteArray(src, i, self.blockSize)

    def decrypt(self, src: ByteArray):
        j = 0
        vector: ByteArray = self.getIV4d()
        tmp: ByteArray = ByteArray()
        for i in range(0, len(src), self.blockSize):
            tmp.position = 0
            tmp.writeByteArray(src, i, self.blockSize)
            self.key.decrypt(src, i)
            for j in range(self.blockSize):
                src[i + j] ^= vector[j]
            vector.position = 0
            vector.writeByteArray(tmp, 0, self.blockSize)
        self.padding.unpad(src)

    def toString(self):
        return self.key.toString() + "-cbc"
