from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QFrame, QStackedWidget, QVBoxLayout
from qfluentwidgets import TabBar, TabCloseButtonDisplayMode

from app.gui.components.common import TopPage
from app.gui.pages.scrapping.scrapping_craft_tab.scrapping_craft import ScrappingCraft
from app.gui.pages.scrapping.scrapping_price_tab.chart_price import ChartPrice
from app.gui.pages.scrapping.scrapping_progression import ScrappingProgression
from app.gui.pages.scrapping.scrapping_tables_tab.scrapping_tables import (
    ScrappingTables,
)
from app.gui.signals import AppSignals
from app.interfaces.models.common import BotInfo


class ScrappingFrame(QFrame):
    def __init__(
        self,
        bot_info: BotInfo,
        app_signals: AppSignals,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.bot_info = bot_info
        self.app_signals = app_signals
        self.server_id: int | None = None

        self.setLayout(QVBoxLayout(self))
        self.layout().setAlignment(Qt.AlignTop)

        self.init_header()

        self.init_tabs()

        self.app_signals.on_new_buying_hdv_playing_value.connect(
            lambda: self.on_update_do_play_scrapping(
                self.bot_info.scraping_info.is_playing_event.is_set()
            )
        )

        self.app_signals.on_new_server_id.connect(self.on_new_server_id)

    def init_header(self):
        self.progress_widget = ScrappingProgression(bot_info=self.bot_info)
        self.app_signals.on_leaving_hdv.connect(self.progress_widget.hide)
        self.app_signals.on_new_scraping_current_state.connect(
            self.progress_widget.update_content
        )
        self.layout().addWidget(self.progress_widget)
        self.progress_widget.hide()

        self.header = TopPage()
        self.header.do_play(self.bot_info.scraping_info.is_playing_event.is_set())
        self.header.button_play.clicked.connect(
            lambda: self.on_update_do_play_scrapping(True)
        )
        self.header.button_stop.clicked.connect(
            lambda: self.on_update_do_play_scrapping(False)
        )

        self.layout().addWidget(self.header)

    def init_tabs(self):
        self.tabs_stacked = QStackedWidget(self)

        self.tabs = TabBar(self)
        self.tabs.setCloseButtonDisplayMode(TabCloseButtonDisplayMode.NEVER)
        self.tabs.setAddButtonVisible(False)

        self.scrapping_prices = ChartPrice(self.bot_info)
        self.tabs_stacked.addWidget(self.scrapping_prices)
        self.tabs.addTab("scraping.prices", "Évolution des prix")

        self.scrapping_tables = ScrappingTables(
            self.server_id, self.bot_info, self.app_signals
        )
        self.tabs_stacked.addWidget(self.scrapping_tables)
        self.tabs.addTab("scraping.tables", "Chute de Prix / Bénéfices Recyclage")

        self.scrapping_craft = ScrappingCraft(self.bot_info, self.app_signals)
        self.tabs_stacked.addWidget(self.scrapping_craft)
        self.tabs.addTab("scraping.craft", "Bénéfices Craft")

        self.tabs.currentChanged.connect(self.on_tab_changed)

        self.layout().addWidget(self.tabs)
        self.layout().addWidget(self.tabs_stacked)

    @pyqtSlot()
    def on_new_server_id(self) -> None:
        if (server_id := self.bot_info.common_info.server_id) != self.server_id:
            self.server_id = server_id

            self.scrapping_prices.server_id = server_id
            self.scrapping_prices.on_select_item(
                self.scrapping_prices.filters.item_combobox.currentText()
            )

            self.scrapping_tables.server_id = server_id

            self.scrapping_tables.benefit_recycling.table.server_id = server_id
            self.scrapping_tables.benefit_recycling.table.get_benefit_recycling(
                self.scrapping_tables.benefit_recycling.filters.quantity.currentText()
            )

            self.scrapping_tables.price_drop.server_id = server_id
            self.scrapping_tables.price_drop.table.server_id = server_id
            self.scrapping_tables.price_drop.table.get_price_drop(
                self.scrapping_tables.price_drop.filters.quantity.currentText()
            )

            self.scrapping_craft.server_id = server_id

    @pyqtSlot(int)
    def on_tab_changed(self, index: int):
        self.tabs_stacked.setCurrentIndex(index)

    @pyqtSlot(bool)
    def on_update_do_play_scrapping(self, do_play: bool):
        if do_play:
            self.bot_info.scraping_info.is_playing_event.set()
        else:
            self.bot_info.scraping_info.is_playing_event.clear()
        self.header.do_play(do_play)
