from importlib import import_module
import logging
import os
import socket

from types_.interface import ThreadsInfos

logger = logging.getLogger(__name__)


def get_local_ip() -> str:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(0)
    try:
        sock.connect(("10.255.255.255", 1))
        ip_local = sock.getsockname()[0]
        logger.info(msg=f"Local ip = {ip_local}")
    except Exception as err:
        logger.error(f"Exception on get local ip : {err}")
        ip_local = "127.0.0.1"
    finally:
        sock.close()
    return ip_local


def send_parsed_msg(threads_infos: ThreadsInfos, parsed_message, from_client=True):
    msg_to_send = {
        **parsed_message,
        "from_client": from_client,
        "type": f"__{parsed_message.__class__.__name__}__",
    }
    threads_infos["queue_msg_to_send"].put(msg_to_send)


def convert_snake_case_to_camel_case(snake_case_str: str):
    camel_case_str = ""
    for word in snake_case_str.split("_"):
        camel_case_str += word[0].upper() + word[1:]
    return camel_case_str


def get_classes_in_path(path, condition_end_file: str) -> list:
    class_handlers = []
    for folder, sub_folder, files in os.walk(path):
        folder = os.path.relpath(folder).replace("app\\", "").replace("\\", ".")

        for file in files:
            if file.endswith(condition_end_file) and not file.startswith("__init__"):
                file_path = f"{folder}.{file[:-3]}"
                mod = import_module(file_path)
                class_handlers.append(
                    getattr(mod, f"{convert_snake_case_to_camel_case(file[:-3])}")
                )
    return class_handlers
