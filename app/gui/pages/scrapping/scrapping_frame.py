from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (
    QWidget,
)

from app.database.models import get_engine
from app.gui.components.common import (
    Header,
    Frame, ButtonIcon,
)
from app.gui.components.organization import VerticalLayout
from app.gui.pages.scrapping.chart import Chart
from app.gui.pages.scrapping.remaining_content import RemainingContent
from app.gui.pages.scrapping.valuable_info import ValuableInfo
from app.modules.hdv.buying_hdv import BuyingHdv
from app.types_ import BotInfo


class ScrappingFrame(Frame):
    header_widget: QWidget
    header: Header
    content_widget: QWidget
    chart: Chart
    valuable_info: ValuableInfo
    remaining_content: RemainingContent

    def __init__(self, bot_info: BotInfo, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.server_id: int | None = None

        self.engine = get_engine()

        self.buying_hdv: BuyingHdv | None = None
        self.bot_info = bot_info

        self.main_frame_layout = VerticalLayout()

        self.set_header()
        self.setup_content()

        self.setLayout(self.main_frame_layout)

        self.timer = QTimer(parent=self)
        self.timer.timeout.connect(self.check_buying_hdv)
        self.timer.start(200)

        self.timer_server_id = QTimer(parent=self)
        self.timer_server_id.timeout.connect(self.on_new_server_id)
        self.timer_server_id.start(1000)

    def check_buying_hdv(self):
        with self.bot_info.scraping_info.buying_hdv_with_lock.get("lock"):
            self.buying_hdv = self.bot_info.scraping_info.buying_hdv_with_lock.get(
                "buying_hdv"
            )
        self.remaining_content.update_content()

    def on_new_server_id(self):
        if (server_id := self.bot_info.common_info.server_id) != self.server_id:
            self.server_id = server_id
            self.chart.server_id = server_id
            self.valuable_info.server_id = server_id
            self.chart.on_select_item(self.chart.filters.item_combobox.currentText())
            self.valuable_info.on_reset()

    def set_header(self):
        self.header_widget = QWidget()

        v_layout = VerticalLayout()
        self.header_widget.setLayout(v_layout)

        self.header = Header(parent=self)
        v_layout.addWidget(self.header)
        self.header.do_play(self.bot_info.scraping_info.is_playing_event.is_set())
        self.header.button_play.clicked.connect(
            lambda: self.on_update_do_play_scrapping(True)
        )
        self.header.button_stop.clicked.connect(
            lambda: self.on_update_do_play_scrapping(False)
        )

        button_reset = ButtonIcon("restart.svg", parent=self.header)
        button_reset.clicked.connect(self.on_reset)
        v_layout.addWidget(button_reset)

        self.main_frame_layout.addWidget(self.header_widget)

    def setup_content(self):
        self.content_widget = QWidget(parent=self)

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
