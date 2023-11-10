import json
import os
import shutil
from pathlib import Path

from tqdm import tqdm
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from network.utils import get_classes_in_path


def convert_byte_type_python(byte_type: str):
    match byte_type:
        case "UTF":
            return "str"
        case "Boolean":
            return "bool"
        case "Float" | "Double":
            return "float"
        case (
            "Byte"
            | "Int"
            | "Short"
            | "VarUhShort"
            | "VarUhLong"
            | "VarUhInt"
            | "UnsignedByte"
            | "UnsignedInt"
            | "UnsignedShort"
            | "VarInt"
            | "VarShort"
            | "VarLong"
            | "Uuid"
        ):
            return "int"
        case "ByteArray":
            return "int"

    return False


def find_import_path_by_class_name(
    class_name: str, protocol_json: dict, base_path_imports: str
) -> str:
    class_data = protocol_json.get(class_name)
    if class_data is not None:
        folder_path = (
            os.path.join(
                base_path_imports, class_data.get("path").split("code_source\\")[1][:-3]
            )
            .replace("\\", ".")
            .replace("_global", "global")
        )
        return f"from {folder_path} import {class_name}\n"
    raise Exception


def create_python_class_dofus_file(base_path_output):
    BASE_PATH_IMPORTS = os.path.relpath(
        os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "types_",
            "dofus",
        )
    )
    PROTOCOL_JSON_PATH = os.path.join(
        Path(__file__).parent.parent, "network", "protocol", "protocol_type.json"
    )

    shutil.rmtree(
        base_path_output,
        ignore_errors=True,
    )

    with open(PROTOCOL_JSON_PATH) as protocol_json_file:
        protocol_json = json.load(protocol_json_file)
        for class_name, class_data in tqdm(protocol_json.items()):
            parent: str = class_data.get("parent")

            import_lines = "from __future__ import annotations\n"
            import_lines += "from typing import TYPE_CHECKING\n"

            import_class_line = "if TYPE_CHECKING:\n"

            class_line = f"class {class_name}"
            if parent is not None:
                class_line += f"({parent})"
            class_line += ":\n"

            init_method_name = "\tdef __init__(self"
            init_method_name_optional = ""
            init_vars_init = ""

            if parent is not None:
                import_lines += find_import_path_by_class_name(
                    parent, protocol_json, BASE_PATH_IMPORTS
                )
                init_vars_init += f"\n\t\tsuper().__init__(*args)"

            consistent_vars = [
                _var for _var in class_data["vars"] if _var.get("type") is not False
            ]
            if len(consistent_vars) > 0:
                for _var in consistent_vars:
                    python_type = convert_byte_type_python(_var.get("type"))
                    if not python_type:
                        import_class_name = find_import_path_by_class_name(
                            _var.get("type"), protocol_json, BASE_PATH_IMPORTS
                        )

                        import_class_line += "\t" + import_class_name

                        python_type = _var.get("type")

                    if _var.get("optional") is True:
                        python_type += "|None=None "
                        if _var.get("length") is not None:
                            init_method_name_optional += (
                                f", {_var.get('name')}:list[{python_type}]"
                            )
                        else:
                            init_method_name_optional += (
                                f", {_var.get('name')}:{python_type}"
                            )
                    else:
                        if _var.get("length") is not None:
                            init_method_name += (
                                f", {_var.get('name')}:list[{python_type}]"
                            )
                        else:
                            init_method_name += f", {_var.get('name')}:{python_type}"
                    init_vars_init += (
                        f"\n\t\tself.{_var.get('name')}={_var.get('name')}"
                    )
            else:
                init_vars_init += "\n\t\t..."

            if not "\t" in import_class_line:
                import_class_line += "\t...\n"

            if parent is not None:
                init_method_name += f", *args"
            init_method_name_optional += "):"

            python_code = (
                import_lines
                + import_class_line
                + class_line
                + init_method_name
                + init_method_name_optional
                + init_vars_init
            )

            class_path = os.path.dirname(
                os.path.join(
                    base_path_output,
                    class_data.get("path").split("code_source\\")[1],
                )
            ).replace("global", "_global")
            os.makedirs(class_path, exist_ok=True)
            with open(
                os.path.join(class_path, class_name + ".py"),
                "w",
            ) as python_file:
                python_file.write(python_code)


def create_utils_file(base_path_output):
    utils_import = ""
    utils_code = "CLASSES_BY_NAME = {\n"

    classes = get_classes_in_path(
        os.path.join(Path(__file__).parent.parent, "types_", "dofus"), ".py"
    )
    for _class in classes:
        utils_import += f"from {_class.__module__} import {_class.__name__}\n"
        utils_code += f"\t'{_class.__name__}': {_class.__name__},\n"

    with open(os.path.join(base_path_output, "utils.py"), "w") as utils_file:
        utils_file.write(utils_import + utils_code + "}")


def launch_generator():
    BASE_PATH_OUTPUT = os.path.join(Path(__file__).parent.parent, "types_", "dofus")
    create_python_class_dofus_file(BASE_PATH_OUTPUT)
    create_utils_file(BASE_PATH_OUTPUT)


if __name__ == "__main__":
    launch_generator()
