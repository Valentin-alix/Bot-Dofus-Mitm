from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
)
from qfluentwidgets import BodyLabel, FluentIcon, ToolButton


class TopPage(QWidget):
    def __init__(self, title: str | None = None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        v_layout = QVBoxLayout()
        v_layout.setContentsMargins(0, 0, 0, 0)
        v_layout.setSpacing(0)
        self.setLayout(v_layout)
        self.layout().setAlignment(Qt.AlignTop)

        if title is not None:
            self.title = BodyLabel(parent=self, text=title)
            self.layout().addWidget(self.title)

        self.header_buttons = QWidget(parent=self)
        self.layout().addWidget(self.header_buttons)

        self.header_buttons.setLayout(QHBoxLayout())

        self.button_play = ToolButton(FluentIcon.PLAY)
        self.header_buttons.layout().addWidget(self.button_play)

        self.button_stop = ToolButton(FluentIcon.PAUSE)
        self.header_buttons.layout().addWidget(self.button_stop)

    def do_play(self, is_playing: bool):
        if is_playing:
            self.button_play.hide()
            self.button_stop.show()
        else:
            self.button_play.show()
            self.button_stop.hide()
