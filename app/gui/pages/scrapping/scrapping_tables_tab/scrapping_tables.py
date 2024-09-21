from PyQt5.QtWidgets import QHBoxLayout, QWidget

from app.gui.pages.scrapping.scrapping_tables_tab.benefit_recycling.benefit_recycling import (
    BenefitRecycling,
)
from app.gui.pages.scrapping.scrapping_tables_tab.price_drop.price_drop import (
    PriceDrop,
)
from app.gui.signals import AppSignals
from app.interfaces.models.common import BotInfo


class ScrappingTables(QWidget):
    def __init__(
        self,
        server_id: int | None,
        bot_info: BotInfo,
        app_signals: AppSignals,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.server_id = server_id
        self.app_signals = app_signals
        self.bot_info = bot_info

        self.setLayout(QHBoxLayout(self))

        self.setup_content()

    def setup_content(self):
        self.benefit_recycling = BenefitRecycling(self.server_id)
        self.layout().addWidget(self.benefit_recycling)

        self.price_drop = PriceDrop()
        self.layout().addWidget(self.price_drop)
