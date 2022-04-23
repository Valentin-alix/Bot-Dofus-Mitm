from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray


class ISymmetricKey:
    def getBlockSize(self) -> int:
        pass

    def encrypt(self, src: ByteArray, offset: int = 0) -> None:
        pass

    def decrypt(self, src: ByteArray, offset: int = 0) -> None:
        pass

    def dispose() -> None:
        pass

    def toString() -> str:
        pass
