from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QHBoxLayout
from qfluentwidgets import ComboBox

from app.database.models import CategoryEnum
from app.database.queries import get_recipes
from app.database.utils import SessionLocal
from app.gui.components.common import QWidget


class BenefitRecipeFilters(QWidget):
    class FilterSignals(QObject):
        on_select_type = pyqtSignal(str)
        on_select_category = pyqtSignal(CategoryEnum)

    def __init__(self):
        super().__init__()
        self.filter_signals = self.FilterSignals()

        self.setLayout(QHBoxLayout())

        self.categories = [
            (CategoryEnum.CONSUMABLES, "Consommables"),
            (CategoryEnum.EQUIPMENT, "Equipements"),
            (CategoryEnum.RESOURCES, "Ressources"),
        ]
        with SessionLocal() as session:
            self.types_with_recipe = get_recipes(session)

        self.combo_category = ComboBox(parent=self)
        self.combo_category.addItems([category[1] for category in self.categories])
        self.layout().addWidget(self.combo_category)

        self.combo_type_item = ComboBox(parent=self)
        self.layout().addWidget(self.combo_type_item)
        self.combo_type_item.currentTextChanged.connect(self.on_select_type)

        self.combo_category.currentIndexChanged.connect(self.on_select_category)

    def on_select_category(self, index: int):
        category = self.categories[index][0]
        self.combo_type_item.clear()
        self.combo_type_item.addItem("")
        self.combo_type_item.addItems(
            type_item.name
            for type_item in self.types_with_recipe
            if type_item.category == category
        )
        self.filter_signals.on_select_category.emit(category)

    def on_select_type(self, type_name: str):
        if type_name != "":
            _type = next(
                type_item
                for type_item in self.types_with_recipe
                if type_item.name == type_name
            )
            self.filter_signals.on_select_type.emit(_type.name)

    def emit_change(self):
        if (type_name := self.combo_type_item.currentText()) != "":
            self.on_select_type(type_name)
        else:
            self.on_select_category(self.combo_category.currentIndex())
