import os.path
from pathlib import Path

from PyQt5.QtCore import (
    QObject,
    pyqtSignal, Qt, )
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedWidget,
    QBoxLayout, )

from app.gui.components.common import Widget
from app.gui.components.organization import HorizontalLayout, VerticalLayout
from app.gui.fragments.header import Header
from app.gui.fragments.palette import DarkThemePalette
from app.gui.fragments.side_bar import SideBar
from app.gui.pages.scrapping.scrapping_frame import ScrappingFrame
from app.gui.pages.seller.seller_frame import SellerFrame
from app.gui.pages.sniffer.sniffer_frame import SnifferFrame
from app.gui.signals import AppSignals
from app.types_.models.common import BotInfo

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
    BASE_WIDTH = 1280
    BASE_HEIGHT = 720

    def __init__(
            self,
            bot_info: BotInfo,
            app_signals: AppSignals,
            only_sniffer: bool = False,
            *args,
            **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.setWindowFlag(Qt.FramelessWindowHint)  # to hide topbar
        self.app_signals = app_signals
        self.only_sniffer = only_sniffer
        self.bot_info = bot_info
        self.signals = Signals()

        self.setWindowTitle(TITLE)
        self.resize(self.BASE_WIDTH, self.BASE_HEIGHT)
        self.show()

        self.all_content = Widget(parent=self)
        self.layout_all_content = HorizontalLayout()
        self.layout_all_content.setDirection(QBoxLayout.Direction.RightToLeft)
        self.all_content.setLayout(self.layout_all_content)

        self.main_content = Widget(parent=self)
        self.layout_all_content.addWidget(self.main_content)
        self.main_content_layout = VerticalLayout()
        self.main_content.setLayout(self.main_content_layout)

        self.set_header()
        self.set_pages()
        self.set_menu()

        self.setCentralWidget(self.all_content)

    def set_menu(self):
        self.side_menu = SideBar(parent=self, frames=[
            self.stacked_frames.widget(index)
            for index in range(self.stacked_frames.count())
        ])
        self.layout_all_content.addWidget(self.side_menu)

    def set_header(self):
        self.header = Header(parent=self)
        self.main_content_layout.addWidget(self.header)

    def set_pages(self):
        self.stacked_frames = QStackedWidget(parent=self.all_content)
        self.frame_sniffer = SnifferFrame(name="Sniffer", bot_info=self.bot_info, app_signals=self.app_signals)
        self.stacked_frames.addWidget(self.frame_sniffer)

        if not self.only_sniffer:
            self.frame_scrapping = ScrappingFrame(name="Scraping", bot_info=self.bot_info,
                                                  app_signals=self.app_signals)
            self.stacked_frames.addWidget(self.frame_scrapping)

            self.frame_seller = SellerFrame(name="Vendeur", bot_info=self.bot_info, app_signals=self.app_signals)
            self.stacked_frames.addWidget(self.frame_seller)

        self.main_content_layout.addWidget(self.stacked_frames)

    def closeEvent(self, _: QCloseEvent):
        self.app_signals.on_close.emit()
