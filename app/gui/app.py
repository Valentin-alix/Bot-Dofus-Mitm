import os.path
from pathlib import Path

from PyQt5.QtCore import (
    QObject,
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
from app.gui.pages.fm.fm_frame import FmFrame
from app.gui.pages.scrapping.scrapping_frame import ScrappingFrame
from app.gui.pages.seller.seller_frame import SellerFrame
from app.gui.pages.sniffer.sniffer_frame import SnifferFrame
from app.gui.signals import AppSignals
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
    on_new_frames = pyqtSignal()


class MainWindow(QMainWindow):
    BASE_WIDTH = 1600
    BASE_HEIGHT = 900

    def __init__(
            self,
            bot_info: BotInfo,
            app_signals: AppSignals,
            only_sniffer: bool = False,
            *args,
            **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.app_signals = app_signals
        self.only_sniffer = only_sniffer
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

    def set_menu(self):
        self.side_menu = SideMenu(parent=self)
        self.layout_all_content.addWidget(self.side_menu)

    def set_pages(self):
        self.frame_sniffer = SnifferFrame(name="Sniffer", bot_info=self.bot_info)
        self.stacked_frames.addWidget(self.frame_sniffer)
        
        if not self.only_sniffer:
            self.frame_scrapping = ScrappingFrame(name="Scraping", bot_info=self.bot_info)
            self.stacked_frames.addWidget(self.frame_scrapping)

            self.frame_seller = SellerFrame(name="Vendeur", bot_info=self.bot_info)
            self.stacked_frames.addWidget(self.frame_seller)

            self.frame_fm = FmFrame(name="Fm", bot_info=self.bot_info)
            self.stacked_frames.addWidget(self.frame_fm)

        self.layout_all_content.addWidget(self.stacked_frames)

    def closeEvent(self, _: QCloseEvent):
        self.app_signals.close.emit()
