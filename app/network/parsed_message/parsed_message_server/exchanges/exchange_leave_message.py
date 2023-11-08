from __future__ import annotations
import logging

from network.parsed_message.parsed_message_server.parsed_message_server import (
    ParsedMessageServer,
)
import types_

logger = logging.getLogger(__name__)


class ExchangeLeaveMessage(ParsedMessageServer):
    """When leaving modal"""

    dialogType: int
    success: bool

    def handle(self, threads_infos: types_.ThreadsInfos) -> None:
        if self.dialogType == types_.DialogType.DIALOG_EXCHANGE:
            with threads_infos.get("buying_hdv_with_lock").get("lock"):
                if (
                    buying_hdv := threads_infos.get("buying_hdv_with_lock").get(
                        "buying_hdv"
                    )
                ) is not None:
                    logger.info("deleting buying hdv")
                    buying_hdv.stop_timer = True
                    threads_infos["buying_hdv_with_lock"]["buying_hdv"] = None
            with threads_infos.get("selling_hdv_with_lock").get("lock"):
                if (
                    threads_infos.get("selling_hdv_with_lock").get("selling_hdv")
                ) is not None:
                    logger.info("deleting selling hdv")
                    threads_infos["selling_hdv_with_lock"]["selling_hdv"] = None
