from com.ankamagames.dofus.kernel.Kernel import Kernel
from com.ankamagames.dofus.kernel.PanicMessages import PanicMessages
from com.ankamagames.dofus.kernel.net.ConnectionsHandler import ConnectionsHandler
from com.ankamagames.dofus.logic.game.common.actions.GameContextQuitAction import (
    GameContextQuitAction,
)
from com.ankamagames.dofus.network.enums.GameContextEnum import GameContextEnum
from com.ankamagames.dofus.network.messages.game.context.GameContextCreateMessage import (
    GameContextCreateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameContextQuitMessage import (
    GameContextQuitMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.CurrentMapMessage import (
    CurrentMapMessage,
)
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.messages.Frame import Frame
from com.ankamagames.jerakine.messages.Message import Message
from com.ankamagames.jerakine.types.enums.Priority import Priority
from pyd2bot.events.BotEventsManager import BotEventsManager

logger = Logger(__name__)


class ContextChangeFrame(Frame):
    def __init__(self):
        self.mapChangeConnexion = ""
        super().__init__()

    @property
    def priority(self) -> int:
        return Priority.LOW

    def pushed(self) -> bool:
        return True

    def process(self, msg: Message) -> bool:

        if isinstance(msg, GameContextCreateMessage):
            context = GameContextEnum(msg.context)
            if context == GameContextEnum.ROLE_PLAY:
                import com.ankamagames.dofus.logic.game.roleplay.frames.RoleplayContextFrame as rplCF

                Kernel().getWorker().addFrame(rplCF.RoleplayContextFrame())
                BotEventsManager().dispatch(BotEventsManager.SWITCH_TO_ROLEPLAY)
            elif context == GameContextEnum.FIGHT:
                # Kernel().getWorker().addFrame(FightContextFrame())
                BotEventsManager().dispatch(BotEventsManager.SWITCH_TO_FIGHT)
            else:
                Kernel().panic(PanicMessages.WRONG_CONTEXT_CREATED, [msg.context])
            return True

        if isinstance(msg, GameContextQuitAction):
            gcqmsg = GameContextQuitMessage()
            ConnectionsHandler.getConnection().send(gcqmsg)
            return True

        if isinstance(msg, CurrentMapMessage):
            mcmsg = msg
            self.mapChangeConnexion = mcmsg.sourceConnection
            return False

        else:
            return False

    def pulled(self) -> bool:
        return True
