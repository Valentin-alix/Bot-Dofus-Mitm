from PyQt5.QtWidgets import QHBoxLayout
from qfluentwidgets import ComboBox

from app.database.models import CategoryEnum
from app.database.queries import get_items, get_types_items
from app.database.utils import SessionLocal
from app.gui.components.common import QWidget


class ChartFilters(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.categories = [
            (CategoryEnum.RESOURCES, "Ressources"),
            (CategoryEnum.EQUIPMENT, "Equipements"),
            (CategoryEnum.CONSUMABLES, "Consommables"),
            (CategoryEnum.COSMETICS, "Cosmétiques"),
        ]
        with SessionLocal() as session:
            self.types = get_types_items(session)
            self.items = get_items(session)

        self.setLayout(QHBoxLayout(self))

        category_combobox = ComboBox(parent=self)
        category_combobox.addItems(category[1] for category in self.categories)
        category_combobox.currentIndexChanged.connect(self.on_select_category)
        self.layout().addWidget(category_combobox)

        self.type_combobox = ComboBox(parent=self)
        self.type_combobox.currentTextChanged.connect(self.on_select_type)
        self.layout().addWidget(self.type_combobox)

        self.item_combobox = ComboBox(parent=self)
        self.layout().addWidget(self.item_combobox)

        self.on_select_category(0)

    def on_select_category(self, index):
        category = CategoryEnum(self.categories[index][0])
        self.type_combobox.clear()
        self.item_combobox.clear()
        self.type_combobox.addItem("")
        self.type_combobox.addItems(
            [_type.name for _type in self.types if _type.category == category]
        )

    def on_select_type(self, type_name):
        _type = next((_type for _type in self.types if _type.name == type_name), None)
        if _type is not None:
            self.item_combobox.clear()
            self.item_combobox.addItem("")
            self.item_combobox.addItems(
                [item.name for item in self.items if item.type_item_id == _type.id]
            )
