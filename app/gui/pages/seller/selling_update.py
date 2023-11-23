from PyQt5.QtWidgets import QWidget, QLabel, QBoxLayout

from app.gui.components.common import TopPage, Widget
from app.gui.components.organization import VerticalLayout
from app.gui.signals import AppSignals
from app.types_.dicts.selling import TreatedObjectProgression
from app.types_.models.common import BotInfo


class SellingUpdate(QWidget):
    def __init__(self, bot_info: BotInfo, app_signals: AppSignals, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.bot_info = bot_info
        self.app_signals = app_signals

        self.main_frame_layout = VerticalLayout()

        self.set_header()
        self.setup_content()

        self.setLayout(self.main_frame_layout)

        self.app_signals.on_leaving_hdv.connect(self.clear_progression)
        self.app_signals.on_new_hdv_update_progression.connect(self.update_progression)
        self.app_signals.on_new_selling_hdv_update_playing_value.connect(self.update_state_buttons)

    def clear_progression(self):
        self.progression_label.setText("")

    def set_header(self):
        self.header = TopPage(parent=self, title="Mettre à jour les prix")
        self.header.button_play.clicked.connect(lambda: self.on_update_do_play(True))
        self.header.button_stop.clicked.connect(lambda: self.on_update_do_play(False))
        self.main_frame_layout.addWidget(self.header)
        self.update_state_buttons()

    def setup_content(self):
        self.widget_content = Widget(parent=self)

        self.layout_content = VerticalLayout(without_space=False, without_margins=False)
        self.layout_content.addStretch()
        self.layout_content.setDirection(QBoxLayout.Direction.BottomToTop)
        self.widget_content.setLayout(self.layout_content)

        self.setup_progression()

        self.main_frame_layout.addWidget(self.widget_content)

    def setup_progression(self):
        self.progression_label = QLabel(parent=self.widget_content)
        self.layout_content.addWidget(self.progression_label)

    def update_state_buttons(self):
        self.header.do_play(self.bot_info.selling_info.is_playing_update_event.is_set())

    def on_update_do_play(self, do_play: bool):
        if do_play and not self.bot_info.selling_info.is_playing_from_inventory_event.is_set():
            self.bot_info.selling_info.is_playing_update_event.set()
        else:
            self.bot_info.selling_info.is_playing_update_event.clear()
        self.update_state_buttons()

    def update_progression(self, progression: TreatedObjectProgression):
        self.progression_label.setText(f"{progression['treated_objects_count']} / {progression['total_objects_count']}")
