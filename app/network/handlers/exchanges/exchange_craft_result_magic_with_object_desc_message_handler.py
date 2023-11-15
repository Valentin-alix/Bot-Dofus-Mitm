import logging

from app.types_ import ParsedMessageHandler, BotInfo, MagicPoolStatus
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeCraftResultMagicWithObjectDescMessage import (
    ExchangeCraftResultMagicWithObjectDescMessage,
)

logger = logging.getLogger(__name__)


class ExchangeCraftResultMagicWithObjectDescMessageHandler(
    ParsedMessageHandler, ExchangeCraftResultMagicWithObjectDescMessage
):
    def handle(self, bot_info: BotInfo) -> None:
        with bot_info.fm_info.fm_with_lock["lock"]:
            if (fm := bot_info.fm_info.fm_with_lock["fm"]) is not None:
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
