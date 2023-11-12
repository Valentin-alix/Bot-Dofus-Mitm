import matplotlib
from PyQt5.QtWidgets import (
    QWidget,
    QComboBox,
)
from sqlalchemy import Engine

from app.database.models import get_engine, CategoryEnum
from app.gui.components.organization import VerticalLayout, HorizontalLayout
from app.utils import get_info_by_type_or_object, get_type, get_items

matplotlib.use("Qt5Agg")

import pandas as pd
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, width=5, height=5, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(MplCanvas, self).__init__(self.fig)
        self.axes = self.fig.add_subplot(111)

    def show(self, df_info: pd.DataFrame):
        self.axes.cla()
        self.axes.set_xlabel("Date de création")
        self.axes.set_ylabel(f"Prix par 1, 10 et 100")

        self.axes.plot(df_info["creation_date"], df_info["hundred"], label="100")
        self.axes.plot(df_info["creation_date"], df_info["ten"], label="10")
        self.axes.plot(df_info["creation_date"], df_info["one"], label="1")

        self.axes.legend()
        self.draw()


class ChartItems(QWidget):
    def __init__(self, engine: Engine, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.engine = engine
        self.chart_layout = VerticalLayout()
        self.setLayout(self.chart_layout)

        self.categories = [
            (CategoryEnum.RESOURCES, "Ressources"),
            (CategoryEnum.EQUIPMENT, "Equipements"),
            (CategoryEnum.CONSUMABLES, "Consommables"),
            (CategoryEnum.COSMETICS, "Cosmétiques"),
        ]
        self.types = get_type(self.engine)
        self.items = get_items(self.engine)

        self.set_header()

        self.canvas = MplCanvas()
        self.chart_layout.addWidget(self.canvas)

    def set_header(self):
        self.widget_header = QWidget(parent=self)
        self.chart_layout.addWidget(self.widget_header)
        self.layout_h = HorizontalLayout()
        self.widget_header.setLayout(self.layout_h)

        category_combobox = QComboBox(parent=self.widget_header)
        category_combobox.addItems(category[1] for category in self.categories)
        category_combobox.currentIndexChanged.connect(self.on_select_category)
        self.layout_h.addWidget(category_combobox)

        self.type_combobox = QComboBox(parent=self.widget_header)
        self.type_combobox.currentTextChanged.connect(self.on_select_type)
        self.layout_h.addWidget(self.type_combobox)

        self.item_combobox = QComboBox(parent=self.widget_header)
        self.item_combobox.currentTextChanged.connect(self.on_select_item)
        self.layout_h.addWidget(self.item_combobox)

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

    def on_select_item(self, item_name):
        if item_name != "":
            df_info = get_info_by_type_or_object(get_engine(), object_name=item_name)
            self.canvas.show(df_info)
