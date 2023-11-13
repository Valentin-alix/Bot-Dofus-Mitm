from app.types_ import ParsedMessageHandler, BotInfo
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeCraftResultMagicWithObjectDescMessage import \
    ExchangeCraftResultMagicWithObjectDescMessage


class ExchangeCraftResultMagicWithObjectDescMessageHandler(ParsedMessageHandler,
                                                           ExchangeCraftResultMagicWithObjectDescMessage):
    def handle(self, bot_info: BotInfo) -> None:
        with bot_info.fm_info.fm_with_lock["lock"]:
            if (fm := bot_info.fm_info.fm_with_lock["fm"]) is not None:
                fm.current_item = self.objectInfo
            else:
                raise ValueError("fm instance should not be None")
