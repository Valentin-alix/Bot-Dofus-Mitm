from PyQt5.QtWidgets import QLabel, QComboBox, QTableWidgetItem
from sqlalchemy import Engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.query import RowReturningQuery

from app.database.models import Item, Price, TypeItem, CategoryEnum
from app.gui.components.common import Widget, TableWidget
from app.gui.components.organization import VerticalLayout


class PriceDropTable(Widget):
    FIELD_BY_QUANTITY = {
        "100": "hundred",
        "10": "ten",
        "1": "one"
    }

    def __init__(self, engine: Engine):
        super().__init__()
        self.engine = engine
        self.server_id: int | None = None
        v_layout = VerticalLayout()
        self.setLayout(v_layout)

        title = QLabel(parent=self, text="Chute de prix")
        v_layout.addWidget(title)

        self.quantity_drop_price_combobox = QComboBox(parent=self)
        self.quantity_drop_price_combobox.addItems(["100", "10", "1"])
        self.quantity_drop_price_combobox.currentTextChanged.connect(
            lambda text: self.get_price_drop())
        v_layout.addWidget(self.quantity_drop_price_combobox)

        table_price_drop_scroll = TableWidget(["Type", "Nom", "Différence"])
        self.table_price_drop = table_price_drop_scroll.table
        v_layout.addWidget(self.table_price_drop)

    def get_price_drop(self):
        quantity = self.FIELD_BY_QUANTITY.get(self.quantity_drop_price_combobox.currentText())

        self.table_price_drop.clearContents()
        self.table_price_drop.setRowCount(0)

        rows = 20

        items = get_difference_on_all_prices(self.engine, self.server_id, quantity, rows)
        if items is None:
            return

        self.table_price_drop.setRowCount(rows)

        for index, (_type, name, benefit) in enumerate(items):
            type_col = QTableWidgetItem(_type)
            name_col = QTableWidgetItem(name)
            difference_col = QTableWidgetItem(str(benefit))

            self.table_price_drop.setItem(index, 0, type_col)
            self.table_price_drop.setItem(index, 1, name_col)
            self.table_price_drop.setItem(index, 2, difference_col)


def get_difference_on_all_prices(
        engine: Engine, server_id: int | None, quantity: str, limit: int = 10
) -> RowReturningQuery[tuple[str, Item, int]] | None:
    if server_id is None:
        return None

    with sessionmaker(bind=engine)() as session:
        _items_latest_oldest_date = (
            session.query(
                Item.id,
                func.max(Price.creation_date).label("max_date"),
                func.min(Price.creation_date).label("min_date"),
            )
            .join(Price, Price.item_id == Item.id)
            .filter(Price.server_id == server_id)
            .group_by(Item.id)
            .subquery()
        )

        _items_latest = (
            session.query(Item.id, getattr(Price, quantity))
            .join(_items_latest_oldest_date, _items_latest_oldest_date.c.id == Item.id)
            .join(Price, Price.item_id == Item.id)
            .filter(Price.creation_date == _items_latest_oldest_date.c.max_date)
            .group_by(Item.id)
            .subquery()
        )

        _items_oldest = (
            session.query(Item.id, getattr(Price, quantity))
            .join(_items_latest_oldest_date, _items_latest_oldest_date.c.id == Item.id)
            .join(Price, Price.item_id == Item.id)
            .filter(Price.creation_date == _items_latest_oldest_date.c.min_date)
            .group_by(Item.id)
            .subquery()
        )

        difference_items = (
            session.query(TypeItem, Item)
            .join(_items_latest, _items_latest.c.id == Item.id)
            .join(_items_oldest, _items_oldest.c.id == Item.id)
            .join(TypeItem, Item.type_item_id == TypeItem.id)
            .filter(
                getattr(_items_latest.c, quantity) != 0,
                getattr(_items_oldest.c, quantity) != 0,
                TypeItem.category.in_(
                    [CategoryEnum.RESOURCES, CategoryEnum.CONSUMABLES]
                ),
            )
            .group_by(Item.id)
            .with_entities(
                TypeItem.name,
                Item.name,
                (getattr(_items_oldest.c, quantity) - getattr(_items_latest.c, quantity)).label("benefit"),
            )
            .order_by(-(getattr(_items_oldest.c, quantity) - getattr(_items_latest.c, quantity)))
            .limit(limit)
        )

    return difference_items
