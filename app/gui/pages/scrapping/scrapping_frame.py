from PyQt5.QtWidgets import QTabWidget

from app.database.models import get_engine
from app.gui.components.common import Frame
from app.gui.components.organization import VerticalLayout
from app.gui.pages.scrapping.scrapping_craft_tab.scrapping_craft import ScrappingCraft
from app.gui.pages.scrapping.scrapping_presentation_tab.scrapping_presentation import ScrappingPresentation
from app.gui.signals import AppSignals
from app.types_.models.common import BotInfo


class ScrappingFrame(Frame):
    def __init__(self, bot_info: BotInfo, app_signals: AppSignals, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = VerticalLayout()
        self.setLayout(self.layout)
        self.tabs = QTabWidget()

        engine = get_engine()

        self.scrapping_presentation_tab = ScrappingPresentation(bot_info, app_signals, engine)
        self.tabs.addTab(self.scrapping_presentation_tab, "Présentation")

        self.scrapping_craft_tab = ScrappingCraft(bot_info, app_signals, engine)
        self.tabs.addTab(self.scrapping_craft_tab, "Craft")

        self.layout.addWidget(self.tabs)
