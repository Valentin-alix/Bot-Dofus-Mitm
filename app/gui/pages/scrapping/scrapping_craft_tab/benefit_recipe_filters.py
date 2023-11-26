from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QComboBox
from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker

from app.database.models import CategoryEnum, TypeItem, Item, Recipe
from app.gui.components.common import Widget
from app.gui.components.organization import VerticalLayout


class BenefitRecipeFilters(Widget):
    class FilterSignals(QObject):
        on_select_type = pyqtSignal(str)
        on_select_category = pyqtSignal(CategoryEnum)

    def __init__(self, engine: Engine):
        super().__init__()
        self.filter_signals = self.FilterSignals()

        v_layout = VerticalLayout()
        self.setLayout(v_layout)

        self.categories = [
            (CategoryEnum.CONSUMABLES, "Consommables"),
            (CategoryEnum.EQUIPMENT, "Equipements"),
            (CategoryEnum.RESOURCES, "Ressources")
        ]
        with sessionmaker(bind=engine)() as session:
            self.types_with_recipe = session.query(Recipe).join(Item, Item.id == Recipe.result_item_id).join(TypeItem,
                                                                                                             TypeItem.id == Item.type_item_id).with_entities(
                TypeItem).order_by(TypeItem.name).all()

        self.combo_category = QComboBox(parent=self)
        self.combo_category.addItems([category[1] for category in self.categories])
        v_layout.addWidget(self.combo_category)

        self.combo_type_item = QComboBox(parent=self)
        v_layout.addWidget(self.combo_type_item)
        self.combo_type_item.currentTextChanged.connect(self.on_select_type)

        self.combo_category.currentIndexChanged.connect(self.on_select_category)

    def on_select_category(self, index: int):
        category = self.categories[index][0]
        self.combo_type_item.clear()
        self.combo_type_item.addItem("")
        self.combo_type_item.addItems(
            type_item.name for type_item in self.types_with_recipe if type_item.category == category)
        self.filter_signals.on_select_category.emit(category)

    def on_select_type(self, type_name: str):
        if type_name != "":
            _type = next(type_item for type_item in self.types_with_recipe if type_item.name == type_name)
            self.filter_signals.on_select_type.emit(_type.name)

    def emit_change(self):
        if (type_name := self.combo_type_item.currentText()) != "":
            self.on_select_type(type_name)
        else:
            self.on_select_category(self.combo_category.currentIndex())
