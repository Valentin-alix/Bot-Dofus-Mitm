from whistle import EventDispatcher
from com.ankamagames.jerakine.events.FramePulledEvent import FramePulledEvent
from com.ankamagames.jerakine.logger.Logger import Logger
from time import perf_counter
from types import FunctionType
from com.ankamagames.jerakine.messages.ForTreatment import ForTreatment
from com.ankamagames.jerakine.messages.ForeachTreatment import ForeachTreatment
from com.ankamagames.jerakine.messages.Frame import Frame
from com.ankamagames.jerakine.messages.Message import Message
from com.ankamagames.jerakine.messages.Treatment import Treatment
from com.ankamagames.jerakine.messages.WhileTreatment import WhileTreatment
from com.ankamagames.jerakine.messages.CancelableMessages import CancelableMessage
from com.ankamagames.jerakine.messages.DiscardableMessage import DiscardableMessage
from com.ankamagames.jerakine.messages.MessageHandler import MessageHandler
from com.ankamagames.jerakine.messages.QueueableMessage import QueueableMessage
from com.ankamagames.jerakine.messages.events.FramePushedEvent import FramePushedEvent
from com.ankamagames.jerakine.pools.GenericPool import GenericPool
from com.ankamagames.jerakine.pools.Poolable import Poolable
import com.ankamagames.jerakine.utils.display.EnterFrameDispatcher as efd
from com.ankamagames.jerakine.utils.display.FrameIdManager import FrameIdManager

logger = Logger(__name__)


class Worker(EventDispatcher, MessageHandler):

    DEBUG_FRAMES: bool = False
    DEBUG_MESSAGES: bool = False
    DEBUG_FRAMES_PROCESSING: bool = False
    LONG_MESSAGE_QUEUE: int = 100
    MAX_TIME_FRAME: int = 40

    def __init__(self):
        self._unstoppableMsgobjectList = list()
        self._framesBeingDeleted = dict()
        self._messagesQueue = list[Message]()
        self._treatmentsQueue = list[Treatment]()
        self._framesList = list[Frame]()
        self._processingMessage = False
        self._framesToAdd = list[Frame]()
        self._framesToRemove = list[Frame]()
        self._paused = False
        self._pausedQueue = list[Message]()
        self._terminated: bool = False
        self._terminating: bool = False
        self._unstoppableMsgobjectList = list()
        self._currentFrameTypesCache = dict()
        super().__init__()

    @property
    def framesList(self) -> list[Frame]:
        return self._framesList

    @property
    def isPaused(self) -> bool:
        return self._paused

    @property
    def pausedQueue(self) -> list[Message]:
        return self._pausedQueue

    @property
    def terminated(self) -> bool:
        return self._terminated

    @property
    def terminating(self) -> bool:
        return self._terminating

    def process(self, msg: Message) -> bool:
        if self._terminated:
            return False
        self._messagesQueue.append(msg)
        self.run()
        return True

    def addSingleTreatmentAtPos(
        self, object, func: FunctionType, params: list, pos: int
    ) -> None:
        if len(self._treatmentsQueue) == 0:
            efd.EnterFrameDispatcher().addWorker(self)
        self._treatmentsQueue.insert(pos, Treatment(object, func, params))

    def addSingleTreatment(self, object, func: FunctionType, params: list) -> None:
        if len(self._treatmentsQueue) == 0:
            efd.EnterFrameDispatcher().addWorker(self)
        self._treatmentsQueue.append(Treatment(object, func, params))

    def addUniqueSingleTreatment(
        self, object, func: FunctionType, params: list
    ) -> None:
        if len(self._treatmentsQueue) == 0:
            efd.EnterFrameDispatcher().addWorker(self)
        if not self.hasSingleTreatment(object, func, params):
            self._treatmentsQueue.append(Treatment(object, func, params))

    def addForTreatment(
        self, object, func: FunctionType, params: list, iterations: int
    ) -> None:
        if iterations == 0:
            return
        if len(self._treatmentsQueue) == 0:
            efd.EnterFrameDispatcher().addWorker(self)
        self._treatmentsQueue.append(
            ForTreatment(object, func, params, iterations, self)
        )

    def addForeachTreatment(
        self, object, func: FunctionType, params: list, iterable
    ) -> None:
        if len(self._treatmentsQueue) == 0:
            efd.EnterFrameDispatcher().addWorker(self)
        self._treatmentsQueue.append(
            ForeachTreatment(object, func, params, iterable, self)
        )

    def addWhileTreatment(self, object, func: FunctionType, params: list) -> None:
        if len(self._treatmentsQueue) == 0:
            efd.EnterFrameDispatcher().addWorker(self)
        self._treatmentsQueue.append(WhileTreatment(object, func, params))

    def hasSingleTreatment(self, object, func: FunctionType, params: list) -> bool:
        treatment: Treatment = None
        for treatment in self._treatmentsQueue:
            if treatment.isSameTreatment(object, func, params):
                return True
        return False

    def findTreatments(self, object, func: FunctionType, params: list) -> list:
        treatment: Treatment = None
        result: list = []
        for treatment in self._treatmentsQueue:
            if treatment.isCloseTreatment(object, func, params):
                result.append(treatment)
        return result

    def deleteTreatments(self, treatments: list) -> None:
        treatment: Treatment = None
        for treatment in treatments:
            del self._treatmentsQueue[self._treatmentsQueue.find(treatment)]

    def processImmediately(self, msg: Message) -> bool:
        if self._terminated:
            return False
        self.processMessage(msg)
        return True

    def addFrame(self, frame: Frame) -> None:
        if self._terminated:
            return
        if self._currentFrameTypesCache.get(type(frame)):
            frameRemoving = False
            frameAdding = False
            if self._processingMessage:
                for f in self._framesToAdd:
                    if type(f) == type(frame):
                        frameAdding = True
                        break
                if not frameAdding:
                    for f in self._framesToRemove:
                        if type(f) == type(frame):
                            frameRemoving = True
                            break
            if not frameRemoving or frameAdding:
                logger.error(
                    "Someone asked for the frame "
                    + frame
                    + " to be "
                    + "added to the worker, but there is already another "
                    + "frame of the same type within it."
                )
                return

        if not frame:
            return

        if self.DEBUG_FRAMES:
            logger.info("Adding frame: " + frame.__class__.__name__)

        if (
            self._processingMessage
            or len(self._framesToRemove) > 0
            or len(self._framesToAdd) > 0
        ):
            isAlreadyIn = False
            for f in self._framesToAdd:
                if f.__class__.__name__ == frame.__class__.__name__:
                    isAlreadyIn = True
            if not isAlreadyIn:
                self._framesToAdd.append(frame)

        else:
            self.pushFrame(frame)

    def removeFrame(self, frame: Frame) -> None:
        if self._terminated:
            return

        if not frame:
            return

        if self.DEBUG_FRAMES:
            logger.info(f"Removing frame: {frame.__class__.__name__}")

        if self._processingMessage or len(self._framesToRemove) > 0:
            self._framesToRemove.append(frame)

        elif not self.isBeingDeleted(frame):
            self._framesBeingDeleted[frame] = True
            self.pullFrame(frame)

    def isBeingDeleted(self, frame: Frame) -> bool:
        fr = None
        for fr in self._framesBeingDeleted:
            if fr == frame:
                return True
        return False

    def isBeingAdded(self, frame: object) -> bool:
        fr = None
        for fr in self._framesToAdd:
            if fr is frame:
                return True
        return False

    def contains(self, frameobject: object) -> bool:
        return self.getFrame(frameobject) != None

    def getFrame(self, frameobject: object) -> Frame:
        return self._currentFrameTypesCache.get(frameobject)

    def pause(
        self, targetobject: object = None, unstoppableMsgobjectList: list = None
    ) -> None:
        logger.info("Worker is paused, all queueable messages will be queued : ")
        self._paused = True
        if unstoppableMsgobjectList:
            self._unstoppableMsgobjectList = self._unstoppableMsgobjectList.extend(
                unstoppableMsgobjectList
            )

    def clearUnstoppableMsgobjectList(self) -> None:
        self._unstoppableMsgobjectList = []

    def msgIsUnstoppable(self, msg: Message) -> bool:
        msgobject: object = None
        for msgobject in self._unstoppableMsgobjectList:
            if msg is msgobject:
                return True
        return False

    def resume(self) -> None:
        if self._terminated:
            return
        if not self._paused:
            return
        logger.info("Worker is resuming, processing all queued messages.")
        self._paused = False
        self._messagesQueue = self._messagesQueue.extend(self._pausedQueue)
        self._pausedQueue = list[Message]()
        self.processFramesInAndOut()
        self.processQueues()

    def terminate(self) -> None:
        self._terminating = True
        self.clear()
        self._terminating = False
        self._terminated = True

    def clear(self) -> None:
        frameList: list[Frame] = None
        frame: Frame = None
        if self.DEBUG_FRAMES:
            logger.info("Clearing worker (no more frames or messages in queue)")
        nonPulledFrameList = [f for f in self._framesList if not f.pulled()]
        self._framesList = list[Frame]()
        self._framesToAdd = list[Frame]()
        self._framesToRemove = list[Frame]()
        self._messagesQueue = list[Message]()
        self._treatmentsQueue = list[Treatment]()
        self._pausedQueue = list[Message]()
        self._currentFrameTypesCache = dict()
        for frame in nonPulledFrameList:
            self.pushFrame(frame)
        efd.EnterFrameDispatcher().removeWorker()
        self._paused = False

    def onEnterFrame(self) -> None:
        self.processQueues()

    def run(self) -> None:
        efd.EnterFrameDispatcher().addWorker(self)

    def pushFrame(self, frame: Frame) -> None:
        if frame.pushed():
            self._framesList.append(frame)
            self._framesList.sort(key=lambda x: x.priority.value, reverse=True)
            self._currentFrameTypesCache[type(frame)] = frame
            if self.has_listeners(FramePushedEvent.EVENT_FRAME_PUSHED):
                self.dispatch(
                    FramePushedEvent.EVENT_FRAME_PUSHED, FramePushedEvent(frame)
                )
        else:
            logger.warn(
                "Frame " + frame.__class__.__name__ + " refused to be.appended."
            )

    def pullFrame(self, frame: Frame) -> None:
        index: int = 0
        if frame.pulled():
            try:
                index = self._framesList.index(frame)
            except:
                index = -1
            if index > -1:
                del self._framesList[index]
                del self._currentFrameTypesCache[type(frame)]
                if frame in self._framesBeingDeleted:
                    del self._framesBeingDeleted[frame]
            if self.has_listeners(FramePulledEvent.EVENT_FRAME_PULLED):
                self.dispatch(
                    FramePulledEvent.EVENT_FRAME_PULLED, FramePulledEvent(frame)
                )
        else:
            logger.warn(f"Frame {frame.__class__.__name__} refused to be pulled.")

    def processQueues(self, maxTime: int = 40) -> None:
        startTime: int = perf_counter()
        while perf_counter() - startTime < maxTime and (
            len(self._messagesQueue) > 0 or len(self._treatmentsQueue) > 0
        ):
            if len(self._treatmentsQueue) > 0:
                self.processTreatments(startTime, maxTime)
                if len(self._treatmentsQueue) == 0:
                    self.processFramesInAndOut()
            else:
                msg = self._messagesQueue.pop(0)
                if not isinstance(msg, CancelableMessage) or msg.cancel:
                    if (
                        self._paused
                        and isinstance(msg, QueueableMessage)
                        and not self.msgIsUnstoppable(msg)
                    ):
                        self._pausedQueue.append(msg)
                        logger.warn("Queued message: " + msg.__class__.__name__)
                    else:
                        self.processMessage(msg)
                        if isinstance(msg, Poolable):
                            GenericPool().free(msg)
                        if len(self._treatmentsQueue) == 0:
                            self.processFramesInAndOut()
        if len(self._messagesQueue) == 0 and len(self._treatmentsQueue) == 0:
            efd.EnterFrameDispatcher().removeWorker()

    def processTreatments(self, startTime: int, maxTime: int) -> None:
        treatment: Treatment = None
        while perf_counter() - startTime < maxTime and len(self._treatmentsQueue) > 0:
            treatment = self._treatmentsQueue[0]
            if treatment.process():
                del self._treatmentsQueue[self._treatmentsQueue.find(treatment)]

    def aNoneFlood(self, messageName: str) -> bool:
        if len(self._messagesQueue) > self.LONG_MESSAGE_QUEUE:
            count = 0
            toClean = []
            for i in range(len(self._messagesQueue)):
                if self._messagesQueue[i].__class__.__name__ == messageName:
                    count += 1
                    toClean.append(self._messagesQueue[i])
            if count > 10:
                for i in range(len(toClean)):
                    del self._messagesQueue[self._messagesQueue.find(toClean[i])]
                return True
        return False

    def processMessage(self, msg: Message) -> None:
        processed: bool = False
        self._processingMessage = True
        for frame in self._framesList:
            if self.DEBUG_FRAMES_PROCESSING:
                logger.debug(
                    "Processing message: "
                    + msg.__class__.__name__
                    + " in frame: "
                    + frame.__class__.__name__
                )
            if frame.process(msg):
                processed = True
                break
        self._processingMessage = False
        if not processed and not isinstance(msg, DiscardableMessage):
            logger.debug(
                f"Discarded message: {msg.__class__.__name__} (at frame {FrameIdManager().frameId})"
            )

    def processFramesInAndOut(self) -> None:
        if len(self._framesToRemove) > 0:
            for frameToRemove in self._framesToRemove:
                self.pullFrame(frameToRemove)
            del self._framesToRemove[0 : len(self._framesToRemove)]
        if len(self._framesToAdd) > 0:
            for frameToAdd in self._framesToAdd:
                self.pushFrame(frameToAdd)
            del self._framesToAdd[0 : len(self._framesToAdd)]
