from __future__ import annotations

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from app.types_.dofus.utils import CLASSES_BY_NAME


def deep_dict_to_object(from_client: bool | None = None, **kwargs):
    props = kwargs
    for key, value in kwargs.items():
        if isinstance(value, dict):
            value = deep_dict_to_object(**value)
            props[key] = value
        elif isinstance(value, list):
            value = [deep_dict_to_object(**_value) for _value in value]
            props[key] = value
    if kwargs.get('__type__') is not None:
        class_type = CLASSES_BY_NAME.get(kwargs.pop('__type__'))
        if class_type is not None:
            return class_type(**props)
    return props


if __name__ == "__main__":
    object_dict = {'from_client': False, '__type__': 'InventoryContentMessage', 'objects': [
        {'__type__': 'ObjectItem', 'position': 3, 'objectGID': 18006,
         'effects': [{'__type__': 'ObjectEffectInteger', 'actionId': 125, 'value': 342},
                     {'__type__': 'ObjectEffectInteger', 'actionId': 123, 'value': 57},
                     {'__type__': 'ObjectEffectInteger', 'actionId': 124, 'value': 35},
                     {'__type__': 'ObjectEffectInteger', 'actionId': 176, 'value': 15},
                     {'__type__': 'ObjectEffectInteger', 'actionId': 160, 'value': 15},
                     {'__type__': 'ObjectEffectInteger', 'actionId': 426, 'value': 14},
                     {'__type__': 'ObjectEffectInteger', 'actionId': 213, 'value': 7},
                     {'__type__': 'ObjectEffectInteger', 'actionId': 214, 'value': 6},
                     {'__type__': 'ObjectEffectInteger', 'actionId': 115, 'value': 2},
                     {'__type__': 'ObjectEffectInteger', 'actionId': 111, 'value': 1}], 'objectUID': 107743439,
         'quantity': 1}]}
    testeu = deep_dict_to_object(**object_dict)
    print(testeu.objects[0].position)
