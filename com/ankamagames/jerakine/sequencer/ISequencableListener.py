from com.ankamagames.jerakine.sequencer.ISequencable import ISequencable


class ISequencableListener:
    def stepFinished(self, param1: ISequencable, param2: bool = False) -> None:
        pass
