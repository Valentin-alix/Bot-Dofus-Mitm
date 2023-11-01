from typing import Optional, Dict, Type, Callable

from threading import Event
from time import sleep
from queue import Queue, Empty

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
from PyQt5.QtCore import Qt, QSize, QObject, pyqtSignal, QRunnable, QThreadPool, QEvent
from PyQt5.QtGui import QPalette, QColor, QCloseEvent
from gui.frames.sniffer_frame import SnifferFrame

from gui.utils import QDarkThemePalette, SideMenu
from network.models.message import Message


class Application(QApplication):
    def __init__(self, argv) -> None:
        super().__init__(argv)
        palette = QDarkThemePalette()
        self.setPalette(palette)
        self.setApplicationName("Bot dofus")
        self.setStyle("Fusion")


class MainWindow(QMainWindow):
    queue_handler_message: Queue[Message]
    event_play_sniffer: Event
    frame_sniffer: SnifferFrame | None
    side_menu: SideMenu | None
    is_active: bool = True

    def __init__(
        self,
        queue_handler_message: Queue[Message],
        event_play_sniffer: Event,
    ) -> None:
        super().__init__()
        self.event_play_sniffer = event_play_sniffer
        self.queue_handler_message = queue_handler_message
        self.setWindowTitle("Bot Dofus")
        self.resize(800, 500)
        self.show()

        self.all_content = QWidget()
        self.layout_all_content = QHBoxLayout()
        self.layout_all_content.setSpacing(0)
        self.layout_all_content.setContentsMargins(0, 0, 0, 0)

        self.stacked_frames = QStackedWidget()

        self.set_menu()
        self.set_pages()

        self.all_content.setLayout(self.layout_all_content)
        self.setCentralWidget(self.all_content)

        self.set_up_listener()

    def set_menu(self):
        self.side_menu = SideMenu(
            parent=self.all_content, on_change_page=self.stacked_frames.setCurrentIndex
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
    new_message = pyqtSignal(Message)


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
