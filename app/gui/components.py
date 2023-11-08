import os
from pathlib import Path

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QDialog,
    QFrame,
    QGroupBox,
    QHBoxLayout,
    QLayout,
    QListWidgetItem,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
)

from network.parsed_message.parsed_message import ParsedMessage


class Frame(QFrame):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name


class ListWidgetItem(QListWidgetItem):
    def __init__(self) -> None:
        super().__init__()
        self.setSizeHint(QSize(100, 100))
        self.setTextAlignment(Qt.AlignmentFlag.AlignCenter)


class GroupBox(QGroupBox):
    def __init__(self, with_title: bool = True) -> None:
        super().__init__()
        if not with_title:
            self.setStyleSheet("QGroupBox{padding-top:15px;}")
        self.setContentsMargins(0, 0, 0, 0)


class LayoutUtils(QLayout):
    def set_not_margins(self):
        self.setContentsMargins(0, 0, 0, 0)

    def clear_list(self, proportion: float = 1):
        for i in reversed(range(int(self.count() * proportion))):
            if (item_child_layout := self.itemAt(i)) is not None and (
                child_layout := item_child_layout.widget()
            ) is not None:
                child_layout.deleteLater()


class VerticalLayout(QVBoxLayout, LayoutUtils):
    def __init__(self, without_margins: bool = True):
        super().__init__()
        if without_margins:
            self.set_not_margins()


class HorizontalLayout(QHBoxLayout, LayoutUtils):
    def __init__(self, without_margins: bool = True):
        super().__init__()
        if without_margins:
            self.set_not_margins()


class PushButtonUtils(QPushButton):
    def set_active_button(self):
        self.setStyleSheet("background-color: green")

    def set_inactive_button(self):
        self.setStyleSheet("background-color: rgb(53, 53, 53)")


class ButtonIcon(PushButtonUtils):
    def __init__(
        self, filename, icon_size: int = 30, button_size: int | None = None
    ) -> None:
        super().__init__()
        self.setIcon(
            QIcon(
                os.path.join(
                    Path(__file__).parent,
                    "resources",
                    filename,
                )
            )
        )
        self.setIconSize(QSize(icon_size, icon_size))
        if button_size is not None:
            self.setFixedSize(QSize(button_size, button_size))


class DetailMessageDialog(QDialog):
    def __init__(self, parent, parsed_msg: ParsedMessage) -> None:
        super().__init__(parent)
        self.setFixedSize(500, 300)
        self.setWindowTitle(f"{parsed_msg.__type__}")

        main_layout = QVBoxLayout()

        text_edit = QTextEdit(self)
        text_edit.setPlainText(str(parsed_msg))
        text_edit.setReadOnly(True)
        main_layout.addWidget(text_edit)

        self.setLayout(main_layout)


class Header(GroupBox):
    button_reset: PushButtonUtils | None = None

    def __init__(self) -> None:
        super().__init__()
        self.h_layout = HorizontalLayout()
        self.setLayout(self.h_layout)

        self.button_play = ButtonIcon("play.svg")
        self.h_layout.addWidget(self.button_play)

        self.button_stop = ButtonIcon("stop")
        self.h_layout.addWidget(self.button_stop)

    def do_play(self, is_playing: bool):
        if is_playing:
            self.button_play.set_active_button()
            self.button_stop.set_inactive_button()
        else:
            self.button_play.set_inactive_button()
            self.button_stop.set_active_button()
