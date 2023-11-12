from queue import Empty

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (
    QScrollArea,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QTreeWidget,
    QTreeWidgetItem,
    QAbstractItemView,
)

from app.gui.components.common import (
    ButtonIcon,
    Header,
    Frame,
)
from app.gui.components.organization import (
    VerticalLayout,
    HorizontalLayout,
    AlignDelegate,
)
from app.types_ import BotInfo


class SnifferFrame(Frame):
    def __init__(self, bot_info: BotInfo, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.bot_info = bot_info
        self.main_layout = VerticalLayout()
        self.info_message_widget: QWidget | None = None

        self.set_header_sniffer()
        self.set_content()

        self.setLayout(self.main_layout)

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

        self.main_layout.addWidget(self.header_sniffer)

    def set_content(self):
        self.content = QWidget()
        self.content_layout = HorizontalLayout()
        self.content.setLayout(self.content_layout)

        self.set_list_message()

        self.main_layout.addWidget(self.content)

    def set_list_message(self):
        self.table_messages = QTableWidget()
        self.table_messages.setColumnCount(3)
        self.table_messages.setColumnHidden(2, True)
        self.table_messages.setHorizontalHeaderLabels(["Origine", "Message"])

        delegate = AlignDelegate(self.table_messages)
        for column_index in range(2):
            self.table_messages.setItemDelegateForColumn(column_index, delegate)

        self.table_messages.horizontalHeader().setStretchLastSection(True)
        self.table_messages.verticalHeader().hide()
        self.table_messages.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_messages.cellClicked.connect(self.show_info_message)

        scroll_area = QScrollArea()
        scroll_area.setWidget(self.table_messages)
        scroll_area.setWidgetResizable(True)

        self.content_layout.addWidget(scroll_area)

    def on_get_message(self, parsed_message_json: dict):
        if self.bot_info.sniffer_info.is_playing_event.is_set():
            background_color = (
                "red" if parsed_message_json.get("from_client") else "green"
            )

            row_position = 0
            self.table_messages.insertRow(0)
            origin_col = QTableWidgetItem(
                "Client" if parsed_message_json.get("from_client") else "Server"
            )
            origin_col.setBackground(QColor(background_color))
            parsed_message_json.pop("from_client")

            self.table_messages.setItem(
                row_position,
                0,
                origin_col,
            )

            message_col = QTableWidgetItem(str(parsed_message_json.get("__type__")))
            message_col.setBackground(QColor(background_color))
            self.table_messages.setItem(row_position, 1, message_col)

            parsed_message_json.pop("__type__")

            message_col_data = QTableWidgetItem()
            message_col_data.setData(0, parsed_message_json)
            self.table_messages.setItem(row_position, 2, message_col_data)

    def on_quit_info_message(self):
        if self.info_message_widget is not None:
            self.info_message_widget.deleteLater()
            self.info_message_widget = None

    def show_info_message(self, row: int, _):
        if (msg_item := self.table_messages.item(row, 2)) is not None:
            parsed_msg_json: dict = msg_item.data(0)
            if self.info_message_widget is not None:
                self.info_message_widget.deleteLater()
                self.info_message_widget = None

            self.info_message_widget = QWidget()
            v_layout = VerticalLayout()
            self.info_message_widget.setLayout(v_layout)

            exit_button = ButtonIcon("quit.svg")
            exit_button.clicked.connect(self.on_quit_info_message)
            v_layout.addWidget(exit_button)

            self.info_message_tree = QTreeWidget()
            self.info_message_tree.header().hide()

            self.deep_tree_from_message_dict(
                parsed_msg_json, None, self.info_message_tree
            )
            v_layout.addWidget(self.info_message_tree)

            self.content_layout.addWidget(self.info_message_widget)

    def deep_tree_from_message_dict(
        self,
        _values,
        parent: QTreeWidgetItem | None = None,
        base_qtree: QTreeWidget | None = None,
    ):
        if not isinstance(_values, dict):
            widget_item = QTreeWidgetItem([f"{_values}"])
            if parent is not None:
                parent.addChild(widget_item)
        else:
            for key, value in _values.items():
                if isinstance(value, dict):
                    widget_item = QTreeWidgetItem([f"{key}"])
                    self.deep_tree_from_message_dict(value, widget_item)
                elif isinstance(value, list):
                    widget_item = QTreeWidgetItem([f"{key}"])
                    for _value in value:
                        self.deep_tree_from_message_dict(_value, widget_item)
                else:
                    widget_item = QTreeWidgetItem([f"{key} = {value}"])
                if parent is not None:
                    parent.addChild(widget_item)
                elif base_qtree is not None:
                    base_qtree.addTopLevelItem(widget_item)
