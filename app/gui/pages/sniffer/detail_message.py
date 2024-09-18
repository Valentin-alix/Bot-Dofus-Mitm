from PyQt5.QtWidgets import QVBoxLayout, QWidget
from qfluentwidgets import FluentIcon, ToolButton

from app.gui.components.tree import DynamicTreeWidget


class DetailMessage(QWidget):
    def __init__(self, parsed_msg_json: dict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.v_layout = QVBoxLayout()
        self.setLayout(self.v_layout)

        self.quit_btn = ToolButton(FluentIcon.CLOSE)
        self.v_layout.addWidget(self.quit_btn)

        self.content = DynamicTreeWidget()
        self.content.set_content(parsed_msg_json)
        self.v_layout.addWidget(self.content)
