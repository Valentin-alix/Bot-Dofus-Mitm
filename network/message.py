import datetime
from asyncio import Queue, Event
from dataclasses import dataclass

from bot.bot_hdv import BotHDV
from databases.database import Database
from models.data import Data
from models.item import Item


@dataclass
class Message:
    message_id: int = None
    data: Data = None

    async def event(self, queue_actual_item: Queue, queue_inserted_item: Queue, event_is_playing: Event,
                    database: Database) -> None:
        if self.message_id == int(database.select_id_by_message(
                "ExchangeCraftResultMagicWithObjectDescMessage")) and event_is_playing.is_set():
            actual_item: Item = Item()
            # action.actual_item.__init__()
            # Ci dessous craft result
            self.data.readByte()
            # Ci dessous object GID
            self.data.readVarUhShort()
            effects_len = self.data.readUnsignedShort()

            for _ in range(effects_len):
                self.data.readUnsignedShort()
                actual_item.runes.append(
                    {"type": database.select_type_rune_by_id(self.data.readVarUhShort()), "value": self.data.readVarUhShort()})

            await queue_actual_item.put(actual_item)

        elif self.message_id == int(
                database.select_id_by_message("ExchangeObjectAddedMessage")) and not event_is_playing.is_set():
            inserted_item: Item = Item()
            # Ci-dessous remote
            self.data.readBoolean()
            # Ci-dessous position
            self.data.readShort()
            # Ci-dessous object_gid
            self.data.readVarUhShort()

            effects_len = self.data.readUnsignedShort()
            # Si l'élément n'est pas une rune alors ->
            if effects_len > 1:
                for _ in range(effects_len):
                    self.data.readUnsignedShort()
                    inserted_item.runes.append(
                        {"type": database.select_type_rune_by_id(self.data.readVarUhShort()), "value": self.data.readVarUhShort()})

                await queue_inserted_item.put(inserted_item)

        elif self.message_id == Database().select_id_by_message(
                "ExchangeTypesItemsExchangerDescriptionForUserMessage"):
            prices: list = []
            action_id: int = 0
            object_gid = self.data.readVarUhInt()
            self.data.readInt()
            item_type_description_len = self.data.readUnsignedShort()
            for _ in range(item_type_description_len):
                self.data.readVarUhInt()
                self.data.readVarUhInt()
                self.data.readInt()
                effects_len: int = self.data.readUnsignedShort()
                for _ in range(effects_len):
                    self.data.readUnsignedShort()
                    action_id = self.data.readVarUhShort()
                    self.data.readVarUhShort()

                prices_len: int = self.data.readUnsignedShort()

                [prices.append(self.data.readVarUhLong()) for _ in range(prices_len)]
            try:
                type_rune: str = database.select_type_rune_by_id(action_id)
            except TypeError:
                return
            if prices[2]:
                average_price: int = prices[2] / 100
            elif prices[1]:
                average_price: int = prices[1] / 10
            elif prices[0]:
                average_price: int = prices[0]
            else:
                return
            if database.select_name_by_item_id(object_gid):
                BotHDV.maj_csv_value(datetime.date.today(), type_rune, average_price)
            database.update_average_price_by_name(type_rune, average_price)
            database.update_average_price_by_name(f"-{type_rune}", average_price)
