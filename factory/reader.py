from gui import interface
from models.data import Data


class Reader:
    @staticmethod
    def interpretation(data_object: Data):
        if Reader.recuperation_id(data_object) == 6242:
            data_object.readUnsignedShort()
            data_object.readByte()
            craft_result = data_object.readByte()
            object_gid = data_object.readVarUhShort()
            effects_len = data_object.readUnsignedShort()
            item = []
            for i in range(effects_len):
                temp_id = data_object.readUnsignedShort()
                action_id = data_object.readVarUhShort()
                value = data_object.readVarUhShort()
                item.append([action_id, value])

            data_object.readUnsignedShort()
            data_object.readByte()
            object_uid = data_object.readVarUhInt()
            quantity = data_object.readVarUhInt()
            magic_pool_status = data_object.readByte()
            print("un coupe de rune")

        elif Reader.recuperation_id(data_object) == 2329:

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
            print("insertion item")
            interface.inserted_item = [actions_id, values]
            interface.interface.clear_frame(interface.interface.root)
            interface.interface.ajout_item_window()
            # FIXME CODE QUI MET A JOUR INTERFACE

    @staticmethod
    def recuperation_id(data_receive):
        if not isinstance(data_receive, Data):
            data_receive = Data(bytearray.fromhex(data_receive[:4]))
        header = data_receive.readUnsignedShort()
        id_value = header >> 2
        data_receive.reset_pos()
        return id_value
