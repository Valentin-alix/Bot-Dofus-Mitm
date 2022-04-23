from com.ankamagames.jerakine.sequencer.ISequencable import ISequencable


class IPausableSequencable(ISequencable):
    def pause(self) -> None:
        pass

    def resume(self) -> None:
        pass
