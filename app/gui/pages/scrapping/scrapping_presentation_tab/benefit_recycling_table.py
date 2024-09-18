from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem
from qfluentwidgets import BodyLabel, ComboBox, VBoxLayout
from sqlalchemy import Engine, desc, func
from sqlalchemy.orm import Query, joinedload, sessionmaker
from sqlalchemy.orm.query import RowReturningQuery

from app.database.models import CategoryEnum, Item, Price, TypeItem
from app.gui.components.common import QWidget
from app.gui.components.table import BaseTableWidget, ColumnInfo


class BenefitRecyclingTable(QWidget):
    FIELD_BY_QUANTITY = {"100": "hundred", "10": "ten", "1": "one"}

    def __init__(self, engine: Engine):
        super().__init__()
        self.engine = engine
        self.server_id: int | None = None
        self.setLayout(VBoxLayout(self))
        self.layout().setAlignment(Qt.AlignTop)

        title = BodyLabel(parent=self, text="Meilleur bénéfice recyclage")
        self.layout().addWidget(title)

        self.quantity_nuggets_combobox = ComboBox(parent=self)
        self.quantity_nuggets_combobox.addItems(["100", "10", "1"])
        self.quantity_nuggets_combobox.currentTextChanged.connect(
            lambda _: self.get_benefit_recycling()
        )
        self.layout().addWidget(self.quantity_nuggets_combobox)

        table_benefit_recycling = BaseTableWidget(is_searchable=False)
        table_benefit_recycling.set_columns(
            [
                ColumnInfo(name="Type", search_type=None),
                ColumnInfo(name="Nom", search_type=None),
                ColumnInfo(name="Bénéfices", search_type=None),
                ColumnInfo(name="Zone favorite", search_type=None),
            ]
        )
        self.table_benefit_recycling = table_benefit_recycling.table
        self.layout().addWidget(self.table_benefit_recycling)

    def get_benefit_recycling(self):
        quantity = self.FIELD_BY_QUANTITY[self.quantity_nuggets_combobox.currentText()]

        self.table_benefit_recycling.clearContents()
        self.table_benefit_recycling.setRowCount(0)

        rows = 20

        items_for_nugget = get_benefit_nugget(
            self.engine, self.server_id, quantity, rows
        )
        if items_for_nugget is None:
            return

        self.table_benefit_recycling.setRowCount(rows)
        for index, (_type, item, benefit) in enumerate(items_for_nugget):
            type_col = QTableWidgetItem(_type)
            name_col = QTableWidgetItem(item.name)
            benefit_col = QTableWidgetItem(str(benefit))
            favorite_zone_col = QTableWidgetItem(
                str(
                    ", ".join(
                        sub_area.name for sub_area in item.favorite_recycling_sub_areas
                    )
                )
            )

            self.table_benefit_recycling.setItem(index, 0, type_col)
            self.table_benefit_recycling.setItem(index, 1, name_col)
            self.table_benefit_recycling.setItem(index, 2, benefit_col)
            self.table_benefit_recycling.setItem(index, 3, favorite_zone_col)


def get_benefit_nugget(
    engine: Engine, server_id: int | None, quantity: str, limit: int = 10
) -> RowReturningQuery[tuple[str, list[Item], int]] | Query | None:
    if server_id is None:
        return None
    with sessionmaker(bind=engine)() as session:
        price_for_100_nugget = (
            session.query(getattr(Price, quantity))
            .filter(Price.server_id == server_id)
            .join(Item, Price.item_id == Item.id)
            .order_by(Price.creation_date.desc())
            .filter(Item.name == "Pépite")
            .first()
        )
        if price_for_100_nugget is None:
            return None

        price_for_100_nugget = price_for_100_nugget[0]

        _items_latest = (
            session.query(Item.id, func.max(Price.creation_date).label("max_date"))
            .join(Price, Price.item_id == Item.id)
            .filter(Price.server_id == server_id)
            .group_by(Item.id)
            .subquery()
        )

        benefits_nugget = (
            session.query(
                Price,
                TypeItem.name,
                Item.name,
                func.round(
                    Item.recycling_nuggets * price_for_100_nugget
                    - getattr(Price, quantity),
                    0,
                ).label("benefits"),
                Item.favorite_recycling_sub_areas,
            )
            .join(Item, Item.id == Price.item_id)
            .join(_items_latest, _items_latest.c.id == Item.id)
            .join(TypeItem, TypeItem.id == Item.type_item_id)
            .filter(
                Price.server_id == server_id,
                Price.creation_date == _items_latest.c.max_date,
                TypeItem.category == CategoryEnum.RESOURCES,
            )
            .group_by(Price.item_id)
            .having(getattr(Price, quantity) != 0)
            .order_by(
                desc(
                    Item.recycling_nuggets * price_for_100_nugget
                    - getattr(Price, quantity)
                )
            )
            .with_entities(
                TypeItem.name,
                Item,
                func.round(
                    Item.recycling_nuggets * price_for_100_nugget
                    - getattr(Price, quantity),
                    0,
                ).label("benefits"),
            )
            .options(joinedload(Item.favorite_recycling_sub_areas))
            .limit(limit)
        )

    return benefits_nugget
