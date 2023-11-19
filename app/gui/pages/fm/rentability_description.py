from PyQt5.QtWidgets import QGridLayout, QLabel

from app.gui.components.common import Widget


class RentabilityDescription(Widget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.title = QLabel("Rentabilité de l'item :")
        self.layout.addWidget(self.title, 0, 0)
