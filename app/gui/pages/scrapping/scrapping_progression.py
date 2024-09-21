from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QWidget
from qfluentwidgets import BodyLabel

from app.interfaces.dicts.scraping import ScrapingCurrentState
from app.interfaces.models.common import BotInfo


class ScrappingProgression(QWidget):
    def __init__(self, bot_info: BotInfo, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot_info = bot_info
        self.h_layout = QHBoxLayout()
        self.h_layout.setSpacing(32)
        self.h_layout.setAlignment(Qt.AlignHCenter)
        self.setLayout(self.h_layout)

        self.label_remaining_objects = BodyLabel(parent=self)
        self.layout().addWidget(self.label_remaining_objects)

        self.label_remaining_categories = BodyLabel(parent=self)
        self.layout().addWidget(self.label_remaining_categories)

    def update_content(self, scrapping_current_state: ScrapingCurrentState):
        self.label_remaining_objects.setText(
            f"Nombre d'objets restants à traiter dans la catégorie : {scrapping_current_state['object_remaining']}"
        )
        self.label_remaining_categories.setText(
            f"Nombre de catégories restantes : {scrapping_current_state['category_remaining']}"
        )
        self.show()
