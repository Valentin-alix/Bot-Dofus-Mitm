from com.ankamagames.jerakine.data.BinaryStream import BinaryStream


class Fixture:
    def __init__(self, raw):
        self.read(raw)

    def read(self, raw: BinaryStream):
        self.fixtureId = raw.readInt()
        self.offsetX = raw.readShort()
        self.offsetY = raw.readShort()
        self.rotation = raw.readShort()
        self.xScale = raw.readShort()
        self.yScale = raw.readShort()
        self.redMultiplier = raw.readByte()
        self.greenMultiplier = raw.readByte()
        self.blueMultiplier = raw.readByte()
        self.hue = self.redMultiplier | self.greenMultiplier | self.blueMultiplier
        self.alpha = raw.readUchar()
