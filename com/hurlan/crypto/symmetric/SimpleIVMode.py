from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray
from com.hurlan.crypto.symmetric import IMode
from com.hurlan.crypto.symmetric.ICipher import ICipher
from com.hurlan.crypto.symmetric.IMode import IMode


class SimpleIVMode(IMode, ICipher):
    def __init__(self, mode: IMode):
        self.mode = mode
        self.cipher: ICipher = mode

    def getBlockSize(self):
        return self.mode.getBlockSize()

    def dispose(self):
        self.mode.dispose()
        self.mode = None
        self.cipher = None

    def encrypt(self, src: ByteArray):
        self.cipher.encrypt(src)
        tmp: ByteArray = ByteArray()
        tmp.writeByteArray(self.mode.IV)
        tmp.writeByteArray(src)
        src.position = 0
        src.writeByteArray(tmp)

    def decrypt(self, src: ByteArray):
        tmp: ByteArray = ByteArray()
        tmp.writeByteArray(src, 0, self.getBlockSize())
        self.mode.iv = tmp
        tmp = ByteArray()
        tmp.writeByteArray(src, self.getBlockSize())
        self.cipher.decrypt(tmp)
        src.__init__()
        src.writeByteArray(tmp)

    def toString(self):
        return "simple-" + self.cipher.toString()
