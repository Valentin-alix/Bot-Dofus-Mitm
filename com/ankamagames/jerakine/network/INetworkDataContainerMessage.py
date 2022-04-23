from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray


class INetworkDataContainerMessage:
    @property
    def content() -> ByteArray:
        pass

    @content.setter
    def content(self, value: ByteArray):
        pass
