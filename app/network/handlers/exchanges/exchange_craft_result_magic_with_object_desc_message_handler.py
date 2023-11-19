import logging

from app.gui.signals import AppSignals
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeCraftResultMagicWithObjectDescMessage import (
    ExchangeCraftResultMagicWithObjectDescMessage,
)
from app.types_.enums import MagicPoolStatus
from app.types_.models.common import BotInfo, ParsedMessageHandler

logger = logging.getLogger(__name__)


class ExchangeCraftResultMagicWithObjectDescMessageHandler(
    ParsedMessageHandler, ExchangeCraftResultMagicWithObjectDescMessage
):
    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        if (fm := bot_info.fm_info.fm) is not None:
            fm.get_remainder(
                self.objectInfo.effects, MagicPoolStatus(self.magicPoolStatus)
            )
            logger.info(f"Got result fm, remainder : {fm.remainder}")
            fm.selected_rune = None
            fm.current_item = self.objectInfo
            if bot_info.fm_info.is_playing_event.is_set():
                fm.process()
        else:
            raise ValueError("fm instance should not be None")
