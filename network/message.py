from dataclasses import dataclass
import logging
from multiprocessing import Event
from queue import Queue

import eel

from databases.database import Database
from models.data import Data

logger = logging.getLogger(__name__)

@dataclass
class Message:
    message_id: int = None
    data: Data = None

    def event(self, database: Database, queue_actual_item: Queue, event_is_playing: Event) -> None:
        if self.message_id == int(database.select_protocol_id_by_message_name(
                "ExchangeCraftResultMagicWithObjectDescMessage")) and event_is_playing.is_set():
            actual_item = []
            self.data.readByte()
            self.data.readVarUhShort()
            effects_len = self.data.readUnsignedShort()
            for _ in range(effects_len):
                self.data.readUnsignedShort()
                actual_item.append(
                    {"rune_name": database.select_rune_name_by_rune_id(self.data.readVarUhShort()),
                     "value": self.data.readVarUhShort()})
            queue_actual_item.put(actual_item)

        elif self.message_id == int(
                database.select_protocol_id_by_message_name("ExchangeObjectAddedMessage"))and not event_is_playing.is_set():
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
                        {"type": database.select_rune_name_by_rune_id(self.data.readVarUhShort()),
                         "value": self.data.readVarUhShort()})

            eel.on_inserted_item(inserted_item)