from PyQt5.QtCore import QSize

from app.gui.components.common import ButtonIcon, TreeWidget, Widget
from app.gui.components.organization import VerticalLayout


class DetailMessage(Widget):
    def __init__(self, parsed_msg_json: dict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = VerticalLayout()
        self.setLayout(self.layout)

        self.quit_btn = ButtonIcon("quit.svg")
        self.quit_btn.setFixedHeight(30)
        self.quit_btn.setIconSize(QSize(25, 25))
        self.layout.addWidget(self.quit_btn)

        self.content = TreeWidget(parsed_msg_json)
        self.layout.addWidget(self.content)
