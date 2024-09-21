import os
from importlib import import_module

try:
    from app.interfaces.dofus.utils import CLASSES_BY_NAME
except ModuleNotFoundError:
    CLASSES_BY_NAME = {}


def convert_snake_case_to_camel_case(snake_case_str: str):
    camel_case_str = ""
    for word in snake_case_str.split("_"):
        camel_case_str += word[0].upper() + word[1:]
    return camel_case_str


def deep_dict_to_object(**kwargs):
    props = kwargs
    for key, value in kwargs.items():
        if isinstance(value, dict):
            value = deep_dict_to_object(**value)
            props[key] = value
        elif isinstance(value, list) and len(value) > 0 and isinstance(value[0], dict):
            value = [deep_dict_to_object(**_value) for _value in value]
            props[key] = value
    if (
        kwargs.get("__type__") is not None
        and (class_type := CLASSES_BY_NAME.get(kwargs.pop("__type__"))) is not None
    ):
        return class_type(**props)
    raise ValueError("object must contains valid __type__ key")


def get_classes_in_path(path, condition_end_file: str) -> list:
    class_handlers = []
    for folder, sub_folder, files in os.walk(path):
        app_folder_position = str(folder).find("app")
        folder = folder[app_folder_position:].replace("\\", ".")

        for file in files:
            if file.endswith(condition_end_file) and not file.startswith("__init__"):
                file_path = f"{folder}.{file[:-3]}"
                mod = import_module(file_path)
                class_handlers.append(
                    getattr(mod, f"{convert_snake_case_to_camel_case(file[:-3])}")
                )
    return class_handlers
