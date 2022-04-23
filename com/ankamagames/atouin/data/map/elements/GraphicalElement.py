from com.ankamagames.jerakine.data.BinaryStream import BinaryStream


class GraphicalElement:
    def __init__(self, raw: BinaryStream, mapVersion):
        self.mapVersion = mapVersion
        self.elementName = "Graphical"
        self.read(raw)

    def read(self, raw: BinaryStream):
        self.elementId = raw.readUnsignedInt()

        # hue
        self.hue_1 = raw.readByte()
        self.hue_2 = raw.readByte()
        self.hue_3 = raw.readByte()

        # shadow
        self.shadow_1 = raw.readByte()
        self.shadow_2 = raw.readByte()
        self.shadow_3 = raw.readByte()

        if self.mapVersion <= 4:
            self.offsetX = raw.readByte()
            self.offsetY = raw.readByte()

        else:
            self.offsetX = raw.readShort()
            self.offsetY = raw.readShort()

        self.altitude = raw.readByte()
        self.identifier = raw.readUnsignedInt()
