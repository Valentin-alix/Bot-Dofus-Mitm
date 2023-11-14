from PyQt5.QtCore import (
    Qt,
)
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
    def __init__(self, bot_info: BotInfo, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.bot_info = bot_info

        self.main_frame_layout = VerticalLayout()

        self.set_header()
        self.setup_content()

        self.setLayout(self.main_frame_layout)

    def set_header(self):
        self.header = Header(parent=self)
        self.header.button_play.clicked.connect(lambda: self.on_update_do_play(True))
        self.header.button_stop.clicked.connect(lambda: self.on_update_do_play(False))
        self.main_frame_layout.addWidget(self.header)
        self.update_state_buttons()

    def setup_content(self):
        self.box_content = GroupBox(parent=self)
        self.box_content.setTitle("Objets mis en vente")
        self.box_content.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_content = VerticalLayout()
        self.layout_content.setContentsMargins(0, 0, 0, 0)
        self.layout_content.addStretch()
        self.layout_content.setDirection(QBoxLayout.Direction.BottomToTop)
        self.box_content.setLayout(self.layout_content)

        self.main_frame_layout.addWidget(self.box_content)

    def on_new_object_for_sale(self):
        self.label_sellable_objects = QLabel(parent=self.box_content)
        self.label_sellable_objects.setText("bientot")
        self.label_sellable_objects.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout_content.addWidget(self.label_sellable_objects)

    def update_state_buttons(self):
        self.header.do_play(self.bot_info.selling_info.is_playing_event.is_set())

    def on_update_do_play(self, do_play: bool):
        if do_play:
            self.bot_info.selling_info.is_playing_event.set()
        else:
            self.bot_info.selling_info.is_playing_event.clear()
        self.update_state_buttons()
