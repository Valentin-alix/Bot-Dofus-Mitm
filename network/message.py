from dataclasses import dataclass
import datetime
import logging
from multiprocessing import Event
from queue import Queue

import eel
from bot.bot_hdv import BotHDV
from databases.database import *

from models.data import Data

logger = logging.getLogger(__name__)

@dataclass
class Message:
    message_id: int = None
    data: Data = None

    def event(self, queue_actual_item: Queue, event_is_playing: Event) -> None:
        if self.message_id == int(select_protocol_id_by_message_name(
                "ExchangeCraftResultMagicWithObjectDescMessage")) and event_is_playing.is_set():
            actual_item = []
            self.data.readByte()
            self.data.readVarUhShort()
            effects_len = self.data.readUnsignedShort()
            for _ in range(effects_len):
                self.data.readUnsignedShort()
                actual_item.append(
                    {"rune_name": select_rune_name_by_rune_id(self.data.readVarUhShort()),
                     "value": self.data.readVarUhShort()})
            queue_actual_item.put(actual_item)

        elif self.message_id == int(
                select_protocol_id_by_message_name("ExchangeObjectAddedMessage"))and not event_is_playing.is_set():
            inserted_item = []
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
                    inserted_item.append(
                        {"type": select_rune_name_by_rune_id(self.data.readVarUhShort()),
                         "value": self.data.readVarUhShort()})

            eel.on_inserted_item(inserted_item)
        elif self.message_id == int(select_protocol_id_by_message_name(
                "ExchangeTypesItemsExchangerDescriptionForUserMessage")):
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
                type_rune: str = select_rune_name_by_rune_id(action_id)
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
            
            if select_name_by_object_id(object_gid):
                BotHDV.maj_csv_value(datetime.date.today(), type_rune, average_price)
                update_average_price_by_name(type_rune, average_price)
                update_average_price_by_name(f"-{type_rune}", average_price)
