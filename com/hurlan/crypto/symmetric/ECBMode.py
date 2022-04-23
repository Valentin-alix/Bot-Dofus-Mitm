from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray
from com.hurlan.crypto.symmetric.ICipher import ICipher
from com.hurlan.crypto.symmetric.IMode import IMode
from com.hurlan.crypto.symmetric.IPad import IPad
from com.hurlan.crypto.symmetric.ISymetricKey import ISymmetricKey
from com.hurlan.crypto.symmetric.PKCS5 import PKCS5

logger = Logger(__name__)


class ECBMode(IMode, ICipher):

    key: ISymmetricKey
    padding: IPad

    def __init__(self, key: ISymmetricKey, padding: IPad = None):
        super().__init__()
        self.key = key
        if padding == None:
            padding = PKCS5(key.getBlockSize())
        else:
            padding.setBlockSize(key.getBlockSize())
        self.padding = padding

    def getBlockSize(self) -> int:
        return self.key.getBlockSize()

    def encrypt(self, src: ByteArray) -> None:
        self.padding.pad(src)
        src.position = 0
        blockSize: int = self.key.getBlockSize()
        block: ByteArray = ByteArray()
        dst: ByteArray = ByteArray()
        for i in range(0, len(src), blockSize):
            block.position = 0
            block.writeByteArray(src, i, blockSize)
            self.key.encrypt(block)
            dst.writeByteArray(block)
        src.position = 0
        src.writeByteArray(dst)

    def decrypt(self, src: ByteArray) -> None:
        src.position = 0
        blockSize: int = self.key.getBlockSize()
        if len(src) % blockSize != 0:
            raise Exception(
                "ECB mode cipher length must be a multiple of blocksize " + blockSize
            )
        block: ByteArray = ByteArray()
        dst: ByteArray = ByteArray()
        for i in range(0, len(src), blockSize):
            block.position = 0
            block.writeByteArray(src, i, blockSize)
            self.key.decrypt(block)
            dst.writeByteArray(block)
        src.writeByteArray(dst)
        self.padding.unpad(src)
        src.position = 0

    def dispose(self) -> None:
        self.key.dispose()
        self.key = None
        self.padding = None

    def __str__(self) -> str:
        return str(self.key) + "-ecb"
