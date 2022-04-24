from databases.database_management import DatabaseManagement
from factory import action
from factory.action import Action
from gui import interface
from models.message import Message

ExchangeObjectAddedMessage: int = DatabaseManagement().select_id_by_message("ExchangeObjectAddedMessage")
ExchangeCraftResultMagicWithObjectDescMessage: int = DatabaseManagement().select_id_by_message(
    "ExchangeCraftResultMagicWithObjectDescMessage")


def interpretation(message: Message):
    # HelloConnectMessage
    if message.message_id == DatabaseManagement().select_id_by_message("HelloConnectMessage"):
        salt = message.data.readUTF()
        key_len = message.data.readVarInt()
        vals = []
        for i in range(key_len):
            vals.append(message.data.readByte())

        print(f"salt : {salt} key_len : {key_len} vals : {vals}")

    if message.message_id == int(
            ExchangeCraftResultMagicWithObjectDescMessage) and action.BOT_IS_PLAYING:
        # Ci dessous craft result
        message.data.readByte()
        # Ci dessous object GID
        message.data.readVarUhShort()
        effects_len = message.data.readUnsignedShort()

        actions_id: list[int] = []
        values: list[int] = []

        for i in range(effects_len):
            message.data.readUnsignedShort()
            action_id = message.data.readVarUhShort()
            value = message.data.readVarUhShort()
            actions_id.append(action_id)
            values.append(value)

        message.data.readUnsignedShort()
        message.data.readByte()
        # Ci-Dessous Object UID
        message.data.readVarUhInt()
        # Ci-Dessous Object quantity
        message.data.readVarUhInt()
        # Ci-Dessous Object magic_pool_status
        message.data.readByte()

        action.ITEM.actual_id_values = actions_id

        action.ITEM.actual_values = values

        Action().click_based_on_values()

    elif message.message_id == ExchangeObjectAddedMessage and not action.BOT_IS_PLAYING:
        # Ci-dessous remote
        message.data.readBoolean()
        # Ci-dessous position
        message.data.readShort()
        # Ci-dessous object_gid
        message.data.readVarUhShort()
        effects_len = message.data.readUnsignedShort()
        actions_id: list[int] = []
        values: list[int] = []

        for i in range(effects_len):
            message.data.readUnsignedShort()
            action_id = message.data.readVarUhShort()
            value = message.data.readVarUhShort()
            actions_id.append(action_id)
            values.append(value)
        # Ci-dessous object_uid
        message.data.readVarUhInt()
        # Ci-dessous quantity
        message.data.readVarUhInt()

        # Si l'élément n'est pas une rune alors ->
        if effects_len > 1:
            interface.inserted_item.id_runes = actions_id
            interface.inserted_item.value_runes = values

            interface.interface.clear_frame(interface.interface.root)
            interface.interface.ajout_item_window()
