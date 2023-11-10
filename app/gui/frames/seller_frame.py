from app.gui.components import (
    Frame,
    GroupBox,
    Header,
    VerticalLayout,
)
from PyQt5.QtCore import (
    Qt,
)
from PyQt5.QtWidgets import (
    QBoxLayout,
    QLabel,
)
from app.types_ import ThreadsInfos


class SellerFrame(Frame):
    def __init__(self, threads_infos: ThreadsInfos, name: str) -> None:
        super().__init__(name)
        self.threads_infos = threads_infos

        self.main_frame_layout = VerticalLayout()

        self.set_header()
        self.setup_content()

        self.setLayout(self.main_frame_layout)

    def set_header(self):
        self.header = Header()
        self.header.button_play.clicked.connect(lambda: self.on_update_do_play(True))
        self.header.button_stop.clicked.connect(lambda: self.on_update_do_play(False))
        self.main_frame_layout.addWidget(self.header)
        self.update_state_buttons()

    def setup_content(self):
        self.box_content = GroupBox()
        self.box_content.setTitle("Objects mis en vente")
        self.box_content.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_content = VerticalLayout()
        self.layout_content.setContentsMargins(0, 0, 0, 0)
        self.layout_content.addStretch()
        self.layout_content.setDirection(QBoxLayout.Direction.BottomToTop)
        self.box_content.setLayout(self.layout_content)

        self.main_frame_layout.addWidget(self.box_content)

    def on_new_object_for_sale(self):
        label_sellable_objects = QLabel()
        label_sellable_objects.setText("bientot")
        label_sellable_objects.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout_content.addWidget(self.label_sellable_objects)

    def update_state_buttons(self):
        self.header.do_play(self.threads_infos.get("event_play_hdv_selling").is_set())

    def on_update_do_play(self, do_play: bool):
        if do_play:
            self.threads_infos["event_play_hdv_selling"].set()
            self.update_state_buttons()
        else:
            self.threads_infos["event_play_hdv_selling"].clear()
            self.update_state_buttons()
