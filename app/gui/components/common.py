import os
from pathlib import Path

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QDialog,
    QGroupBox,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
    QFrame,
)

from app.gui.components.organization import HorizontalLayout
from app.types_.parsed_message import ParsedMessage


class GroupBox(QGroupBox):
    def __init__(self, with_title: bool = True, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if not with_title:
            self.setObjectName("not-title")
            self.style().unpolish(self)
            self.style().polish(self)


class PushButtonUtils(QPushButton):
    def set_active_button(self):
        self.setObjectName("active")
        self.update_style()

    def set_inactive_button(self):
        self.setObjectName("inactive")
        self.update_style()

    def update_style(self):
        self.style().unpolish(self)
        self.style().polish(self)


class ButtonIcon(PushButtonUtils):
    def __init__(self, filename, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setIcon(
            QIcon(
                os.path.join(
                    Path(__file__).parent,
                    "../resources",
                    filename,
                )
            )
        )


class DetailMessageDialog(QDialog):
    def __init__(self, parsed_msg: ParsedMessage, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.setFixedSize(500, 300)
        self.setWindowTitle(f"{parsed_msg.__type__}")

        main_layout = QVBoxLayout()

        text_edit = QTextEdit(parent=self)
        text_edit.setPlainText(str(parsed_msg))
        text_edit.setReadOnly(True)
        main_layout.addWidget(text_edit)

        self.setLayout(main_layout)


class Header(QWidget):
    button_reset: PushButtonUtils | None = None

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.h_layout = HorizontalLayout()
        self.setLayout(self.h_layout)

        self.button_play = ButtonIcon("play.svg", parent=self)
        self.h_layout.addWidget(self.button_play)

        self.button_stop = ButtonIcon("stop", parent=self)
        self.h_layout.addWidget(self.button_stop)

    def do_play(self, is_playing: bool):
        if is_playing:
            self.button_play.set_active_button()
            self.button_stop.set_inactive_button()
        else:
            self.button_play.set_inactive_button()
            self.button_stop.set_active_button()


class Frame(QFrame):
    def __init__(self, name: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.name = name
