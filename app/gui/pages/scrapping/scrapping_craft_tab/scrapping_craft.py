from sqlalchemy import Engine

from app.gui.components.common import Widget
from app.gui.components.organization import VerticalLayout
from app.gui.pages.scrapping.scrapping_craft_tab.benefit_recipe_filters import BenefitRecipeFilters
from app.gui.pages.scrapping.scrapping_craft_tab.benefit_recipe_table import BenefitRecipeTable
from app.gui.signals import AppSignals
from app.types_.models.common import BotInfo


class ScrappingCraft(Widget):
    def __init__(self, bot_info: BotInfo, app_signals: AppSignals, engine: Engine):
        super().__init__()
        self.bot_info = bot_info
        self.server_id: int | None = None
        v_layout = VerticalLayout()
        self.setLayout(v_layout)

        self.benefit_recipe_filters = BenefitRecipeFilters(engine)
        v_layout.addWidget(self.benefit_recipe_filters)

        self.benefit_recipe_table = BenefitRecipeTable(engine)
        v_layout.addWidget(self.benefit_recipe_table)

        self.benefit_recipe_filters.filter_signals.on_select_category.connect(
            self.benefit_recipe_table.get_benefit_recipe)
        self.benefit_recipe_filters.filter_signals.on_select_type.connect(
            lambda type_name: self.benefit_recipe_table.get_benefit_recipe(
                self.benefit_recipe_filters.categories[self.benefit_recipe_filters.combo_category.currentIndex()][0],
                type_name))

        app_signals.on_new_server_id.connect(self.on_new_server_id)

    def on_new_server_id(self) -> None:
        if (server_id := self.bot_info.common_info.server_id) != self.server_id:
            self.server_id = server_id
            self.benefit_recipe_table.server_id = server_id
            self.benefit_recipe_filters.emit_change()
