from PyQt5.QtWidgets import QWidget, QLabel

from app.gui.components.organization import HorizontalLayout
from app.types_ import BotInfo


class RemainingContent(QWidget):
    def __init__(self, bot_info: BotInfo, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot_info = bot_info
        layout = HorizontalLayout()
        self.setLayout(layout)

        self.label_remaining_objects = QLabel(parent=self)
        layout.addWidget(self.label_remaining_objects)

        self.label_remaining_categories = QLabel(parent=self)
        layout.addWidget(self.label_remaining_categories)

    def update_content(self):
        with self.bot_info.scraping_info.buying_hdv_with_lock.get("lock"):
            if (buying_hdv := self.bot_info.scraping_info.buying_hdv_with_lock["buying_hdv"]) is not None:
                self.label_remaining_objects.setText(
                    f"Nombre d'objets restants à traiter dans la catégorie : {len(buying_hdv.types_object)}"
                )
                self.label_remaining_categories.setText(
                    f"Nombre de catégories restantes : {len(buying_hdv.categories)}"
                )
                self.show()
            else:
                self.label_remaining_objects.setText("")
                self.label_remaining_categories.setText("")
                self.hide()
