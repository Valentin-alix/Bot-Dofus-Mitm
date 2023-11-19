from PyQt5.QtWidgets import QLabel

from app.gui.components.common import Widget
from app.gui.components.organization import HorizontalLayout
from app.types_.dicts.scraping import ScrapingCurrentState
from app.types_.models.common import BotInfo


class RemainingContent(Widget):
    def __init__(self, bot_info: BotInfo, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot_info = bot_info
        layout = HorizontalLayout()
        self.setLayout(layout)

        self.label_remaining_objects = QLabel(parent=self)
        layout.addWidget(self.label_remaining_objects)

        self.label_remaining_categories = QLabel(parent=self)
        layout.addWidget(self.label_remaining_categories)

    def update_content(self, scrapping_current_state: ScrapingCurrentState):
        self.label_remaining_objects.setText(
            f"Nombre d'objets restants à traiter dans la catégorie : {scrapping_current_state['object_remaining']}"
        )
        self.label_remaining_categories.setText(
            f"Nombre de catégories restantes : {scrapping_current_state['category_remaining']}"
        )
        self.show()
