from PyQt5.QtWidgets import QTabWidget

from app.database.models import get_engine
from app.gui.components.common import Frame, TopPage
from app.gui.components.organization import VerticalLayout
from app.gui.pages.scrapping.scrapping_craft_tab.scrapping_craft import ScrappingCraft
from app.gui.pages.scrapping.scrapping_presentation_tab.scrapping_presentation import ScrappingPresentation
from app.gui.pages.scrapping.scrapping_progression import ScrappingProgression
from app.gui.signals import AppSignals
from app.types_.models.common import BotInfo


class ScrappingFrame(Frame):
    def __init__(self, bot_info: BotInfo, app_signals: AppSignals, *args, **kwargs):
        super().__init__(*args, **kwargs)
        engine = get_engine()
        self.bot_info = bot_info
        self.app_signals = app_signals

        self.layout = VerticalLayout()
        self.setLayout(self.layout)

        self.set_header()

        self.remaining_content = ScrappingProgression(parent=self, bot_info=self.bot_info)
        self.remaining_content.hide()
        self.layout.addWidget(self.remaining_content)

        self.tabs = QTabWidget()
        self.scrapping_presentation_tab = ScrappingPresentation(bot_info, app_signals, engine)
        self.tabs.addTab(self.scrapping_presentation_tab, "Présentation")
        self.scrapping_craft_tab = ScrappingCraft(bot_info, app_signals, engine)
        self.tabs.addTab(self.scrapping_craft_tab, "Craft")
        self.layout.addWidget(self.tabs)

        self.app_signals.on_leaving_hdv.connect(self.remaining_content.hide)
        self.app_signals.on_new_buying_hdv_playing_value.connect(
            lambda: self.on_update_do_play_scrapping(self.bot_info.scraping_info.is_playing_event.is_set()))
        self.app_signals.on_new_scraping_current_state.connect(self.remaining_content.update_content)

    def set_header(self):
        self.header = TopPage(parent=self)
        self.header.do_play(self.bot_info.scraping_info.is_playing_event.is_set())
        self.header.button_play.clicked.connect(
            lambda: self.on_update_do_play_scrapping(True)
        )
        self.header.button_stop.clicked.connect(
            lambda: self.on_update_do_play_scrapping(False)
        )

        self.layout.addWidget(self.header)

    def on_update_do_play_scrapping(self, do_play: bool):
        if do_play:
            self.bot_info.scraping_info.is_playing_event.set()
        else:
            self.bot_info.scraping_info.is_playing_event.clear()
        self.header.do_play(do_play)
