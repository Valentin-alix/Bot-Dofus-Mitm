from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTableWidget, QScrollArea, QTableWidgetItem, QLabel, QHeaderView
from sqlalchemy import Engine

from app.gui.components.organization import HorizontalLayout, VerticalLayout, AlignDelegate
from app.types_ import BotInfo
from app.utils import get_difference_on_all_prices, get_benefit_nugget


class ValuableInfo(QWidget):
    def __init__(self, engine: Engine, bot_info: BotInfo, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.bot_info = bot_info
        self.engine = engine
        self.main_layout = HorizontalLayout(without_space=False)

        self.setLayout(self.main_layout)
        self.show_benefit_recycling()
        self.show_price_drop()

    def on_reset(self):
        self.get_benefit_recycling()
        self.get_price_drop()

    def show_benefit_recycling(self):
        benefit_recycling = QWidget(parent=self)

        v_layout = VerticalLayout()
        benefit_recycling.setLayout(v_layout)

        title = QLabel(parent=self, text="Meilleur bénéfice recyclage")
        title.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(title)

        scroll_area = QScrollArea(parent=self)

        self.table_benefit_recycling = QTableWidget(parent=scroll_area)
        self.table_benefit_recycling.setColumnCount(4)

        delegate = AlignDelegate(self.table_benefit_recycling)
        for column_index in range(4):
            self.table_benefit_recycling.setItemDelegateForColumn(column_index, delegate)

        self.table_benefit_recycling.setHorizontalHeaderLabels(
            ["Type", "Nom", "Bénéfices", "Zone favorite"]
        )

        self.table_benefit_recycling.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_benefit_recycling.verticalHeader().hide()

        scroll_area.setWidget(self.table_benefit_recycling)
        scroll_area.setWidgetResizable(True)

        v_layout.addWidget(scroll_area)

        self.main_layout.addWidget(benefit_recycling)

        self.get_benefit_recycling()

    def show_price_drop(self):
        price_drop_widget = QWidget(parent=self)

        v_layout = VerticalLayout()
        price_drop_widget.setLayout(v_layout)

        title = QLabel(parent=self, text="Chute de prix")
        title.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(title)

        scroll_area = QScrollArea(parent=self)

        self.table_price_drop = QTableWidget(parent=scroll_area)
        self.table_price_drop.setColumnCount(3)

        delegate = AlignDelegate(self.table_price_drop)
        for column_index in range(3):
            self.table_price_drop.setItemDelegateForColumn(column_index, delegate)

        self.table_price_drop.setHorizontalHeaderLabels(["Type", "Nom", "Différence"])

        self.table_price_drop.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_price_drop.verticalHeader().hide()

        scroll_area.setWidget(self.table_price_drop)
        scroll_area.setWidgetResizable(True)
        v_layout.addWidget(scroll_area)

        self.main_layout.addWidget(price_drop_widget)

        self.get_price_drop()

    def get_price_drop(self):
        self.table_price_drop.clearContents()
        self.table_price_drop.setRowCount(0)

        with self.bot_info.common_info.server_id_with_lock.get("lock"):
            items = get_difference_on_all_prices(self.engine,
                                                 self.bot_info.common_info.server_id_with_lock["server_id"])
        self.table_price_drop.setRowCount(10)

        for index, (_type, name, benefit) in enumerate(items):
            type_col = QTableWidgetItem(_type)
            name_col = QTableWidgetItem(name)
            difference_col = QTableWidgetItem(str(benefit))
            self.table_price_drop.setItem(int(index), 0, type_col)
            self.table_price_drop.setItem(int(index), 1, name_col)
            self.table_price_drop.setItem(int(index), 2, difference_col)

    def get_benefit_recycling(self):
        self.table_benefit_recycling.clearContents()
        self.table_benefit_recycling.setRowCount(0)
        with self.bot_info.common_info.server_id_with_lock.get("lock"):
            items_for_nugget = get_benefit_nugget(self.engine,
                                                  self.bot_info.common_info.server_id_with_lock["server_id"])
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
