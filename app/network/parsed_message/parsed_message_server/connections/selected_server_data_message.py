from network.parsed_message.parsed_message_server.parsed_message_server import (
    ParsedMessageServer,
)
import types_
from types_.interface import ThreadsInfos


class SelectedServerDataMessage(ParsedMessageServer):
    address: str
    canCreateNewCharacter: bool
    ports: list[int]
    serverId: int
    ticket: list[int]

    def handle(self, threads_infos: ThreadsInfos) -> None:
        with threads_infos["server_id_with_lock"]["lock"]:
            threads_infos["server_id_with_lock"]["server_id"] = self.serverId
