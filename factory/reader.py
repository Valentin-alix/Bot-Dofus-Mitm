from factory import action
from gui import interface
from models.data import Data
from models.item import Item

item_played: Item()


def interpretation(data_object: Data):
    if id_packet_getter(data_object) == 6242:
        data_object.readUnsignedShort()
        data_object.readByte()
        craft_result = data_object.readByte()
        object_gid = data_object.readVarUhShort()
        effects_len = data_object.readUnsignedShort()

        actions_id = []
        values = []

        for i in range(effects_len):
            temp_id = data_object.readUnsignedShort()
            action_id = data_object.readVarUhShort()
            value = data_object.readVarUhShort()
            actions_id.append(action_id)
            values.append(value)

        data_object.readUnsignedShort()
        data_object.readByte()
        object_uid = data_object.readVarUhInt()
        quantity = data_object.readVarUhInt()
        magic_pool_status = data_object.readByte()

        item_played.id_runes = actions_id
        item_played.inserted_item.value_runes = values

        action.click_based_on_values()

    elif id_packet_getter(data_object) == 2329:

        header = data_object.readUnsignedShort()
        header += data_object.readByte()

        remote = data_object.readBoolean()
        position = data_object.readShort()
        object_gid = data_object.readVarUhShort()
        effects_len = data_object.readUnsignedShort()
        actions_id = []
        values = []

        for i in range(effects_len):
            temp_id = data_object.readUnsignedShort()
            action_id = data_object.readVarUhShort()
            value = data_object.readVarUhShort()
            actions_id.append(action_id)
            values.append(value)
        object_uid = data_object.readVarUhInt()
        quantity = data_object.readVarUhInt()

        interface.inserted_item.id_runes = actions_id
        interface.inserted_item.value_runes = values

        interface.interface.clear_frame(interface.interface.root)
        interface.interface.ajout_item_window()


def id_packet_getter(data_receive):
    if not isinstance(data_receive, Data):
        data_receive = Data(bytearray.fromhex(data_receive[:4]))
    header = data_receive.readUnsignedShort()
    id_value = header >> 2
    data_receive.reset_pos()
    return id_value
