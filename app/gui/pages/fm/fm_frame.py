from PyQt5.QtWidgets import QGridLayout

from app.gui.components.common import Frame, TopPage, Widget
from app.gui.components.organization import VerticalLayout, GridLayout
from app.gui.pages.fm.item import Item
from app.gui.pages.fm.rentability_description import RentabilityDescription
from app.types_.models.common import BotInfo


class FmFrame(Frame):
    header: TopPage
    content_widget: Widget
    content_layout: QGridLayout
    item: Item | None
    rentability_description: RentabilityDescription | None

    def __init__(self, bot_info: BotInfo, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.bot_info = bot_info
        self.layout = VerticalLayout()
        self.setLayout(self.layout)
        self.set_header()
        self.set_content()

    def set_header(self):
        self.header = TopPage(parent=self)
        self.header.button_play.clicked.connect(lambda: self.on_update_do_play(True))
        self.header.button_stop.clicked.connect(lambda: self.on_update_do_play(False))
        self.layout.addWidget(self.header)
        self.update_state_buttons()

    def update_state_buttons(self):
        self.header.do_play(self.bot_info.fm_info.is_playing_event.is_set())

    def on_update_do_play(self, do_play: bool):
        if do_play:
            self.bot_info.fm_info.is_playing_event.set()
        else:
            self.bot_info.fm_info.is_playing_event.clear()
        self.update_state_buttons()

    def set_content(self):
        self.content_widget = Widget(parent=self)
        self.layout.addWidget(self.content_widget)

        self.content_layout = GridLayout()
        self.content_widget.setLayout(self.content_layout)

        self.item = Item(name="Amulette truc", parent=self.content_widget)
        self.content_layout.addWidget(self.item, 0, 0)

        self.rentability_description = RentabilityDescription(parent=self.content_widget)
        self.content_layout.addWidget(self.rentability_description, 0, 1)

        self.content_layout.setColumnStretch(0, 1)
        self.content_layout.setColumnStretch(1, 1)

        self.content_layout.setRowStretch(2, 2)
