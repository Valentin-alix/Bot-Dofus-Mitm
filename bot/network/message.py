import datetime
import threading
from dataclasses import dataclass

from bot.databases.database import Database
from bot.factory import action, hdv_graphic
from bot.gui import ui
from bot.models.data import Data


@dataclass
class Message:
    message_id: int = None
    data: Data = None

    def event(self) -> None:
        if self.message_id == int(Database().select_id_by_message(
                "ExchangeCraftResultMagicWithObjectDescMessage")) and action.bot_fm_is_playing:
            action.actual_item.__init__()
            # Ci dessous craft result
            self.data.readByte()
            # Ci dessous object GID
            self.data.readVarUhShort()
            effects_len = self.data.readUnsignedShort()

            for _ in range(effects_len):
                self.data.readUnsignedShort()
                action_id = self.data.readVarUhShort()
                value = self.data.readVarUhShort()
                action.actual_item.runes.append(
                    {"type": Database().select_type_rune_by_id(action_id), "value": value})

            click_thread = threading.Thread(target=action.click_fm)
            click_thread.start()

        elif self.message_id == int(
                Database().select_id_by_message("ExchangeObjectAddedMessage")) and not action.bot_fm_is_playing:
            ui.inserted_item.__init__()
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
                    action_id = self.data.readVarUhShort()
                    value = self.data.readVarUhShort()
                    ui.inserted_item.runes.append(
                        {"type": Database().select_type_rune_by_id(action_id), "value": value})

                ui.interface.clear_frame(ui.interface)
                ui.interface.ajout_item_page()

        elif self.message_id == Database().select_id_by_message(
                "ExchangeTypesItemsExchangerDescriptionForUserMessage") and action.bot_hdv_is_playing:
            action.waiting_click = False
            prices: list = []
            action_id: int = 0
            object_gid = self.data.readVarUhInt()
            object_type = self.data.readInt()
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
                type_rune: str = Database().select_type_rune_by_id(action_id)
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
            if not Database().select_name_by_item_id(object_gid) or graphic.check_if_same_day(type_rune):
                return
            graphic.maj_csv_value(datetime.date.today(), type_rune, average_price)
            Database().update_average_price_by_name(type_rune, average_price)
            Database().update_average_price_by_name(f"-{type_rune}", average_price)
