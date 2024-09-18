from PyQt5.QtWidgets import (
    QFrame,
    QHBoxLayout,
)

from app.gui.pages.seller.selling_from_inventory import SellingFromInventory
from app.gui.pages.seller.selling_update import SellingUpdate
from app.gui.signals import AppSignals
from app.types_.models.common import BotInfo


class SellerFrame(QFrame):
    def __init__(
        self, bot_info: BotInfo, app_signals: AppSignals, *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)

        self.bot_info = bot_info
        self.app_signals = app_signals

        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        self.selling = SellingFromInventory(self.bot_info, self.app_signals)
        self.main_layout.addWidget(self.selling)

        self.selling_update = SellingUpdate(self.bot_info, self.app_signals)
        self.main_layout.addWidget(self.selling_update)
