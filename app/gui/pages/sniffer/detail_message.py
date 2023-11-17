from PyQt5.QtWidgets import QWidget

from app.gui.components.common import ButtonIcon, TreeWidget
from app.gui.components.organization import VerticalLayout


class DetailMessage(QWidget):
    def __init__(self, parsed_msg_json: dict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = VerticalLayout()
        self.setLayout(self.layout)

        self.quit_btn = ButtonIcon("quit.svg")
        self.layout.addWidget(self.quit_btn)

        self.content = TreeWidget(parsed_msg_json)
        self.layout.addWidget(self.content)
