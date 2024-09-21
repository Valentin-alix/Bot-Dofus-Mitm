from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QVBoxLayout

from app.gui.components.common import QWidget
from app.gui.pages.scrapping.scrapping_craft_tab.benefit_recipe_filters import (
    BenefitRecipeFilters,
)
from app.gui.pages.scrapping.scrapping_craft_tab.benefit_recipe_table import (
    BenefitRecipeTable,
)
from app.gui.signals import AppSignals
from app.interfaces.models.common import BotInfo


class ScrappingCraft(QWidget):
    def __init__(self, bot_info: BotInfo, app_signals: AppSignals):
        super().__init__()
        self.bot_info = bot_info
        self.server_id: int | None = None
        self.setLayout(QVBoxLayout(self))
        self.layout().setAlignment(Qt.AlignTop)

        self.benefit_recipe_filters = BenefitRecipeFilters()
        self.layout().addWidget(self.benefit_recipe_filters)

        self.benefit_recipe_table = BenefitRecipeTable()
        self.layout().addWidget(self.benefit_recipe_table)

        self.benefit_recipe_filters.filter_signals.on_select_category.connect(
            self.benefit_recipe_table.get_benefits_recipes
        )
        self.benefit_recipe_filters.filter_signals.on_select_type.connect(
            self.on_select_type
        )

        app_signals.on_new_server_id.connect(self.on_new_server_id)

    @pyqtSlot(str)
    def on_select_type(self, type_name: str):
        self.benefit_recipe_table.get_benefits_recipes(
            self.benefit_recipe_filters.categories[
                self.benefit_recipe_filters.combo_category.currentIndex()
            ][0],
            type_name,
        )

    @pyqtSlot()
    def on_new_server_id(self) -> None:
        if (server_id := self.bot_info.common_info.server_id) != self.server_id:
            self.server_id = server_id
            self.benefit_recipe_table.server_id = server_id
            self.benefit_recipe_filters.emit_change()
