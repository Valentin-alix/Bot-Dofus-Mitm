from PyQt5.QtWidgets import QTableWidgetItem

from app.database.queries import get_benefit_nugget
from app.database.utils import SessionLocal
from app.gui.components.table import BaseTableWidget, ColumnInfo


class BenefitRecyclingTable(BaseTableWidget):
    FIELD_BY_QUANTITY = {"100": "hundred", "10": "ten", "1": "one"}

    def __init__(self, server_id: int | None):
        super().__init__(is_searchable=False)
        self.server_id = server_id
        self.set_columns(
            [
                ColumnInfo(name="Type", search_type=None),
                ColumnInfo(name="Nom", search_type=None),
                ColumnInfo(name="Bénéfices", search_type=None),
                ColumnInfo(name="Zone favorite", search_type=None),
            ]
        )

    def get_benefit_recycling(self, quantity: str):
        quantity = self.FIELD_BY_QUANTITY[quantity]

        self.table.clearContents()
        self.table.setRowCount(0)

        rows = 20
        with SessionLocal() as session:
            items_for_nugget = get_benefit_nugget(
                session, self.server_id, quantity, rows
            )
        if items_for_nugget is None:
            return

        self.table.setRowCount(rows)
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

            self.table.setItem(index, 0, type_col)
            self.table.setItem(index, 1, name_col)
            self.table.setItem(index, 2, benefit_col)
            self.table.setItem(index, 3, favorite_zone_col)
