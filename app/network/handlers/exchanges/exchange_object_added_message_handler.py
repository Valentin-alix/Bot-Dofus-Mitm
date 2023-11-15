import logging

from sqlalchemy.orm import sessionmaker

from app.database.models import Item, get_engine, TypeItem, CategoryEnum
from app.modules.fm import Fm
from app.types_ import ParsedMessageHandler, BotInfo
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectAddedMessage import (
    ExchangeObjectAddedMessage,
)

logger = logging.getLogger(__name__)


class ExchangeObjectAddedMessageHandler(
    ParsedMessageHandler, ExchangeObjectAddedMessage
):
    def handle(self, bot_info: BotInfo) -> None:
        with bot_info.fm_info.fm_with_lock["lock"]:
            engine = get_engine()
            session = sessionmaker(bind=engine)()

            item_with_category = (
                session.query(Item.id, TypeItem.name, TypeItem.category)
                .join(TypeItem, TypeItem.id == Item.type_item_id)
                .filter(Item.id == self.object.objectGID)
                .first()
            )
            if item_with_category[1] == "Rune de forgemagie":
                logger.info(
                    f"Got rune selected with actionId : {self.object.effects[0].actionId}"
                )
                if (fm := bot_info.fm_info.fm_with_lock["fm"]) is None:
                    raise ValueError("fm instance should not be none")
                fm.selected_rune = self.object
                if bot_info.fm_info.is_playing_event.is_set():
                    fm.merge_rune()

            elif item_with_category[2] == CategoryEnum.EQUIPMENT:
                logger.info(
                    f"Got equipement selected with gid : {self.object.objectGID}"
                )
                bot_info.fm_info.fm_with_lock["fm"] = Fm(current_item=self.object)
                if bot_info.fm_info.is_playing_event.is_set():
                    bot_info.fm_info.fm_with_lock["fm"].process()
