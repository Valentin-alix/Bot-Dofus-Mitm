class boolByteWrapper:
    def __init__(self):
        super().__init__()

    @staticmethod
    def setFlag(a: int, pos: int, b: bool) -> int:
        if pos == 0:
            if b:
                a |= 1
            a &= 255 - 1
        elif pos == 1:
            if b:
                a |= 2
            a &= 255 - 2
        elif pos == 2:
            if b:
                a |= 4
            a &= 255 - 4
        elif pos == 3:
            if b:
                a |= 8
            a &= 255 - 8
        elif pos == 4:
            if b:
                a |= 16
            a &= 255 - 16
        elif pos == 5:
            if b:
                a |= 32
            a &= 255 - 32
        elif pos == 6:
            if b:
                a |= 64
            a &= 255 - 64
        elif pos == 7:
            if b:
                a |= 128
            a &= 255 - 128
        else:
            raise Exception("Bytebox overflow.")
        return a

    @staticmethod
    def getFlag(a: int, pos: int) -> bool:
        if pos == 0:
            return (a & 1) != 0
        elif pos == 1:
            return (a & 2) != 0
        elif pos == 2:
            return (a & 4) != 0
        elif pos == 3:
            return (a & 8) != 0
        elif pos == 4:
            return (a & 16) != 0
        elif pos == 5:
            return (a & 32) != 0
        elif pos == 6:
            return (a & 64) != 0
        elif pos == 7:
            return (a & 128) != 0
        else:
            raise Exception("Bytebox overflow.")
