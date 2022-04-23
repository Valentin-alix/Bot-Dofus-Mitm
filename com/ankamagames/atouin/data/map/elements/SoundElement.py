from com.ankamagames.jerakine.data.BinaryStream import BinaryStream


class SoundElement:
    def __init__(self, raw: BinaryStream, mapVersion):
        self.mapVersion = mapVersion
        self.elementName = "Sound"
        self.read(raw)

    def read(self, raw: BinaryStream):
        self.soundId = raw.readInt()
        self.baseVolume = raw.readShort()
        self.fullVolumeDistance = raw.readInt()
        self.nullVolumeDistance = raw.readInt()
        self.minDelayBetweenLoops = raw.readShort()
        self.maxDelayBetweenLoops = raw.readShort()
