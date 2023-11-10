import logging
import os
from pathlib import Path
from typing import Any
from importlib import import_module

from modules.character import Character
from modules.hdv.buying_hdv import BuyingHdv
from modules.hdv.selling_hdv import SellingHdv
from time import perf_counter
from network.utils import convert_snake_case_to_camel_case
from types_ import ParsedMessage, ThreadsInfos, ParsedMessageHandler
from types_.dofus.utils import CLASSES_BY_NAME

logger = logging.getLogger(__name__)


class Handler:
    def __init__(self, threads_infos: ThreadsInfos) -> None:
        self.buying_hdv: BuyingHdv | None = None
        self.selling_hdv: SellingHdv | None = None
        self.character: Character | None = None
        self.threads_infos = threads_infos
        before = perf_counter()
        self.classes_handler = self.get_classes_in_path(
            os.path.join(Path(__file__).parent, "handlers"), "handler.py"
        )
        print(perf_counter() - before)

    def handle_message_unpacked(self, parsed_message: ParsedMessage):
        if self.threads_infos.get("event_play_sniffer").is_set():
            self.threads_infos.get("queue_handler_message").put(parsed_message)
        class_handler = next(
            (
                class_handler
                for class_handler in self.classes_handler
                if class_handler.__name__ == f"{parsed_message.__type__}Handler"
            ),
            None,
        )
        if class_handler is not None:
            self.deep_dict_to_object(parsed_message)
            class_handler_instance = class_handler(
                **self.deep_dict_to_object(parsed_message)
            )
            class_handler_instance.handle(self.threads_infos)

    def deep_dict_to_object(self, _dict) -> Any:
        for key, value in vars(_dict).items():
            if (
                isinstance(value, dict)
                and (class_type_name := value.pop("__type__")) is not None
                and (class_type := CLASSES_BY_NAME.get(class_type_name)) is not None
            ):
                value_converted = self.deep_dict_to_object(value)
                value = class_type(**value_converted)
                print(value)
        return _dict

    def get_classes_in_path(
        self, path, condition_end_file: str
    ) -> list[type[ParsedMessageHandler]]:
        class_handlers = []
        for folder, sub_folder, files in os.walk(path):
            folder = os.path.relpath(folder).replace("app\\", "").replace("\\", ".")

            for file in files:
                if file.endswith(condition_end_file) and not file.startswith(
                    "__init__"
                ):
                    file_path = f"{folder}.{file[:-3]}"
                    mod = import_module(file_path)
                    class_handlers.append(
                        getattr(mod, f"{convert_snake_case_to_camel_case(file[:-3])}")
                    )
        return class_handlers
