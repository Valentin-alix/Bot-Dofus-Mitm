from PyQt5.QtCore import (
    QObject,
    pyqtSignal,
)
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import (
    QApplication,
)
from qfluentwidgets import FluentIcon, FluentWindow

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


class Signals(QObject):
    on_new_frames = pyqtSignal()


class MainWindow(FluentWindow):
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
        self.app_signals = app_signals
        self.only_sniffer = only_sniffer
        self.bot_info = bot_info
        self.signals = Signals()

        self.init_window()
        self.init_nagivation()

    def init_window(self):
        self.setWindowTitle(TITLE)
        self.resize(self.BASE_WIDTH, self.BASE_HEIGHT)

    def init_nagivation(self):
        # sniffer
        self.sniffer_interface = SnifferFrame(
            bot_info=self.bot_info, app_signals=self.app_signals
        )
        self.sniffer_interface.setObjectName("sniffer")
        self.addSubInterface(self.sniffer_interface, FluentIcon.SEARCH, "Sniffer")

        if not self.only_sniffer:
            # scrapping
            self.scrapping_interface = ScrappingFrame(
                bot_info=self.bot_info, app_signals=self.app_signals
            )
            self.scrapping_interface.setObjectName("scapping")
            self.addSubInterface(
                self.scrapping_interface, FluentIcon.PIE_SINGLE, "Scrapping"
            )

            # seller
            self.seller_interface = SellerFrame(
                bot_info=self.bot_info, app_signals=self.app_signals
            )
            self.seller_interface.setObjectName("seller")
            self.addSubInterface(self.seller_interface, FluentIcon.MARKET, "Seller")

    def closeEvent(self, _: QCloseEvent):
        self.app_signals.on_close.emit()
