from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (
    QBoxLayout,
    QLabel,
)

from app.gui.components.common import (
    GroupBox,
    Header,
    Frame,
)
from app.gui.components.organization import VerticalLayout
from app.types_ import BotInfo


class SellerFrame(Frame):
    header: Header
    box_content: GroupBox
    layout_content: VerticalLayout
    label_number_on_sale: QLabel
    label_sum_on_sale: QLabel

    def __init__(self, bot_info: BotInfo, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.bot_info = bot_info

        self.main_frame_layout = VerticalLayout()

        self.set_header()
        self.setup_content()

        self.setLayout(self.main_frame_layout)

        self.timer = QTimer(parent=self)
        self.timer.timeout.connect(self.check_item_on_sale)
        self.timer.start(300)

    def check_item_on_sale(self):
        self.update_content_selling()

    def set_header(self):
        self.header = Header(parent=self)
        self.header.button_play.clicked.connect(lambda: self.on_update_do_play(True))
        self.header.button_stop.clicked.connect(lambda: self.on_update_do_play(False))
        self.main_frame_layout.addWidget(self.header)
        self.update_state_buttons()

    def setup_content(self):
        self.box_content = GroupBox(parent=self)
        self.box_content.setTitle("Objets mis en vente")

        self.layout_content = VerticalLayout(without_space=False, without_margins=False)
        self.layout_content.addStretch()
        self.layout_content.setDirection(QBoxLayout.Direction.BottomToTop)
        self.box_content.setLayout(self.layout_content)

        self.set_content_selling()

        self.main_frame_layout.addWidget(self.box_content)

    def set_content_selling(self):
        self.label_number_on_sale = QLabel(parent=self.box_content)
        self.layout_content.addWidget(self.label_number_on_sale)

        self.label_sum_on_sale = QLabel(parent=self.box_content)
        self.layout_content.addWidget(self.label_sum_on_sale)

    def update_content_selling(self):
        with self.bot_info.selling_info.on_sale_info_with_lock.get("lock"):
            self.label_number_on_sale.setText(
                f"Nombre de slot utilisé : {self.bot_info.selling_info.on_sale_info_with_lock['number']}")
            self.label_sum_on_sale.setText(
                f"Valeur estimé mis en vente : {self.bot_info.selling_info.on_sale_info_with_lock['sum_price']}")

    def update_state_buttons(self):
        self.header.do_play(self.bot_info.selling_info.is_playing_event.is_set())

    def on_update_do_play(self, do_play: bool):
        if do_play:
            self.bot_info.selling_info.is_playing_event.set()
        else:
            self.bot_info.selling_info.is_playing_event.clear()
        self.update_state_buttons()
