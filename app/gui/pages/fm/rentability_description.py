from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel


class RentabilityDescription(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.title = QLabel("Rentabilité de l'item :")
        self.layout.addWidget(self.title, 0, 0)
