from PyQt5.QtCore import QObject, Qt, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QTableWidgetItem, QVBoxLayout
from qfluentwidgets import BodyLabel

from app.database.models import CategoryEnum
from app.database.queries import get_benefit_from_craft
from app.database.utils import SessionLocal
from app.gui.components.common import QWidget
from app.gui.components.table import BaseTableWidget, ColumnInfo
from app.gui.utils import Worker, run_in_background
from app.utils.debugger import timeit


class BenefitRecipeTableSignals(QObject):
    new_benefit_recipes = pyqtSignal(list)


class BenefitRecipeTable(QWidget):
    def __init__(self):
        super().__init__()
        self.signals = BenefitRecipeTableSignals()
        self.thread_benefit: QThread | None = None
        self.worker_benefit: Worker | None = None

        self.signals.new_benefit_recipes.connect(self.on_new_benefit_recipes)
        self.server_id: int | None = None
        self.setLayout(QVBoxLayout(self))
        self.layout().setAlignment(Qt.AlignTop)

        title = BodyLabel(parent=self, text="Meilleur bénéfice sur les crafts")
        self.layout().addWidget(title)

        table_benefit_recipe_scroll = BaseTableWidget()
        table_benefit_recipe_scroll.set_columns(
            [
                ColumnInfo(name="Nom", search_type=None),
                ColumnInfo(name="Bénéfice", search_type=None),
            ]
        )
        self.table_benefit_recipe = table_benefit_recipe_scroll.table
        self.layout().addWidget(self.table_benefit_recipe)

    @timeit
    def get_benefits_recipes(
        self, category: CategoryEnum, type_name: str | None = None
    ):
        def _get_benefits_recipes():
            with SessionLocal() as session:
                benefits_recipes = get_benefit_from_craft(
                    session, self.server_id, category, type_name, 40
                )
            return benefits_recipes

        self.thread_benefit, self.worker_benefit = run_in_background(
            _get_benefits_recipes
        )
        self.worker_benefit.signals.function_result.connect(
            self.signals.new_benefit_recipes.emit
        )

    @pyqtSlot(list)
    def on_new_benefit_recipes(self, benefit_recipes: list):
        self.table_benefit_recipe.clearContents()
        self.table_benefit_recipe.setRowCount(0)
        self.table_benefit_recipe.setRowCount(len(benefit_recipes))
        for index, (name, benefit) in enumerate(benefit_recipes):
            name_col = QTableWidgetItem(name)
            benefit_col = QTableWidgetItem(str(benefit))

            self.table_benefit_recipe.setItem(index, 0, name_col)
            self.table_benefit_recipe.setItem(index, 1, benefit_col)
