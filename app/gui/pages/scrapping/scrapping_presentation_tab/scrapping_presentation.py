from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget
from qfluentwidgets import VBoxLayout
from sqlalchemy import Engine

from app.gui.pages.scrapping.scrapping_presentation_tab.benefit_recycling_table import (
    BenefitRecyclingTable,
)
from app.gui.pages.scrapping.scrapping_presentation_tab.chart import Chart
from app.gui.pages.scrapping.scrapping_presentation_tab.price_drop_table import (
    PriceDropTable,
)
from app.gui.signals import AppSignals
from app.types_.models.common import BotInfo


class ScrappingPresentation(QWidget):
    def __init__(
        self,
        bot_info: BotInfo,
        app_signals: AppSignals,
        engine: Engine,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.server_id: int | None = None

        self.engine = engine

        self.app_signals = app_signals
        self.bot_info = bot_info

        self.setLayout(QVBoxLayout(self))
        self.layout().setAlignment(Qt.AlignTop)

        self.setup_content()

        self.app_signals.on_new_server_id.connect(self.on_new_server_id)

    @pyqtSlot()
    def on_new_server_id(self) -> None:
        if (server_id := self.bot_info.common_info.server_id) != self.server_id:
            self.server_id = server_id
            self.chart.server_id = server_id
            self.table_benefit_recycling.server_id = server_id
            self.table_price_drop.server_id = server_id
            self.chart.on_select_item(self.chart.filters.item_combobox.currentText())
            self.table_benefit_recycling.get_benefit_recycling()
            self.table_price_drop.get_price_drop()

    def setup_content(self):
        self.content_widget = QWidget(parent=self)
        self.content_widget.setLayout(VBoxLayout(self.content_widget))

        self.chart = Chart(
            parent=self.content_widget, engine=self.engine, bot_info=self.bot_info
        )
        self.content_widget.layout().addWidget(self.chart)

        tables = QWidget()
        self.content_widget.layout().addWidget(tables)
        tables.setLayout(QHBoxLayout())

        self.table_benefit_recycling = BenefitRecyclingTable(self.engine)
        tables.layout().addWidget(self.table_benefit_recycling)

        self.table_price_drop = PriceDropTable(self.engine)
        tables.layout().addWidget(self.table_price_drop)

        self.layout().addWidget(self.content_widget)
