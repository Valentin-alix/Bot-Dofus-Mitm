from abc import ABC
import os
import pprint
from pathlib import Path

from network.models.message import Message, ParsedMessage
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QBoxLayout,
    QColorDialog,
    QDialog,
    QDialogButtonBox,
    QFrame,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLayout,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMenu,
    QMessageBox,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


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

    def clear_list(self):
        for i in reversed(range(self.count())):
            if (item_child_layout := self.itemAt(i)) is not None and (
                child_layout := item_child_layout.widget()
            ) is not None:
                child_layout.setParent(None)


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
    def __init__(self, parent, message: ParsedMessage) -> None:
        super().__init__(parent)
        self.setFixedSize(500, 300)
        self.setWindowTitle(f"{message.__type__}")

        main_layout = QVBoxLayout()

        text_edit = QTextEdit(self)
        text_edit.setPlainText(str(message))
        text_edit.setReadOnly(True)
        main_layout.addWidget(text_edit)

        self.setLayout(main_layout)
