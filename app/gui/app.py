from queue import Empty, Queue
from threading import Event
from time import sleep
from typing import Callable, Dict, Optional, Type

from gui.components import HorizontalLayout
from gui.frames.sniffer_frame import SnifferFrame
from gui.utils import SideMenu
from network.models.message import Message, ParsedMessage
from PyQt5.QtCore import QEvent, QObject, QRunnable, QSize, Qt, QThreadPool, pyqtSignal
from PyQt5.QtGui import QCloseEvent, QColor, QPalette
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
from qt_material import apply_stylesheet


TITLE = "Bot Dofus"


class Application(QApplication):
    def __init__(self, argv) -> None:
        super().__init__(argv)
        apply_stylesheet(self, theme="dark_teal.xml")
        self.setApplicationName(TITLE)
        self.setStyle("Fusion")


class MainWindow(QMainWindow):
    BASE_WIDTH = 1200
    BASE_HEIGHT = 900

    queue_handler_message: Queue[ParsedMessage]
    event_play_sniffer: Event
    frame_sniffer: SnifferFrame | None
    side_menu: SideMenu | None
    is_active: bool = True

    def __init__(
        self,
        queue_handler_message: Queue[ParsedMessage],
        event_play_sniffer: Event,
    ) -> None:
        super().__init__()
        self.event_play_sniffer = event_play_sniffer
        self.queue_handler_message = queue_handler_message

        self.setWindowTitle(TITLE)
        self.resize(self.BASE_WIDTH, self.BASE_HEIGHT)
        self.show()

        self.all_content = QWidget()
        self.layout_all_content = HorizontalLayout()
        self.layout_all_content.setSpacing(0)

        self.stacked_frames = QStackedWidget()

        self.set_menu()
        self.set_pages()

        self.all_content.setLayout(self.layout_all_content)
        self.setCentralWidget(self.all_content)

        self.set_up_listener()

    def set_menu(self):
        self.side_menu = SideMenu(parent=self.all_content)
        self.side_menu.on_change_page_signal.connect(
            self.stacked_frames.setCurrentIndex
        )
        self.layout_all_content.addWidget(self.side_menu)

    def set_pages(self):
        self.frame_sniffer = SnifferFrame(
            parent=self.all_content, event_play_sniffer=self.event_play_sniffer
        )
        self.frame_bot_fm = QFrame()
        self.stacked_frames.addWidget(self.frame_sniffer)
        self.stacked_frames.addWidget(self.frame_bot_fm)
        self.layout_all_content.addWidget(self.stacked_frames)

    def set_up_listener(self):
        if self.queue_handler_message is not None and self.frame_sniffer is not None:
            msg_listener = MessageListener(
                queue_handler_message=self.queue_handler_message, parent=self
            )
            if (global_instance := QThreadPool.globalInstance()) is not None:
                global_instance.start(msg_listener)

            msg_listener.signals.new_message.connect(self.frame_sniffer.on_get_message)

    def closeEvent(self, _: QCloseEvent):
        self.is_active = False


class NetworkSignals(QObject):
    new_message = pyqtSignal(ParsedMessage)


class MessageListener(QRunnable):
    def __init__(self, queue_handler_message: Queue, parent: MainWindow):
        super().__init__()
        self.parent = parent
        self.queue_handler_message = queue_handler_message
        self.signals = NetworkSignals()

    def run(self):
        while self.parent.is_active:
            try:
                message = self.queue_handler_message.get(timeout=1)
                if self.parent.is_active:
                    self.signals.new_message.emit(message)
            except Empty:
                continue
