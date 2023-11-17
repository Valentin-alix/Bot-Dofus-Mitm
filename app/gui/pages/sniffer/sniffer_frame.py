from queue import Empty

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (
    QWidget,
    QTableWidgetItem,
    QAbstractItemView, QTableWidget, )

from app.gui.components.common import (
    ButtonIcon,
    Header,
    Frame, TableWidget,
)
from app.gui.components.organization import (
    VerticalLayout,
    HorizontalLayout,
)
from app.gui.pages.sniffer.detail_message import DetailMessage
from app.types_ import BotInfo


class SnifferFrame(Frame):
    header_sniffer: Header
    content: QWidget
    content_layout: HorizontalLayout
    table_messages: QTableWidget

    def __init__(self, bot_info: BotInfo, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.bot_info = bot_info

        self.layout = VerticalLayout()
        self.detail_msg: DetailMessage | None = None

        self.set_header_sniffer()
        self.set_content()

        self.setLayout(self.layout)

        self.timer_check_new_msg = QTimer(self)
        self.timer_check_new_msg.timeout.connect(self.check_new_msg)
        self.timer_check_new_msg.start(300)

    def check_new_msg(self):
        try:
            while True:
                parsed_msg = (
                    self.bot_info.sniffer_info.parsed_message_queue.get_nowait()
                )
                self.on_get_message(vars(parsed_msg))
        except Empty:
            pass

    def on_reset(self):
        self.table_messages.clearContents()
        self.table_messages.setRowCount(0)

    def on_play(self):
        self.bot_info.sniffer_info.is_playing_event.set()
        self.header_sniffer.do_play(
            self.bot_info.sniffer_info.is_playing_event.is_set()
        )

    def on_stop(self):
        self.bot_info.sniffer_info.is_playing_event.clear()
        self.header_sniffer.do_play(
            self.bot_info.sniffer_info.is_playing_event.is_set()
        )

    def set_header_sniffer(self):
        self.header_sniffer = Header()

        self.header_sniffer.button_reset = ButtonIcon("restart.svg")
        self.header_sniffer.button_reset.clicked.connect(self.on_reset)
        self.header_sniffer.h_layout.insertWidget(0, self.header_sniffer.button_reset)

        self.header_sniffer.button_play.clicked.connect(self.on_play)
        self.header_sniffer.button_stop.clicked.connect(self.on_stop)
        self.header_sniffer.do_play(
            self.bot_info.sniffer_info.is_playing_event.is_set()
        )

        self.layout.addWidget(self.header_sniffer)

    def set_content(self):
        self.content = QWidget()
        self.content_layout = HorizontalLayout()
        self.content.setLayout(self.content_layout)

        self.set_list_message()

        self.layout.addWidget(self.content)

    def set_list_message(self):
        table_messages_scroll = TableWidget(columns_name=["Origine", "Message"])
        self.table_messages = table_messages_scroll.table

        self.table_messages.setColumnCount(3)
        self.table_messages.setColumnHidden(2, True)
        self.table_messages.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_messages.cellClicked.connect(self.show_info_message)

        self.content_layout.addWidget(table_messages_scroll)

    def on_get_message(self, parsed_message_json: dict):
        if self.bot_info.sniffer_info.is_playing_event.is_set():
            background_color = (
                "red" if parsed_message_json.get("from_client") else "green"
            )

            self.table_messages.insertRow(0)

            origin_col = QTableWidgetItem(
                "Client" if parsed_message_json.pop("from_client") else "Server"
            )
            origin_col.setBackground(QColor(background_color))
            self.table_messages.setItem(0, 0, origin_col)

            message_col = QTableWidgetItem(parsed_message_json.pop("__type__"))
            message_col.setBackground(QColor(background_color))
            self.table_messages.setItem(0, 1, message_col)

            message_col_data = QTableWidgetItem()
            message_col_data.setData(0, parsed_message_json)
            self.table_messages.setItem(0, 2, message_col_data)

    def show_info_message(self, row: int, _):
        if (msg_item := self.table_messages.item(row, 2)) is not None:
            self.quit_detail_msg()
            parsed_msg_json: dict = msg_item.data(0)

            self.detail_msg = DetailMessage(parsed_msg_json)
            self.detail_msg.quit_btn.clicked.connect(self.quit_detail_msg)
            self.content_layout.addWidget(self.detail_msg)

    def quit_detail_msg(self):
        if self.detail_msg is not None:
            self.detail_msg.deleteLater()
            self.detail_msg = None
