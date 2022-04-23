from time import sleep
from com.ankamagames.dofus.logic.common.managers.StatsManager import StatsManager
from com.ankamagames.dofus.logic.connection.managers.AuthentificationManager import (
    AuthentificationManager,
)
from com.ankamagames.dofus.logic.game.fight.managers.FightersStateManager import (
    FightersStateManager,
)
import com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager as pcm
from com.ankamagames.dofus.network.Metadata import Metadata
from com.ankamagames.jerakine.network.messages.Worker import Worker
from com.ankamagames.jerakine.metaclasses.Singleton import Singleton
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.utils.display.FrameIdManager import FrameIdManager

logger = Logger("kernel")


class Kernel(metaclass=Singleton):
    _worker: Worker = Worker()
    beingInReconection: bool = False

    def getWorker(self) -> Worker:
        return self._worker

    def panic(self, errorId: int = 0, panicArgs: list = None) -> None:
        from com.ankamagames.dofus.kernel.net.ConnectionsHandler import (
            ConnectionsHandler,
        )

        self._worker.clear()
        ConnectionsHandler.closeConnection()

    def init(self) -> None:
        FrameIdManager()
        self._worker.clear()
        self.addInitialFrames(True)
        logger.info(
            f"Using protocole #{Metadata.PROTOCOL_BUILD}, built on {Metadata.PROTOCOL_DATE}"
        )

    def reset(
        self,
        messagesToDispatchAfter: list = None,
        autoRetry: bool = False,
        reloadData: bool = False,
    ) -> None:
        import com.ankamagames.dofus.logic.game.fight.managers.CurrentPlayedFighterManager as cpfm

        StatsManager.clear()
        if not autoRetry:
            AuthentificationManager.clear()
        FightersStateManager().endFight()
        cpfm.CurrentPlayedFighterManager().endFight()
        cpc = pcm.PlayedCharacterManager()
        del cpc
        self._worker.clear()
        self.addInitialFrames(reloadData)
        self.beingInReconection = False
        if messagesToDispatchAfter is not None and len(messagesToDispatchAfter) > 0:
            for msg in messagesToDispatchAfter:
                self._worker.process(msg)

    def addInitialFrames(self, firstLaunch: bool = False) -> None:
        import com.ankamagames.dofus.logic.connection.frames.DisconnectionHandlerFrame as dhF
        from com.ankamagames.dofus.logic.connection.frames.AuthentificationFrame import (
            AuthentificationFrame,
        )
        from com.ankamagames.dofus.logic.common.frames.CleanupCrewFrame import (
            CleanupCrewFrame,
        )
        from com.ankamagames.dofus.logic.common.frames.QueueFrame import QueueFrame

        self._worker.addFrame(AuthentificationFrame())
        self._worker.addFrame(QueueFrame())
        if not self._worker.contains(CleanupCrewFrame):
            self._worker.addFrame(CleanupCrewFrame())
        self.getWorker().addFrame(dhF.DisconnectionHandlerFrame())
        # Kernel().getWorker().addFrame(GameStartingFrame())
        # if not self._worker.contains(LatencyFrame):
        #    self._worker.addFrame(LatencyFrame())
        # if not self._worker.contains(ServerControlFrame):
        #    self._worker.addFrame(ServerControlFrame())
        # if not self._worker.contains(AuthorizedFrame):
        #    self._worker.addFrame(AuthorizedFrame())
