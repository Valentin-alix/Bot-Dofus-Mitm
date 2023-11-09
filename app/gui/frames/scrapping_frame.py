from gui.components import (
    Frame,
    GroupBox,
    Header,
    VerticalLayout,
)
from modules.hdv.buying_hdv import BuyingHdv
from PyQt5.QtCore import (
    Qt,
    QTimer,
)
from PyQt5.QtWidgets import (
    QBoxLayout,
    QLabel,
)
from types_.interface import ThreadsInfos


class ScrappingFrame(Frame):
    def __init__(self, threads_infos: ThreadsInfos, name: str) -> None:
        super().__init__(name)
        self.buying_hdv: BuyingHdv | None = None
        self.threads_infos = threads_infos

        self.main_frame_layout = VerticalLayout()

        self.set_header()
        self.setup_content()

        self.setLayout(self.main_frame_layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_buying_hdv)
        self.timer.start(300)

    def set_header(self):
        self.header = Header()
        self.header.do_play(self.threads_infos.get("event_play_hdv_scrapping").is_set())
        self.header.button_play.clicked.connect(
            lambda: self.on_update_do_play_scrapping(True)
        )
        self.header.button_stop.clicked.connect(
            lambda: self.on_update_do_play_scrapping(False)
        )
        self.main_frame_layout.addWidget(self.header)

    def setup_content(self):
        self.box_content = GroupBox()
        self.box_content.setTitle("Informations")
        self.box_content.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_content = VerticalLayout()
        self.layout_content.setContentsMargins(0, 0, 0, 0)
        self.layout_content.addStretch()
        self.layout_content.setDirection(QBoxLayout.Direction.BottomToTop)
        self.box_content.setLayout(self.layout_content)

        self.label_remaining_objects = QLabel()
        self.label_remaining_objects.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout_content.addWidget(self.label_remaining_objects)

        self.main_frame_layout.addWidget(self.box_content)

    def update_content_buying_hdv(self):
        if self.buying_hdv is not None:
            self.label_remaining_objects.setText(
                f"Nombre d'objets restantes à traiter dans la catégorie : {len(self.buying_hdv.types_object)}\n\
                Nombre de catégories restantes : {len(self.buying_hdv.categories)}"
            )
        else:
            self.label_remaining_objects.setText("")

    def on_update_do_play_scrapping(self, do_play: bool):
        if do_play:
            self.threads_infos["event_play_hdv_scrapping"].set()
        else:
            self.threads_infos["event_play_hdv_scrapping"].clear()
        self.header.do_play(do_play)

    def check_buying_hdv(self):
        with self.threads_infos.get("buying_hdv_with_lock").get("lock"):
            self.buying_hdv = self.threads_infos.get("buying_hdv_with_lock").get(
                "buying_hdv"
            )
        self.update_content_buying_hdv()
