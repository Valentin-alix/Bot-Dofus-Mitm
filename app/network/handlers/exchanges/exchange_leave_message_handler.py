import logging

import types_
from types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeLeaveMessage import (
    ExchangeLeaveMessage,
)
from types_.parsed_message import ParsedMessageHandler

logger = logging.getLogger(__name__)


class ExchangeLeaveMessageHandler(ParsedMessageHandler, ExchangeLeaveMessage):
    """When leaving modal"""

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
