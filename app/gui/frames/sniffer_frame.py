import os
from pathlib import Path
from pprint import pformat
from queue import Empty
from threading import Event
from typing import Callable, Dict, Optional, Type

from gui.components import (
    ButtonIcon,
    DetailMessageDialog,
    Frame,
    GroupBox,
    HorizontalLayout,
    VerticalLayout,
)
from network.models.message import Message
from PyQt5.QtCore import QSize, Qt, QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QBoxLayout,
    QColorDialog,
    QDialog,
    QDialogButtonBox,
    QDockWidget,
    QFrame,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLayout,
    QListWidget,
    QMainWindow,
    QMenu,
    QMessageBox,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSpacerItem,
    QStackedLayout,
    QStackedWidget,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)

from types_ import ThreadsInfos, ParsedMessage


class SnifferFrame(Frame):
    def __init__(self, threads_infos: ThreadsInfos, name: str) -> None:
        super().__init__(name)
        self.threads_infos = threads_infos
        self.sniffer_frame_layout = VerticalLayout()
        self.sniffer_frame_layout.setSpacing(0)

        self.set_header_sniffer()
        self.set_list_message()

        self.setLayout(self.sniffer_frame_layout)

        self.timer_check_new_msg = QTimer(self)
        self.timer_check_new_msg.timeout.connect(self.check_new_msg)
        self.timer_check_new_msg.start(100)

    def check_new_msg(self):
        try:
            while True:
                parsed_msg = self.threads_infos["queue_handler_message"].get_nowait()
                self.on_get_message(parsed_msg)
        except Empty:
            pass

    def on_reset(self):
        self.layout_messages.clear_list()

    def update_state_buttons(self):
        if self.threads_infos["event_play_sniffer"].is_set():
            self.button_play.set_active_button()
            self.button_stop.set_inactive_button()
        else:
            self.button_play.set_inactive_button()
            self.button_stop.set_active_button()

    def on_play(self):
        self.threads_infos["event_play_sniffer"].set()
        self.update_state_buttons()

    def on_stop(self):
        self.threads_infos["event_play_sniffer"].clear()
        self.update_state_buttons()

    def set_header_sniffer(self):
        self.box_header = GroupBox(with_title=False)

        self.header_layout = HorizontalLayout()
        self.header_layout.setSpacing(8)
        self.box_header.setLayout(self.header_layout)
        self.box_header.setFixedHeight(80)

        # Buttons
        self.button_reset = ButtonIcon("restart.svg")
        self.button_reset.clicked.connect(self.on_reset)
        self.header_layout.addWidget(self.button_reset)

        self.button_play = ButtonIcon("play.svg")
        self.button_play.clicked.connect(self.on_play)
        self.header_layout.addWidget(self.button_play)

        self.button_stop = ButtonIcon("stop")
        self.button_stop.clicked.connect(self.on_stop)
        self.header_layout.addWidget(self.button_stop)

        self.update_state_buttons()

        self.sniffer_frame_layout.addWidget(self.box_header)

    def set_list_message(self):
        self.box_messages = GroupBox()
        self.box_messages.setTitle("Messages reçus")
        self.box_messages.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_messages = VerticalLayout()
        self.layout_messages.setContentsMargins(0, 0, 0, 0)
        self.layout_messages.addStretch()
        self.layout_messages.setDirection(QBoxLayout.Direction.BottomToTop)
        self.box_messages.setLayout(self.layout_messages)

        scroll_area = QScrollArea()
        scroll_area.setWidget(self.box_messages)
        scroll_area.setWidgetResizable(True)

        self.sniffer_frame_layout.addWidget(scroll_area)

    def on_get_message(self, message: ParsedMessage):
        button = QPushButton(text=message.__type__)
        button.setFixedHeight(35)
        self.layout_messages.addWidget(button)
        button.clicked.connect(lambda: self.show_info_message_dialog(message))

    def show_info_message_dialog(self, message):
        dialog = DetailMessageDialog(self, parsed_msg=message)
        dialog.exec()
