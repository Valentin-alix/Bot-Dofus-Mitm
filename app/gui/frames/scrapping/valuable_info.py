from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTableWidget, QScrollArea, QTableWidgetItem, QLabel, QHeaderView
from sqlalchemy import Engine

from app.gui.components.organization import HorizontalLayout, VerticalLayout, AlignDelegate
from app.utils import get_difference_on_all_prices, get_benefit_nugget


class ValuableInfo(QWidget):
    def __init__(self, engine: Engine, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
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
            ["Nom", "Prix par 100", "Bénéfices", "Zone favorite"]
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

        self.table_price_drop.setHorizontalHeaderLabels(["Nom", "Prix avant", "Prix après"])

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

        items = get_difference_on_all_prices(self.engine)

        self.table_price_drop.setRowCount(10)

        for index, (name, row) in enumerate(items.iterrows()):
            name_col = QTableWidgetItem(name)
            price_before_col = QTableWidgetItem(str(row["first"]))
            price_after_col = QTableWidgetItem(str(row["last"]))
            self.table_price_drop.setItem(int(index), 0, name_col)
            self.table_price_drop.setItem(int(index), 1, price_before_col)
            self.table_price_drop.setItem(int(index), 2, price_after_col)

    def get_benefit_recycling(self):
        self.table_benefit_recycling.clearContents()
        self.table_benefit_recycling.setRowCount(0)

        items_for_nugget = get_benefit_nugget(self.engine)

        self.table_benefit_recycling.setRowCount(10)
        for index, item_for_nugget in enumerate(items_for_nugget):
            name_col = QTableWidgetItem(item_for_nugget[1].name)
            price_col = QTableWidgetItem(str(item_for_nugget[0].hundred))
            benefit_col = QTableWidgetItem(str(item_for_nugget[3]))
            favorite_zone_col = QTableWidgetItem(
                str(", ".join(sub_area.name for sub_area in item_for_nugget[1].favorite_recycling_sub_areas)))

            self.table_benefit_recycling.setItem(index, 0, name_col)
            self.table_benefit_recycling.setItem(index, 1, price_col)
            self.table_benefit_recycling.setItem(index, 2, benefit_col)
            self.table_benefit_recycling.setItem(index, 3, favorite_zone_col)
