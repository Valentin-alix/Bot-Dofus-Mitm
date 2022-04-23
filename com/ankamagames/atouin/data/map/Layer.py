from com.ankamagames.atouin.data.map.elements.GraphicalElement import GraphicalElement
from com.ankamagames.atouin.data.map.elements.SoundElement import SoundElement
from com.ankamagames.jerakine.data.BinaryStream import BinaryStream


class Layer:
    def __init__(self, raw, mapVersion):
        self.version = mapVersion
        self.read(raw)

    def read(self, raw: BinaryStream):
        if self.version >= 9:
            self.layerId = raw.readByte()

        else:
            self.layerId = raw.readInt()
        self.cellsCount = raw.readShort()
        self.cells = [LayerCell(raw, self.version) for _ in range(self.cellsCount)]


class LayerCell:
    def __init__(self, raw: BinaryStream, mapVersion):
        self.mapVersion = mapVersion
        self.read(raw)

    def read(self, raw: BinaryStream):
        self.cellId = raw.readShort()
        self.elementsCount = raw.readShort()
        self.elements = []
        for _ in range(self.elementsCount):
            el_type = raw.readByte()
            if el_type == 2:  # GRAPHICAL
                el = GraphicalElement(raw, self.mapVersion)
            elif el_type == 33:  # SOUND
                el = SoundElement(raw, self.mapVersion)
            else:
                raise Exception("Invalid element type.")
            self.elements.append(el)
