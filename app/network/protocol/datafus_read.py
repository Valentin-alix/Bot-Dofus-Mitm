import json
import os
import re
from pathlib import Path

from app.types_.models.network.data import Data

primitives = [
    'VarInt'
    , 'VarUhInt'
    , 'VarShort'
    , 'VarUhShort'
    , 'VarLong'
    , 'VarUhLong'
    , 'Bytes'
    , 'Boolean'
    , 'Byte'
    , 'UnsignedByte'
    , 'Short'
    , 'UnsignedShort'
    , 'Int'
    , 'UnsignedInt'
    , 'Float'
    , 'Double'
    , 'MultiByte'
    , 'UTF'
    , 'UTFBytes'
]

TYPE_ID_PATTERN = r'TypeId<([^<>]+)>'
TYPE_ID_VECTOR_PATTERN = r"TypeIdVector<(?P<type>\w+),(?P<value>\w+)>"
VECTOR_PATTERN = r"Vector<(?P<type>\w+),(?P<value>\w+)>"


def json_from_msg(protocol_datas: dict, _type: dict | str, json_values, data: Data):
    if isinstance(_type, dict):
        json_values = {}
        print(_type['class_name'])
        if _type['superclass'] is not None and _type['superclass'] != "NetworkMessage":
            # unpacking parent
            parent = next(msg for msg in protocol_datas if msg["class_name"] == _type['superclass'])
            json_from_msg(protocol_datas, parent, json_values, data)

        _vars = _type['attributes']
        if (bol_vars_len := len([key for key, value in _vars.items() if value == "Boolean"])) >= 2:
            # unpacking booleanWrapper
            for _ in range(0, bol_vars_len, 8):
                data.readByte()
                # todo put value boolean
            _vars = {key: value for key, value in _vars.items() if value != "Boolean"}

        for key, value in _vars.items():
            json_values[key] = json_from_msg(protocol_datas, value, {}, data)
            print(json_values)
        return json_values

    if _type in primitives:
        return getattr(Data, f"read{_type}")(data)
    if _type == "String":
        return data.readUTF()
    if (class_type := next((msg for msg in protocol_datas if _type == msg['class_name']), None)) is not None:
        return json_from_msg(protocol_datas, class_type, json_values, data)

    match_type_id_vector = re.match(TYPE_ID_VECTOR_PATTERN, _type)
    if match_type_id_vector:
        # TODO Test this
        _len = getattr(Data, f"read{match_type_id_vector.group('type')}")(data)  # pb len parfois -1 ?
        print(f"len type id vector : {_len}")
        values = []
        for _ in range(_len):
            _id = data.readUnsignedShort()
            values.append(json_from_msg(protocol_datas, match_type_id_vector.group('value'), {}, data))
        return values

    match_type_id = re.match(TYPE_ID_PATTERN, _type)
    if match_type_id:
        _id = data.readUnsignedShort()
        return json_from_msg(protocol_datas, match_type_id.group(1), {}, data)

    match_vector = re.match(VECTOR_PATTERN, _type)
    if match_vector:
        _len = getattr(Data, f"read{match_vector.group('type')}")(data)
        return [json_from_msg(protocol_datas, match_vector.group('value'), {}, data) for _ in range(_len)]

    raise ValueError(f"Unknown type: {_type}")


def get_json_from_message(class_name: str, data: Data):
    with open(os.path.join(Path(__file__).parent, "datafus_test.json"), "r") as file:
        protocol_data = json.load(file)
        json_values = {}
        msg = next(msg for msg in protocol_data if msg["class_name"] == class_name)
        print(json_from_msg(protocol_data, msg, json_values, data))


if __name__ == "__main__":
    ...
    # get_json_from_message("ActivitySuggestionsRequestMessage", Data())
