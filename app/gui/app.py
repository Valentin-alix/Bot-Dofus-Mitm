import os.path
from pathlib import Path
from queue import Empty

from PyQt5.QtCore import (
    QObject,
    QTimer,
    pyqtSignal,
)
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import (
    QApplication,
    QBoxLayout,
    QMainWindow,
    QStackedWidget,
    QWidget,
)

from app.gui.components.organization import HorizontalLayout
from app.gui.fragments import SideMenu, DarkThemePalette
from app.gui.frames.scrapping.scrapping_frame import ScrappingFrame
from app.gui.frames.seller_frame import SellerFrame
from app.gui.frames.sniffer_frame import SnifferFrame
from app.types_ import BotInfo

TITLE = "Bot Dofus"


class Application(QApplication):
    def __init__(self, argv) -> None:
        super().__init__(argv)
        self.setApplicationName(TITLE)
        self.setStyle("Fusion")
        self.setPalette(DarkThemePalette())
        with open(os.path.join(Path(__file__).parent, "styles.qss"), "r") as file:
            style = file.read()
            self.setStyleSheet(style)


class Signals(QObject):
    on_change_frame = pyqtSignal()


class MainWindow(QMainWindow):
    BASE_WIDTH = 1600
    BASE_HEIGHT = 900

    frame_bot_scrapping: ScrappingFrame
    frame_bot_seller: SellerFrame

    def __init__(
            self,
            bot_info: BotInfo,
            *args,
            **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.bot_info = bot_info
        self.signals = Signals()

        self.setWindowTitle(TITLE)
        self.resize(self.BASE_WIDTH, self.BASE_HEIGHT)
        self.show()

        self.all_content = QWidget(parent=self)
        self.layout_all_content = HorizontalLayout()
        self.layout_all_content.setDirection(QBoxLayout.Direction.RightToLeft)
        self.all_content.setLayout(self.layout_all_content)

        self.stacked_frames = QStackedWidget(parent=self.all_content)

        self.set_pages()
        self.set_menu()

        self.setCentralWidget(self.all_content)

        self.timer_check_is_connected = QTimer(self)
        self.timer_check_is_connected.timeout.connect(self.on_connection_server)
        self.timer_check_is_connected.start(500)

    def on_connection_server(self):
        try:
            if self.bot_info.common_info.is_connected_event.is_set():
                self.frame_bot_scrapping = ScrappingFrame(
                    parent=self, bot_info=self.bot_info, name="Bot Scrapping"
                )
                self.stacked_frames.addWidget(self.frame_bot_scrapping)
                self.frame_bot_seller = SellerFrame(
                    parent=self, bot_info=self.bot_info, name="Bot Vendeur"
                )
                self.stacked_frames.addWidget(self.frame_bot_seller)
                self.signals.on_change_frame.emit()
                self.timer_check_is_connected.stop()
        except Empty:
            pass

    def set_menu(self):
        self.side_menu = SideMenu(parent=self)
        self.layout_all_content.addWidget(self.side_menu)

    def set_pages(self):
        self.frame_sniffer = SnifferFrame(name="Sniffer", bot_info=self.bot_info)
        self.stacked_frames.addWidget(self.frame_sniffer)
        self.layout_all_content.addWidget(self.stacked_frames)

    def closeEvent(self, _: QCloseEvent):
        self.bot_info.common_info.is_closed_event.set()
