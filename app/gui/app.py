from queue import Empty, Queue
from threading import Event
from time import sleep
from typing import Callable, Dict, Optional, Type

from gui.components import HorizontalLayout
from gui.frames.hdv_frame import HDVFrame
from gui.frames.sniffer_frame import SnifferFrame
from gui.fragments import SideMenu
from network.models.message import Message
from PyQt5.QtCore import (
    QEvent,
    QObject,
    QRunnable,
    QSize,
    QTimer,
    Qt,
    QThreadPool,
    pyqtSignal,
)
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

from types_ import ThreadsInfos, ParsedMessage
from types_.constants import GAME_SERVER


TITLE = "Bot Dofus"


class Application(QApplication):
    def __init__(self, argv) -> None:
        super().__init__(argv)
        apply_stylesheet(self, theme="dark_teal.xml")
        self.setApplicationName(TITLE)
        self.setStyle("Fusion")


class Signals(QObject):
    on_change_frame = pyqtSignal()


class MainWindow(QMainWindow):
    BASE_WIDTH = 1200
    BASE_HEIGHT = 900

    frame_bot_hdv: HDVFrame

    def __init__(
        self,
        threads_infos: ThreadsInfos,
    ) -> None:
        super().__init__()
        self.threads_infos = threads_infos
        self.signals = Signals()

        self.setWindowTitle(TITLE)
        self.resize(self.BASE_WIDTH, self.BASE_HEIGHT)
        self.show()

        self.all_content = QWidget()
        self.layout_all_content = HorizontalLayout()
        self.layout_all_content.setSpacing(0)
        self.layout_all_content.setDirection(QBoxLayout.Direction.RightToLeft)

        self.stacked_frames = QStackedWidget()

        self.set_pages()
        self.set_menu()

        self.all_content.setLayout(self.layout_all_content)
        self.setCentralWidget(self.all_content)

        self.timer_check_is_connected = QTimer(self)
        self.timer_check_is_connected.timeout.connect(self.on_connection_server)
        self.timer_check_is_connected.start(500)

    def on_connection_server(self):
        try:
            if self.threads_infos.get("event_connected").is_set():
                self.frame_bot_hdv = HDVFrame(
                    threads_infos=self.threads_infos, name="Bot HDV"
                )
                self.stacked_frames.addWidget(self.frame_bot_hdv)
                self.signals.on_change_frame.emit()
                self.timer_check_is_connected.stop()
        except Empty:
            pass

    def set_menu(self):
        self.side_menu = SideMenu(parent=self)
        self.layout_all_content.addWidget(self.side_menu)

    def set_pages(self):
        self.frame_sniffer = SnifferFrame(
            name="Sniffer", threads_infos=self.threads_infos
        )
        self.stacked_frames.addWidget(self.frame_sniffer)
        self.layout_all_content.addWidget(self.stacked_frames)

    def closeEvent(self, _: QCloseEvent):
        self.threads_infos["event_close"].set()
