import matplotlib
from PyQt5.QtWidgets import (
    QComboBox,
)
from sqlalchemy import Engine

from app.database.models import CategoryEnum
from app.gui.components.common import Widget
from app.gui.components.organization import VerticalLayout, HorizontalLayout
from app.types_.models.common import BotInfo
from app.utils import get_info_by_type_or_object, get_type, get_items

matplotlib.use("Qt5Agg")

import pandas as pd
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class ChartContent(FigureCanvasQTAgg):
    def __init__(self, width=5, height=5, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(ChartContent, self).__init__(self.fig)
        self.axes = self.fig.add_subplot(111)

    def show(self, df_info: pd.DataFrame):
        self.axes.cla()
        self.axes.set_xlabel("Date de création")
        self.axes.set_ylabel("Prix par 1, 10 et 100")

        self.axes.plot(df_info["creation_date"], df_info["hundred"], label="100")
        self.axes.plot(df_info["creation_date"], df_info["ten"], label="10")
        self.axes.plot(df_info["creation_date"], df_info["one"], label="1")

        self.axes.legend()
        self.draw()


class ChartFilters(Widget):
    def __init__(self, parent: 'Chart', engine: Engine, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.engine = engine
        self.categories = [
            (CategoryEnum.RESOURCES, "Ressources"),
            (CategoryEnum.EQUIPMENT, "Equipements"),
            (CategoryEnum.CONSUMABLES, "Consommables"),
            (CategoryEnum.COSMETICS, "Cosmétiques"),
        ]
        self.types = get_type(self.engine)
        self.items = get_items(self.engine)

        self.layout = HorizontalLayout()
        self.setLayout(self.layout)

        category_combobox = QComboBox(parent=self)
        category_combobox.addItems(category[1] for category in self.categories)
        category_combobox.currentIndexChanged.connect(self.on_select_category)
        self.layout.addWidget(category_combobox)

        self.type_combobox = QComboBox(parent=self)
        self.type_combobox.currentTextChanged.connect(self.on_select_type)
        self.layout.addWidget(self.type_combobox)

        self.item_combobox = QComboBox(parent=self)
        self.item_combobox.currentTextChanged.connect(parent.on_select_item)
        self.layout.addWidget(self.item_combobox)

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


class Chart(Widget):
    def __init__(self, engine: Engine, bot_info: BotInfo, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.engine = engine
        self.bot_info = bot_info
        self.server_id: int | None = None

        self.layout = VerticalLayout()
        self.setLayout(self.layout)

        self.filters = ChartFilters(parent=self, engine=self.engine)
        self.layout.addWidget(self.filters)

        self.canvas = ChartContent()
        self.layout.addWidget(self.canvas)

    def on_select_item(self, item_name: str):
        if item_name != "":
            df_info = get_info_by_type_or_object(engine=self.engine, server_id=self.server_id,
                                                 object_name=item_name)
            if df_info is not None:
                self.canvas.show(df_info)
