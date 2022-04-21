from databases.database_management import DatabaseManagement
from factory import action
from gui import interface
from models.data import Data


ExchangeObjectAddedMessage: int = DatabaseManagement().select_needed_message_network()[1][0]
ExchangeCraftResultMagicWithObjectDescMessage: int = DatabaseManagement().select_needed_message_network()[0][0]


def interpretation(data_object: Data):
    if int(id_packet_getter(data_object)) == int(
            ExchangeCraftResultMagicWithObjectDescMessage) and action.bot_is_playing:
        data_object.readUnsignedShort()
        data_object.readByte()
        # Ci dessous craft result
        data_object.readByte()
        # Ci dessous object GID
        data_object.readVarUhShort()
        effects_len = data_object.readUnsignedShort()

        actions_id: list[int] = []
        values: list[int] = []

        for i in range(effects_len):
            data_object.readUnsignedShort()
            action_id = data_object.readVarUhShort()
            value = data_object.readVarUhShort()
            actions_id.append(action_id)
            values.append(value)

        data_object.readUnsignedShort()
        data_object.readByte()
        # Ci-Dessous Object UID
        data_object.readVarUhInt()
        # Ci-Dessous Object quantity
        data_object.readVarUhInt()
        # Ci-Dessous Object magic_pool_status
        data_object.readByte()

        action.item.actual_id_values = actions_id

        action.item.actual_values = values

        action.click_based_on_values()

    elif id_packet_getter(data_object) == ExchangeObjectAddedMessage and not action.bot_is_playing:
        header = data_object.readUnsignedShort()
        header += data_object.readByte()

        # Ci-dessous remote
        data_object.readBoolean()
        # Ci-dessous position
        data_object.readShort()
        # Ci-dessous object_gid
        data_object.readVarUhShort()
        effects_len = data_object.readUnsignedShort()
        actions_id: list[int] = []
        values: list[int] = []

        for i in range(effects_len):
            data_object.readUnsignedShort()
            action_id = data_object.readVarUhShort()
            value = data_object.readVarUhShort()
            actions_id.append(action_id)
            values.append(value)
        # Ci-dessous object_uid
        data_object.readVarUhInt()
        # Ci-dessous quantity
        data_object.readVarUhInt()

        # Si l'élément n'est pas une rune alors ->
        if effects_len > 1:
            interface.inserted_item.id_runes = actions_id
            interface.inserted_item.value_runes = values

            interface.interface.clear_frame(interface.interface.root)
            interface.interface.ajout_item_window()


def id_packet_getter(data_receive) -> int:
    if not isinstance(data_receive, Data):
        data_receive = Data(bytearray.fromhex(data_receive[:4]))
    header = data_receive.readUnsignedShort()
    id_value = header >> 2
    data_receive.reset_pos()
    return id_value
