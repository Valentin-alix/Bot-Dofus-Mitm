from PyQt5.QtCore import QThread, pyqtSlot
from PyQt5.QtWidgets import QTableWidgetItem

from app.database.queries import get_difference_on_all_prices
from app.database.utils import SessionLocal
from app.gui.components.table import BaseTableWidget, ColumnInfo
from app.gui.utils import Worker, run_in_background


class PriceDropTable(BaseTableWidget):
    FIELD_BY_QUANTITY = {"100": "hundred", "10": "ten", "1": "one"}

    def __init__(self, server_id: int | None, *args, **kwargs):
        super().__init__(is_searchable=False, *args, **kwargs)
        self.price_drop_thread: QThread | None = None
        self.price_drop_worker: Worker | None = None
        self.server_id = server_id
        self.set_columns(
            [
                ColumnInfo(name="Type", search_type=None),
                ColumnInfo(name="Nom", search_type=None),
                ColumnInfo(name="Différence", search_type=None),
            ]
        )

    @pyqtSlot(object)
    def on_new_prices_drop(self, items: list | None):
        if items is None:
            return

        self.table.clearContents()
        self.table.setRowCount(0)

        self.table.setRowCount(len(items))

        for index, (type_name, name, benefit) in enumerate(items):
            type_col = QTableWidgetItem(type_name)
            name_col = QTableWidgetItem(name)
            difference_col = QTableWidgetItem(str(benefit))

            self.table.setItem(index, 0, type_col)
            self.table.setItem(index, 1, name_col)
            self.table.setItem(index, 2, difference_col)

    def get_price_drop(self, quantity: str):
        quantity = self.FIELD_BY_QUANTITY[quantity]

        def _get_price_drop():
            with SessionLocal() as session:
                items = get_difference_on_all_prices(
                    session, self.server_id, quantity, 20
                )
            return items

        self.price_drop_thread, self.price_drop_worker = run_in_background(
            _get_price_drop
        )
        self.price_drop_worker.signals.function_result.connect(self.on_new_prices_drop)
