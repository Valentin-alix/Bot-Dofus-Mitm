import matplotlib
import matplotlib.axes
import matplotlib.pyplot
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from qfluentwidgets import ComboBox
from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker

from app.database.models import CategoryEnum, Item, Price, TypeItem
from app.gui.components.common import QWidget
from app.types_.models.common import BotInfo

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


class ChartFilters(QWidget):
    def __init__(self, parent: "Chart", engine: Engine, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.engine = engine
        self.categories = [
            (CategoryEnum.RESOURCES, "Ressources"),
            (CategoryEnum.EQUIPMENT, "Equipements"),
            (CategoryEnum.CONSUMABLES, "Consommables"),
            (CategoryEnum.COSMETICS, "Cosmétiques"),
        ]
        with sessionmaker(bind=engine)() as session:
            self.types = (
                session.query(TypeItem).order_by(TypeItem.name).distinct().all()
            )
            self.items = session.query(Item).order_by(Item.name).distinct().all()

        self.setLayout(QHBoxLayout(self))

        category_combobox = ComboBox(parent=self)
        category_combobox.addItems(category[1] for category in self.categories)
        category_combobox.currentIndexChanged.connect(self.on_select_category)
        self.layout().addWidget(category_combobox)

        self.type_combobox = ComboBox(parent=self)
        self.type_combobox.currentTextChanged.connect(self.on_select_type)
        self.layout().addWidget(self.type_combobox)

        self.item_combobox = ComboBox(parent=self)
        self.item_combobox.currentTextChanged.connect(parent.on_select_item)
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


class Chart(QWidget):
    def __init__(self, engine: Engine, bot_info: BotInfo, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.engine = engine
        self.bot_info = bot_info
        self.server_id: int | None = None
        self.setLayout(QVBoxLayout(self))
        self.layout().setAlignment(Qt.AlignTop)

        self.filters = ChartFilters(parent=self, engine=self.engine)
        self.layout().addWidget(self.filters)

        self.canvas = ChartContent()
        self.layout().addWidget(self.canvas)

    def on_select_item(self, item_name: str):
        if item_name != "":
            df_info = get_info_by_type_or_object(
                engine=self.engine, server_id=self.server_id, object_name=item_name
            )
            if df_info is not None:
                self.canvas.show(df_info)


def get_info_by_type_or_object(
    engine: Engine, server_id: int | None, object_name: str | None = None
) -> pd.DataFrame | None:
    if server_id is None:
        return None
    # TODO Remove zeroes values
    with sessionmaker(bind=engine)() as session:
        df_prices = pd.read_sql(
            session.query(Item, Price, TypeItem)
            .join(TypeItem, Item.type_item_id == TypeItem.id)
            .join(Price, Item.id == Price.item_id)
            .filter(Item.name == object_name, Price.server_id == server_id)
            .with_entities(
                Item.name, Price.creation_date, Price.one, Price.ten, Price.hundred
            )
            .statement,
            engine,
        )

    return df_prices
