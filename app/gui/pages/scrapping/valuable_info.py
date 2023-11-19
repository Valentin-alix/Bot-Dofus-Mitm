from PyQt5.QtWidgets import QTableWidgetItem, QLabel
from sqlalchemy import Engine

from app.gui.components.common import TableWidget, Widget
from app.gui.components.organization import HorizontalLayout, VerticalLayout
from app.types_.models.common import BotInfo
from app.utils import get_benefit_nugget, get_difference_on_all_prices


class ValuableInfo(Widget):
    table_benefit_recycling: TableWidget
    table_price_drop: TableWidget

    def __init__(self, engine: Engine, bot_info: BotInfo, *args,
                 **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.server_id: int | None = None
        self.bot_info = bot_info
        self.engine = engine

        self.main_layout = HorizontalLayout(without_space=False)
        self.setLayout(self.main_layout)

        self.setup_benefit_recycling()
        self.setup_price_drop()

    def on_reset(self):
        self.get_benefit_recycling()
        self.get_price_drop()

    def setup_benefit_recycling(self):
        benefit_recycling = Widget(parent=self)

        v_layout = VerticalLayout()
        benefit_recycling.setLayout(v_layout)

        title = QLabel(parent=self, text="Meilleur bénéfice recyclage")
        v_layout.addWidget(title)

        table_benefit_recycling_scroll = TableWidget(["Type", "Nom", "Bénéfices", "Zone favorite"])
        self.table_benefit_recycling = table_benefit_recycling_scroll.table
        v_layout.addWidget(table_benefit_recycling_scroll)

        self.main_layout.addWidget(benefit_recycling)

    def setup_price_drop(self):
        price_drop_widget = Widget(parent=self)

        v_layout = VerticalLayout()
        price_drop_widget.setLayout(v_layout)

        title = QLabel(parent=self, text="Chute de prix")
        v_layout.addWidget(title)

        table_price_drop_scroll = TableWidget(["Type", "Nom", "Différence"])
        self.table_price_drop = table_price_drop_scroll.table
        v_layout.addWidget(self.table_price_drop)

        self.main_layout.addWidget(price_drop_widget)

    def get_price_drop(self):
        self.table_price_drop.clearContents()
        self.table_price_drop.setRowCount(0)

        items = get_difference_on_all_prices(self.engine, self.server_id)
        if items is None:
            return

        self.table_price_drop.setRowCount(10)

        for index, (_type, name, benefit) in enumerate(items):
            type_col = QTableWidgetItem(_type)
            name_col = QTableWidgetItem(name)
            difference_col = QTableWidgetItem(str(benefit))

            self.table_price_drop.setItem(index, 0, type_col)
            self.table_price_drop.setItem(index, 1, name_col)
            self.table_price_drop.setItem(index, 2, difference_col)

    def get_benefit_recycling(self):
        self.table_benefit_recycling.clearContents()
        self.table_benefit_recycling.setRowCount(0)

        items_for_nugget = get_benefit_nugget(self.engine, self.server_id)
        if items_for_nugget is None:
            return

        self.table_benefit_recycling.setRowCount(10)
        for index, (_type, item, benefit) in enumerate(items_for_nugget):
            type_col = QTableWidgetItem(_type)
            name_col = QTableWidgetItem(item.name)
            benefit_col = QTableWidgetItem(str(benefit))
            favorite_zone_col = QTableWidgetItem(
                str(", ".join(sub_area.name for sub_area in item.favorite_recycling_sub_areas)))

            self.table_benefit_recycling.setItem(index, 0, type_col)
            self.table_benefit_recycling.setItem(index, 1, name_col)
            self.table_benefit_recycling.setItem(index, 2, benefit_col)
            self.table_benefit_recycling.setItem(index, 3, favorite_zone_col)
