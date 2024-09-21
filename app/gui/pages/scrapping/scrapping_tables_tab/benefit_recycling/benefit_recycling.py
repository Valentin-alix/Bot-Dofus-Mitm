from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from qfluentwidgets import BodyLabel

from app.gui.pages.scrapping.scrapping_tables_tab.benefit_recycling.benefit_recycling_filters import (
    BenefitRecyclingFilters,
)
from app.gui.pages.scrapping.scrapping_tables_tab.benefit_recycling.benefit_recycling_table import (
    BenefitRecyclingTable,
)


class BenefitRecycling(QWidget):
    def __init__(self, server_id: int | None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setLayout(QVBoxLayout(self))
        self.layout().setAlignment(Qt.AlignTop)

        self.layout().addWidget(
            BodyLabel(parent=self, text="Meilleur bénéfice recyclage")
        )

        self.filters = BenefitRecyclingFilters()
        self.table = BenefitRecyclingTable(server_id)

        self.filters.quantity.currentTextChanged.connect(
            self.table.get_benefit_recycling
        )

        self.layout().addWidget(self.filters)
        self.layout().addWidget(self.table)
