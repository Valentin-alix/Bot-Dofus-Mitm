from databases.database import Database
from factory import action
from factory.action import Action
from gui import interface
from models.message import Message

ExchangeObjectAddedMessage: int = Database().select_id_by_message("ExchangeObjectAddedMessage")
ExchangeCraftResultMagicWithObjectDescMessage: int = Database().select_id_by_message(
    "ExchangeCraftResultMagicWithObjectDescMessage")


def interpretation(message: Message) -> None:
    if message.message_id == int(
            ExchangeCraftResultMagicWithObjectDescMessage) and action.bot_is_playing:

        action.actual_item.__init__()
        # Ci dessous craft result
        message.data.readByte()
        # Ci dessous object GID
        message.data.readVarUhShort()
        effects_len = message.data.readUnsignedShort()

        for i in range(effects_len):
            message.data.readUnsignedShort()
            action_id = message.data.readVarUhShort()
            value = message.data.readVarUhShort()
            action.actual_item.runes.append(
                {"type": Database().select_type_rune_by_id(action_id), "value": value})

        Action().click_based_on_values()

    elif message.message_id == ExchangeObjectAddedMessage and not action.bot_is_playing:
        # Ci-dessous remote
        message.data.readBoolean()
        # Ci-dessous position
        message.data.readShort()
        # Ci-dessous object_gid
        message.data.readVarUhShort()

        effects_len = message.data.readUnsignedShort()

        for i in range(effects_len):
            message.data.readUnsignedShort()
            action_id = message.data.readVarUhShort()
            value = message.data.readVarUhShort()
            interface.inserted_item_test.runes.append(
                {"type": Database().select_type_rune_by_id(action_id), "value": value})

        # Si l'élément n'est pas une rune alors ->
        if effects_len > 1:
            interface.interface.clear_frame(interface.interface.root)
            interface.interface.ajout_item_window()
