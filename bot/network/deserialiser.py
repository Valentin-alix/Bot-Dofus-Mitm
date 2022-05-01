from bot.databases.database import Database
from bot.factory import action
from bot.factory.action import Action
from bot.gui import interface
from bot.models.message import Message

ExchangeObjectAddedMessage: int = Database().select_id_by_message("ExchangeObjectAddedMessage")
ExchangeCraftResultMagicWithObjectDescMessage: int = Database().select_id_by_message(
    "ExchangeCraftResultMagicWithObjectDescMessage")


def interpretation(message: Message) -> None:
    if message.message_id == int(
            ExchangeCraftResultMagicWithObjectDescMessage) and action.bot_fm_is_playing:

        action.actual_item.__init__()
        # Ci dessous craft result
        message.data.readByte()
        # Ci dessous object GID
        message.data.readVarUhShort()
        effects_len = message.data.readUnsignedShort()

        for _ in range(effects_len):
            message.data.readUnsignedShort()
            action_id = message.data.readVarUhShort()
            value = message.data.readVarUhShort()
            action.actual_item.runes.append(
                {"type": Database().select_type_rune_by_id(action_id), "value": value})

        Action().click_based_on_values()

    elif message.message_id == ExchangeObjectAddedMessage and not action.bot_fm_is_playing:
        interface.inserted_item.__init__()
        # Ci-dessous remote
        message.data.readBoolean()
        # Ci-dessous position
        message.data.readShort()
        # Ci-dessous object_gid
        message.data.readVarUhShort()

        effects_len = message.data.readUnsignedShort()
        # Si l'élément n'est pas une rune alors ->
        if effects_len > 1:
            for _ in range(effects_len):
                message.data.readUnsignedShort()
                action_id = message.data.readVarUhShort()
                value = message.data.readVarUhShort()
                interface.inserted_item.runes.append(
                    {"type": Database().select_type_rune_by_id(action_id), "value": value})

            interface.interface.clear_frame(interface.interface.root)
            interface.interface.ajout_item_page()

    elif message.message_id == Database().select_id_by_message(
            "ExchangeTypesItemsExchangerDescriptionForUserMessage") and action.bot_hdv_is_playing:
        prices: list = []
        action_id: int = 0
        object_gid = message.data.readVarUhInt()
        object_type = message.data.readInt()
        item_type_description_len = message.data.readUnsignedShort()
        for _ in range(item_type_description_len):
            message.data.readVarUhInt()
            message.data.readVarUhInt()
            message.data.readInt()
            effects_len: int = message.data.readUnsignedShort()
            for _ in range(effects_len):
                message.data.readUnsignedShort()
                action_id = message.data.readVarUhShort()
                message.data.readVarUhShort()

            prices_len: int = message.data.readUnsignedShort()

            [prices.append(message.data.readVarUhLong()) for _ in range(prices_len)]
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
        if not Database().select_name_by_item_id(object_gid):
            return
        Database().update_average_price_by_name(type_rune, average_price)
        Database().update_average_price_by_name(f"-{type_rune}", average_price)
