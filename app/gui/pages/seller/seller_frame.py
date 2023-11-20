from PyQt5.QtWidgets import (
    QLabel,
)

from app.gui.components.common import (
    TopPage,
    Frame, Widget,
)
from app.gui.components.organization import VerticalLayout, HorizontalLayout
from app.gui.pages.seller.selling import Selling
from app.gui.signals import AppSignals
from app.types_.models.common import BotInfo


class SellerFrame(Frame):
    header: TopPage
    widget_content: Widget
    layout_content: VerticalLayout
    label_number_on_sale: QLabel
    label_sum_on_sale: QLabel

    def __init__(self, bot_info: BotInfo, app_signals: AppSignals, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.bot_info = bot_info
        self.app_signals = app_signals

        self.main_layout = HorizontalLayout()
        self.setLayout(self.main_layout)

        self.selling = Selling(self.bot_info, self.app_signals)
        self.main_layout.addWidget(self.selling)
