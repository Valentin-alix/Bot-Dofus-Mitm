from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.connection.SelectedServerDataMessage import (
    SelectedServerDataMessage,
)
from app.types_.interface import ThreadsInfos
from app.types_.parsed_message import ParsedMessageHandler


class SelectedServerDataMessageHandler(ParsedMessageHandler, SelectedServerDataMessage):
    def handle(self, threads_infos: ThreadsInfos) -> None:
        with threads_infos["server_id_with_lock"]["lock"]:
            threads_infos["server_id_with_lock"]["server_id"] = self.serverId
