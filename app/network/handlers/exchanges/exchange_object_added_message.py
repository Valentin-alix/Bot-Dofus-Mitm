from sqlalchemy.orm import sessionmaker

from app.database.models import Item, get_engine, TypeItem, CategoryEnum
from app.types_ import ParsedMessageHandler, BotInfo
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectAddedMessage import \
    ExchangeObjectAddedMessage


class ExchangeObjectAddedMessageHandler(ParsedMessageHandler, ExchangeObjectAddedMessage):
    def handle(self, bot_info: BotInfo) -> None:
        with bot_info.fm_info.fm_with_lock["lock"]:
            if (fm := bot_info.fm_info.fm_with_lock["fm"]) is not None:
                engine = get_engine()
                session = sessionmaker(engine=engine)()
                item_with_category = session.query(Item.id, TypeItem.name, TypeItem.category).join(TypeItem,
                                                                                                   TypeItem.id == Item.type_item_id).filter(
                    Item.id == self.object.objectGID).scalar()
                if item_with_category[1] == "Rune de forgemagie":
                    ...
                elif item_with_category[2] == CategoryEnum.EQUIPMENT:
                    fm.current_item = self.object
