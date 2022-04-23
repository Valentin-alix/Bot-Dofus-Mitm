from whistle import EventDispatcher
from com.ankamagames.jerakine.events.SequencerEvent import SequencerEvent
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.network.messages.Worker import Worker
from com.ankamagames.jerakine.sequencer.IPausableSequencable import IPausableSequencable
from com.ankamagames.jerakine.sequencer.ISequencable import ISequencable
from com.ankamagames.jerakine.sequencer.ISequencer import ISequencer
from com.ankamagames.jerakine.sequencer.ISubSequenceSequencable import (
    ISubSequenceSequencable,
)
from com.ankamagames.jerakine.utils.display.EnterFrameDispatcher import (
    EnterFrameDispatcher,
)
from com.ankamagames.jerakine.sequencer.AbstractSequencable import AbstractSequencable

logger = Logger(__name__)


class SerialSequencer(EventDispatcher, ISequencer):

    DEFAULT_SEQUENCER_NAME: str = "SerialSequencerDefault"

    SEQUENCERS: list = []

    _aStep: list

    _currentStep: ISequencable

    _lastStep: ISequencable

    _running: bool = False

    _type: str

    _activeSubSequenceCount: int

    _paused: bool

    _defaultStepTimeout: int = -2147483648

    def __init__(self, type: str = "SerialSequencerDefault"):
        self._aStep = list()
        super().__init__()
        if not self.SEQUENCERS[type]:
            self.SEQUENCERS[type] = dict(True)
        self.SEQUENCERS[type][self] = True

    def clearByType(self, type: str) -> None:
        seq = None
        for seq in self.SEQUENCERS[type]:
            SerialSequencer(seq).clear()
        del self.SEQUENCERS[type]

    @property
    def currentStep(self) -> ISequencable:
        return self._currentStep

    @property
    def lastStep(self) -> ISequencable:
        return self._lastStep

    @property
    def length(self) -> int:
        return len(self._aStep)

    @property
    def running(self) -> bool:
        return self._running

    @property
    def steps(self) -> list:
        return self._aStep

    @property
    def defaultStepTimeout(self) -> int:
        return self._defaultStepTimeout

    @defaultStepTimeout.setter
    def defaultStepTimeout(self, v: int) -> None:
        self._defaultStepTimeout = v

    def pause(self) -> None:
        self._paused = True
        if isinstance(self._currentStep, IPausableSequencable):
            self._currentStep.pause()

    def resume(self) -> None:
        self._paused = False
        if isinstance(self._currentStep, IPausableSequencable):
            self._currentStep.start()

    def add(self, item: ISequencable) -> None:
        if item:
            self.addStep(item)
        else:
            logger.error(
                "Tried to add a null step to the LUA script sequence, self step will be ignored"
            )

    def addStep(self, item: ISequencable) -> None:
        self._aStep.append(item)

    def start(self) -> None:
        if not self._running:
            self._running = len(self._aStep) != 0
            if self._running:
                while len(self._aStep) > 0 and self._running:
                    self.execute()
                    if (
                        self._currentStep
                        and isinstance(self._currentStep, AbstractSequencable)
                        and not self._currentStep
                    ):
                        self._running = False
                    if self._running and not EnterFrameDispatcher().remainsTime():
                        self._running = False
                        worker = EnterFrameDispatcher().worker
                        worker.addSingleTreatmentAtPos(
                            self,
                            self.start,
                            [],
                            len(worker.findTreatments(None, self.start, [])),
                        )
            else:
                self.dispatch(SequencerEvent.SEQUENCE_END, SequencerEvent(self))

    def clear(self) -> None:
        step: ISequencable = None
        self._lastStep = None
        if self._currentStep:
            self._currentStep.clear()
            self._currentStep = None
        for step in self._aStep:
            if step:
                step.clear()
        self._aStep = list()
        self._running = False

    def __str__(self) -> str:
        str: str = ""
        for step in self._aStep:
            str += str(step) + "\n"
        return str

    def execute(self) -> None:
        self._lastStep = self._currentStep
        self._currentStep = self._aStep.pop(0)
        if not self._currentStep:
            return
        # FightProfiler().start()
        self._currentStep.addListener(self)
        try:
            if isinstance(self._currentStep, ISubSequenceSequencable):
                self._activeSubSequenceCount += 1
                self._currentStep.add_listener(
                    SequencerEvent.SEQUENCE_END, self.onSubSequenceEnd
                )
            if (
                self._defaultStepTimeout != int.MIN_VALUE
                and self._currentStep.hasDefaultTimeout
            ):
                self._currentStep.timeout = self._defaultStepTimeout
            if self.has_listeners(SequencerEvent.SEQUENCE_STEP_START):
                self.dispatch(
                    SequencerEvent.SEQUENCE_STEP_START,
                    SequencerEvent(self, self._currentStep),
                )
            self._currentStep.start()
        except Exception as e:
            if isinstance(self._currentStep, ISubSequenceSequencable):
                self._activeSubSequenceCount -= 1
                ISubSequenceSequencable(self._currentStep).remove_listener(
                    SequencerEvent.SEQUENCE_END, self.onSubSequenceEnd
                )
            logger.error(f"Exception sur la step {self._currentStep}", exc_info=True)
            if isinstance(self._currentStep, AbstractSequencable):
                self._currentStep.finished = True
            self.stepFinished(self._currentStep)

    def stepFinished(self, step: ISequencable, withTimout: bool = False) -> None:
        worker: Worker = None
        step.removeListener(self)
        if self._running:
            if withTimout:
                self.dispatch(SequencerEvent.SEQUENCE_TIMEOUT, SequencerEvent(self))
            if self.has_listeners(SequencerEvent.SEQUENCE_STEP_FINISH):
                self.dispatch(
                    SequencerEvent.SEQUENCE_STEP_FINISH,
                    SequencerEvent(self, self._currentStep),
                )
            self._running = len(self._aStep) != 0
            if not self._running:
                if not self._activeSubSequenceCount:
                    self.dispatch(SequencerEvent.SEQUENCE_END, SequencerEvent(self))
                else:
                    self._running = True
        else:
            if self.has_listeners(SequencerEvent.SEQUENCE_STEP_FINISH):
                self.dispatch(
                    SequencerEvent(
                        SequencerEvent.SEQUENCE_STEP_FINISH, self, self._currentStep
                    )
                )
            worker = EnterFrameDispatcher().worker
            worker.addSingleTreatmentAtPos(
                self, self.start, [], worker.findTreatments(None, self.start, []).length
            )

    def onSubSequenceEnd(self, e: SequencerEvent) -> None:
        self._activeSubSequenceCount -= 1
        if not self._activeSubSequenceCount and len(self._aStep) <= 0:
            self._running = False
            self.dispatch(SequencerEvent.SEQUENCE_END, SequencerEvent(self))
