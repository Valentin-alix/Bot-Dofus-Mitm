from sqlalchemy import Engine

from app.gui.components.common import (
    TopPage,
    Widget,
)
from app.gui.components.organization import VerticalLayout, HorizontalLayout
from app.gui.pages.scrapping.scrapping_presentation_tab.benefit_recycling_table import BenefitRecyclingTable
from app.gui.pages.scrapping.scrapping_presentation_tab.chart import Chart
from app.gui.pages.scrapping.scrapping_presentation_tab.price_drop_table import PriceDropTable
from app.gui.pages.scrapping.scrapping_presentation_tab.scrapping_progression import ScrappingProgression
from app.gui.signals import AppSignals
from app.types_.models.common import BotInfo


class ScrappingPresentation(Widget):
    FIELD_BY_QUANTITY = {
        "100": "hundred",
        "10": "ten",
        "1": "one"
    }

    def __init__(self, bot_info: BotInfo, app_signals: AppSignals, engine: Engine, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.server_id: int | None = None

        self.engine = engine

        self.app_signals = app_signals
        self.bot_info = bot_info

        self.main_frame_layout = VerticalLayout()

        self.set_header()
        self.setup_content()

        self.setLayout(self.main_frame_layout)

        self.app_signals.on_leaving_hdv.connect(self.remaining_content.hide)
        self.app_signals.on_new_scraping_current_state.connect(self.remaining_content.update_content)
        self.app_signals.on_new_server_id.connect(self.on_new_server_id)

        self.app_signals.on_new_buying_hdv_playing_value.connect(
            lambda: self.header.do_play(self.bot_info.scraping_info.is_playing_event.is_set()))

    def on_new_server_id(self) -> None:
        if (server_id := self.bot_info.common_info.server_id) != self.server_id:
            self.server_id = server_id
            self.chart.server_id = server_id
            self.table_benefit_recycling.server_id = server_id
            self.table_price_drop.server_id = server_id
            self.on_reset()

    def set_header(self):
        self.header = TopPage(parent=self, with_restart=True)
        self.header.do_play(self.bot_info.scraping_info.is_playing_event.is_set())
        self.header.button_reset.clicked.connect(self.on_reset)
        self.header.button_play.clicked.connect(
            lambda: self.on_update_do_play_scrapping(True)
        )
        self.header.button_stop.clicked.connect(
            lambda: self.on_update_do_play_scrapping(False)
        )

        self.main_frame_layout.addWidget(self.header)

    def setup_content(self):
        self.content_widget = Widget(parent=self)

        layout_content = VerticalLayout()
        self.content_widget.setLayout(layout_content)
        self.remaining_content = ScrappingProgression(parent=self, bot_info=self.bot_info)
        self.remaining_content.hide()
        layout_content.addWidget(self.remaining_content)

        self.chart = Chart(parent=self.content_widget, engine=self.engine, bot_info=self.bot_info)
        layout_content.addWidget(self.chart)

        tables = Widget()
        layout_content.addWidget(tables)
        h_layout = HorizontalLayout()
        tables.setLayout(h_layout)

        self.table_benefit_recycling = BenefitRecyclingTable(self.engine)
        h_layout.addWidget(self.table_benefit_recycling)

        self.table_price_drop = PriceDropTable(self.engine)
        h_layout.addWidget(self.table_price_drop)

        self.main_frame_layout.addWidget(self.content_widget)

    def on_reset(self):
        self.chart.on_select_item(self.chart.filters.item_combobox.currentText())
        self.table_benefit_recycling.get_benefit_recycling()
        self.table_price_drop.get_price_drop()

    def on_update_do_play_scrapping(self, do_play: bool):
        if do_play:
            self.bot_info.scraping_info.is_playing_event.set()
        else:
            self.bot_info.scraping_info.is_playing_event.clear()
        self.header.do_play(do_play)
