from PyQt5.QtWidgets import QHBoxLayout, QWidget
from qfluentwidgets import ComboBox


class PriceDropFilters(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setLayout(QHBoxLayout())
        self.quantity = ComboBox(parent=self)
        self.quantity.addItems(["100", "10", "1"])
        self.layout().addWidget(self.quantity)
