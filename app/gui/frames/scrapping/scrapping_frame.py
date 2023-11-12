from PyQt5.QtCore import (
    Qt,
    QTimer,
)
from PyQt5.QtWidgets import (
    QBoxLayout,
    QLabel,
    QWidget,
)

from app.database.models import get_engine
from app.gui.components.common import (
    Header,
    GroupBox,
    Frame, ButtonIcon,
)
from app.gui.components.organization import VerticalLayout, HorizontalLayout
from app.gui.frames.scrapping.chart import ChartItems
from app.gui.frames.scrapping.valuable_info import ValuableInfo
from app.modules.hdv.buying_hdv import BuyingHdv
from app.types_.interface import BotInfo


class ScrappingFrame(Frame):
    def __init__(self, bot_info: BotInfo, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.engine = get_engine()

        self.buying_hdv: BuyingHdv | None = None
        self.bot_info = bot_info

        self.main_frame_layout = VerticalLayout()

        self.set_header()
        self.setup_content()

        self.setLayout(self.main_frame_layout)

        self.timer = QTimer(parent=self)
        self.timer.timeout.connect(self.check_buying_hdv)
        self.timer.start(300)

    def set_header(self):
        self.header_widget = QWidget()

        v_layout = VerticalLayout()
        self.header_widget.setLayout(v_layout)

        self.header = Header(parent=self)
        v_layout.addWidget(self.header)
        self.header.do_play(self.bot_info.scraping_info.is_playing_event.is_set())
        self.header.button_play.clicked.connect(
            lambda: self.on_update_do_play_scrapping(True)
        )
        self.header.button_stop.clicked.connect(
            lambda: self.on_update_do_play_scrapping(False)
        )

        self.button_reset = ButtonIcon("restart.svg", parent=self.header)
        self.button_reset.clicked.connect(self.on_reset)
        v_layout.addWidget(self.button_reset)

        self.main_frame_layout.addWidget(self.header_widget)

    def on_reset(self):
        self.chart.on_select_item(self.chart.item_combobox.currentText())
        self.valuable_info.on_reset()

    def setup_content(self):
        self.box_content = GroupBox(parent=self, with_title=False)
        self.box_content.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_content = VerticalLayout()
        self.layout_content.setContentsMargins(0, 0, 0, 0)
        self.layout_content.setDirection(QBoxLayout.Direction.BottomToTop)
        self.box_content.setLayout(self.layout_content)

        self.set_remaining_content()

        self.valuable_info = ValuableInfo(parent=self.box_content, engine=self.engine)
        self.layout_content.addWidget(self.valuable_info)

        self.chart = ChartItems(parent=self.box_content, engine=self.engine)
        self.layout_content.addWidget(self.chart)

        self.layout_content.addWidget(self.widget_remaining_objects)
        self.main_frame_layout.addWidget(self.box_content)

    def set_remaining_content(self):
        self.widget_remaining_objects = QWidget(parent=self.box_content)
        self.layout_remaining_objects = HorizontalLayout()
        self.widget_remaining_objects.setLayout(self.layout_remaining_objects)

        self.label_remaining_objects = QLabel(parent=self.widget_remaining_objects)
        self.label_remaining_objects.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout_remaining_objects.addWidget(self.label_remaining_objects)

        self.label_remaining_categories = QLabel(parent=self.widget_remaining_objects)
        self.label_remaining_categories.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout_remaining_objects.addWidget(self.label_remaining_categories)

        self.widget_remaining_objects.hide()

    def update_content_buying_hdv(self):
        if self.buying_hdv is not None:
            self.label_remaining_objects.setText(
                f"Nombre d'objets restants à traiter dans la catégorie : {len(self.buying_hdv.types_object)}"
            )
            self.label_remaining_categories.setText(
                f"Nombre de catégories restantes : {len(self.buying_hdv.categories)}"
            )
            self.widget_remaining_objects.show()
        else:
            self.label_remaining_objects.setText("")
            self.label_remaining_categories.setText("")
            self.widget_remaining_objects.hide()

    def on_update_do_play_scrapping(self, do_play: bool):
        if do_play:
            self.bot_info.scraping_info.is_playing_event.set()
        else:
            self.bot_info.scraping_info.is_playing_event.clear()
        self.header.do_play(do_play)

    def check_buying_hdv(self):
        with self.bot_info.scraping_info.buying_hdv_with_lock.get("lock"):
            self.buying_hdv = self.bot_info.scraping_info.buying_hdv_with_lock.get(
                "buying_hdv"
            )
        self.update_content_buying_hdv()
