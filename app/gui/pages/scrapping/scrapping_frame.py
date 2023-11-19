from app.database.models import get_engine
from app.gui.components.common import (
    TopPage,
    Frame, Widget,
)
from app.gui.components.organization import VerticalLayout
from app.gui.pages.scrapping.chart import Chart
from app.gui.pages.scrapping.remaining_content import RemainingContent
from app.gui.pages.scrapping.valuable_info import ValuableInfo
from app.gui.signals import AppSignals
from app.types_.models.common import BotInfo


class ScrappingFrame(Frame):
    header_widget: Widget
    header: TopPage
    content_widget: Widget
    chart: Chart
    valuable_info: ValuableInfo
    remaining_content: RemainingContent

    def __init__(self, bot_info: BotInfo, app_signals: AppSignals, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.server_id: int | None = None

        self.engine = get_engine()

        self.app_signals = app_signals
        self.bot_info = bot_info

        self.main_frame_layout = VerticalLayout()

        self.set_header()
        self.setup_content()

        self.setLayout(self.main_frame_layout)

        self.app_signals.on_new_scraping_current_state.connect(self.remaining_content.update_content)
        self.app_signals.on_new_server_id.connect(self.on_new_server_id)

    def on_new_server_id(self) -> None:
        if (server_id := self.bot_info.common_info.server_id) != self.server_id:
            self.server_id = server_id
            self.chart.server_id = server_id
            self.valuable_info.server_id = server_id
            self.chart.on_select_item(self.chart.filters.item_combobox.currentText())
            self.valuable_info.on_reset()

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
        self.remaining_content = RemainingContent(parent=self, bot_info=self.bot_info)
        self.remaining_content.hide()
        layout_content.addWidget(self.remaining_content)

        self.chart = Chart(parent=self.content_widget, engine=self.engine, bot_info=self.bot_info)
        layout_content.addWidget(self.chart)

        self.valuable_info = ValuableInfo(parent=self.content_widget, engine=self.engine,
                                          bot_info=self.bot_info)
        layout_content.addWidget(self.valuable_info)

        self.main_frame_layout.addWidget(self.content_widget)

    def on_reset(self):
        self.chart.on_select_item(self.chart.filters.item_combobox.currentText())
        self.valuable_info.on_reset()

    def on_update_do_play_scrapping(self, do_play: bool):
        if do_play:
            self.bot_info.scraping_info.is_playing_event.set()
        else:
            self.bot_info.scraping_info.is_playing_event.clear()
        self.header.do_play(do_play)
