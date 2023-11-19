from PyQt5.QtWidgets import QLabel, QFormLayout, QLineEdit

from app.gui.components.common import Widget
from app.gui.components.organization import VerticalLayout


class Item(Widget):
    def __init__(self, name: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = VerticalLayout()
        self.setLayout(self.layout)

        self.title = QLabel(name, parent=self)
        self.layout.addWidget(self.title)

        self.description = Widget(parent=self)
        self.layout.addWidget(self.description)
        self.form = QFormLayout()
        self.description.setLayout(self.form)

        self.form.addRow('Vitalité', QLineEdit(parent=self))
        self.form.addRow('Intel', QLineEdit(parent=self))
