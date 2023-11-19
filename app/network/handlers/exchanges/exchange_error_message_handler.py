import logging

from app.gui.signals import AppSignals
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeErrorMessage import \
    ExchangeErrorMessage
from app.types_.models.common import ParsedMessageHandler, BotInfo

logger = logging.getLogger(__name__)


class ExchangeErrorMessageHandler(ParsedMessageHandler, ExchangeErrorMessage):
    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        if bot_info.selling_info.is_playing_event.is_set() and (
        selling_hdv := bot_info.selling_info.selling_hdv) is not None:
            selling_hdv.is_selected_error = True
