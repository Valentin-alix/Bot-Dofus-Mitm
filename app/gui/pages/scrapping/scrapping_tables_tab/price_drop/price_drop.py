from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout
from qfluentwidgets import BodyLabel

from app.gui.components.common import QWidget
from app.gui.pages.scrapping.scrapping_tables_tab.price_drop.price_drop_filters import (
    PriceDropFilters,
)
from app.gui.pages.scrapping.scrapping_tables_tab.price_drop.price_drop_table import (
    PriceDropTable,
)


class PriceDrop(QWidget):
    def __init__(self):
        super().__init__()
        self.server_id: int | None = None
        self.setLayout(QVBoxLayout(self))
        self.layout().setAlignment(Qt.AlignTop)

        self.layout().addWidget(BodyLabel(parent=self, text="Chute de prix"))

        self.filters = PriceDropFilters()
        self.table = PriceDropTable(self.server_id)

        self.filters.quantity.currentTextChanged.connect(self.table.get_price_drop)

        self.layout().addWidget(self.filters)
        self.layout().addWidget(self.table)
