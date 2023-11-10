import json
import os
from pathlib import Path

from tqdm import tqdm


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


def find_import_path_by_class_name(class_name: str, protocol_json: dict):
    class_data = protocol_json.get(class_name)
    if class_data is not None:
        folder_path = os.path.join(
            class_data.get("path").split("code_source\\")[1][:-3]
        ).replace("\\", ".")
        return f"from {folder_path} import {class_name}\n"
    raise Exception


if __name__ == "__main__":
    protocol_json_path = os.path.join(
        Path(__file__).parent.parent, "network", "protocol", "protocol_type.json"
    )
    with open(protocol_json_path) as protocol_json_file:
        protocol_json = json.load(protocol_json_file)
        for class_name, class_data in tqdm(protocol_json.items()):
            parent = class_data.get("parent")

            import_lines = (
                find_import_path_by_class_name(parent, protocol_json)
                if parent is not None
                else ""
            )

            class_line = f"class {class_name}"
            if parent is not None:
                class_line += f"({parent})"
            class_line += ":\n"

            var_lines = ""
            # TODO SEE VECTOR
            consistent_vars = [
                _var for _var in class_data["vars"] if _var.get("type") is not False
            ]
            if len(consistent_vars) > 0:
                for _var in consistent_vars:
                    python_type = convert_byte_type_python(_var.get("type"))
                    if not python_type:
                        import_lines += find_import_path_by_class_name(
                            _var.get("type"), protocol_json
                        )
                        python_type = _var.get("type")
                    var_lines += f"\t{_var.get('name')}:{python_type}\n"
            else:
                var_lines += "\t...\n"

            python_code = import_lines + class_line + var_lines

            class_path = os.path.dirname(
                os.path.join(
                    Path(__file__).parent,
                    class_data.get("path").split("code_source\\")[1],
                )
            )
            os.makedirs(class_path, exist_ok=True)
            with open(
                os.path.join(class_path, class_name + ".py"),
                "w",
            ) as python_file:
                python_file.write(python_code)
