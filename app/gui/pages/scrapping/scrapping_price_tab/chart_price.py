from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout

from app.database.queries import get_info_by_type_or_object
from app.database.utils import SessionLocal
from app.gui.components.common import QWidget
from app.gui.pages.scrapping.scrapping_price_tab.chart_content import ChartContent
from app.gui.pages.scrapping.scrapping_price_tab.chart_filters import ChartFilters
from app.interfaces.models.common import BotInfo


class ChartPrice(QWidget):
    def __init__(self, bot_info: BotInfo, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot_info = bot_info
        self.server_id: int | None = None
        self.setLayout(QVBoxLayout(self))
        self.layout().setAlignment(Qt.AlignTop)

        self.filters = ChartFilters(parent=self)
        self.filters.item_combobox.currentTextChanged.connect(self.on_select_item)
        self.layout().addWidget(self.filters)

        self.canvas = ChartContent()
        self.layout().addWidget(self.canvas)

    def on_select_item(self, item_name: str):
        if item_name != "":
            with SessionLocal() as session:
                df_info = get_info_by_type_or_object(
                    session, server_id=self.server_id, object_name=item_name
                )
            if df_info is not None:
                self.canvas.show(df_info)
