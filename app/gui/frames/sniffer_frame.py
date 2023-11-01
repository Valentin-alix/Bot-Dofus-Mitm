from typing import Optional, Dict, Type, Callable
import os
from threading import Event
from pathlib import Path
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QGroupBox,
    QVBoxLayout,
    QHBoxLayout,
    QSizePolicy,
    QLabel,
    QBoxLayout,
    QDialogButtonBox,
    QDialog,
    QMessageBox,
    QColorDialog,
    QLayout,
    QWidget,
    QFrame,
    QAction,
    QListWidget,
    QStatusBar,
    QMenu,
    QStackedWidget,
    QStackedLayout,
    QScrollArea,
    QDockWidget,
    QSpacerItem,
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from gui.components import DetailMessageDialog

from network.models.message import Message


class SnifferFrame(QFrame):
    def __init__(self, parent, event_play_sniffer: Event) -> None:
        super().__init__(parent)
        self.main_layout = QVBoxLayout()
        self.event_play_sniffer = event_play_sniffer
        self.set_header_sniffer()
        self.set_list_message()

        self.setLayout(self.main_layout)

    def on_reset(self):
        for i in reversed(range(self.layout_messages.count())):
            if (item_child_layout := self.layout_messages.itemAt(i)) is not None and (
                child_layout := item_child_layout.widget()
            ) is not None:
                child_layout.setParent(None)

    def update_state_buttons(self):
        if self.event_play_sniffer.is_set():
            self.button_play.setStyleSheet("background-color: grey")
            self.button_stop.setStyleSheet("background-color: rgb(53, 53, 53)")
        else:
            self.button_stop.setStyleSheet("background-color: grey")
            self.button_play.setStyleSheet("background-color: rgb(53, 53, 53)")

    def on_play(self):
        self.event_play_sniffer.set()
        self.update_state_buttons()

    def on_stop(self):
        self.event_play_sniffer.clear()
        self.update_state_buttons()

    def set_header_sniffer(self):
        self.box_header = QGroupBox()
        self.box_header.setContentsMargins(0, 0, 0, 0)
        self.header_layout = QHBoxLayout()
        self.header_layout.setSpacing(0)
        self.header_layout.setContentsMargins(0, 0, 0, 0)

        # Buttons
        self.button_reset = QPushButton(text="Réinitialiser la liste")
        self.button_reset.setIcon(
            QIcon(
                os.path.join(
                    Path(__file__).parent.parent,
                    "resources",
                    "reset.png",
                )
            )
        )
        self.button_reset.clicked.connect(self.on_reset)
        self.button_reset.setFixedHeight(40)
        self.header_layout.addWidget(self.button_reset)

        self.button_play = QPushButton(text="Lancer le sniffeur")
        self.button_play.setIcon(
            QIcon(
                os.path.join(
                    Path(__file__).parent.parent,
                    "resources",
                    "play.png",
                )
            )
        )
        self.button_play.clicked.connect(self.on_play)
        self.button_play.setFixedHeight(40)
        self.header_layout.addWidget(self.button_play)

        self.button_stop = QPushButton(text="Arrêter le sniffeur")
        self.button_stop.setIcon(
            QIcon(
                os.path.join(
                    Path(__file__).parent.parent,
                    "resources",
                    "stop.png",
                )
            )
        )
        self.button_stop.clicked.connect(self.on_stop)
        self.button_stop.setFixedHeight(40)
        self.header_layout.addWidget(self.button_stop)

        self.update_state_buttons()

        self.box_header.setLayout(self.header_layout)
        self.main_layout.addWidget(self.box_header)

    def set_list_message(self):
        self.box_messages = QGroupBox()
        self.box_messages.setTitle("Messages reçus")
        self.box_messages.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_messages = QVBoxLayout()
        self.layout_messages.addStretch()
        self.layout_messages.setDirection(QBoxLayout.Direction.BottomToTop)
        self.box_messages.setLayout(self.layout_messages)
        self.layout_messages.setContentsMargins(0, 0, 0, 0)
        self.layout_messages.setSpacing(0)

        scroll_area = QScrollArea()
        scroll_area.setWidget(self.box_messages)
        scroll_area.setWidgetResizable(True)

        self.main_layout.addWidget(scroll_area)

    def on_get_message(self, message: Message):
        button = QPushButton(text=message.message_type)
        button.setFixedHeight(35)
        self.layout_messages.addWidget(button)
        button.clicked.connect(lambda: self.show_info_message_dialog(message))

    def show_info_message_dialog(self, message):
        dialog = DetailMessageDialog(self, message=message)
        dialog.exec()
