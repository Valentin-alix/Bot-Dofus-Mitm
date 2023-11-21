import os
from pathlib import Path

from PyQt5 import QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtWidgets import (
    QPushButton,
    QWidget,
    QFrame,
    QScrollArea,
    QTableWidget,
    QHeaderView,
    QTreeWidget,
    QTreeWidgetItem, QLabel, )

from app.gui.components.organization import HorizontalLayout, AlignDelegate, VerticalLayout


class Widget(QWidget):
    def set_object_name(self, obj_name: str):
        self.setObjectName(obj_name)
        self.style().unpolish(self)
        self.style().polish(self)


class TableWidget(QScrollArea):
    def __init__(self, columns_name: list[str], delegate_type=AlignDelegate, *args, **kwargs):
        # TODO Delegate painter
        super().__init__(*args, **kwargs)

        self.table = QTableWidget(parent=self)
        self.table.setColumnCount(len(columns_name))

        delegate = delegate_type(self.table)
        for index in range(len(columns_name)):
            self.table.setItemDelegateForColumn(index, delegate)

        self.table.setHorizontalHeaderLabels(columns_name)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().hide()

        self.setWidget(self.table)
        self.setWidgetResizable(True)


class TreeWidget(QTreeWidget):
    def __init__(self, json: dict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.header().hide()
        self.deep_tree_from_message_dict(json, None, self)

    def deep_tree_from_message_dict(
            self,
            _values,
            parent: QTreeWidgetItem | None = None,
            base_qtree: QTreeWidget | None = None,
    ):
        if not isinstance(_values, dict):
            widget_item = QTreeWidgetItem([f"{_values}"])
            if parent is not None:
                parent.addChild(widget_item)
        else:
            for key, value in _values.items():
                if isinstance(value, dict):
                    widget_item = QTreeWidgetItem([f"{key}"])
                    self.deep_tree_from_message_dict(value, widget_item)
                elif isinstance(value, list):
                    widget_item = QTreeWidgetItem([f"{key}"])
                    for _value in value:
                        self.deep_tree_from_message_dict(_value, widget_item)
                else:
                    widget_item = QTreeWidgetItem([f"{key} = {value}"])
                if parent is not None:
                    parent.addChild(widget_item)
                elif base_qtree is not None:
                    base_qtree.addTopLevelItem(widget_item)


class PushButton(QPushButton, Widget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    def set_active_button(self):
        self.set_object_name("active")

    def set_inactive_button(self):
        self.set_object_name("inactive")


class ButtonIcon(PushButton):
    def __init__(self, filename, height=40, icon_size=32, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.set_icon(filename)
        self.setFixedHeight(height)
        self.setIconSize(QSize(icon_size, icon_size))

    def set_icon(self, filename):
        self.setIcon(
            QIcon(
                os.path.join(
                    Path(__file__).parent.parent,
                    "resources",
                    "icons",
                    filename,
                )
            )
        )


class TopPage(Widget):
    button_reset: PushButton | None = None

    def __init__(self, with_restart: bool = False, title: str | None = None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.main_layout = VerticalLayout()
        self.setLayout(self.main_layout)

        if title is not None:
            self.title = QLabel(parent=self, text=title)
            self.main_layout.addWidget(self.title)

        self.header_buttons = QWidget(parent=self)
        self.main_layout.addWidget(self.header_buttons)
        self.h_layout = HorizontalLayout()
        self.header_buttons.setLayout(self.h_layout)
        self.header_buttons.setLayout(self.h_layout)

        if with_restart:
            self.button_reset = ButtonIcon("restart.svg", parent=self, height=30, icon_size=20)
            self.h_layout.addWidget(self.button_reset)

        self.button_play = ButtonIcon("play.svg", parent=self, height=30, icon_size=20)
        self.h_layout.addWidget(self.button_play)

        self.button_stop = ButtonIcon("stop", parent=self, height=30, icon_size=15)
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
