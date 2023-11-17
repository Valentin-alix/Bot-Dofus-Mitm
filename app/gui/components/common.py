import os
from pathlib import Path

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QGroupBox,
    QPushButton,
    QWidget,
    QFrame,
    QScrollArea,
    QTableWidget,
    QHeaderView,
    QTreeWidget,
    QTreeWidgetItem,
)

from app.gui.components.organization import HorizontalLayout, AlignDelegate


class TableWidget(QScrollArea):
    def __init__(self, columns_name: list[str], *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.table = QTableWidget(parent=self)
        self.table.setColumnCount(len(columns_name))

        delegate = AlignDelegate(self.table)
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


class GroupBox(QGroupBox):
    def __init__(self, with_title: bool = True, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if not with_title:
            self.setObjectName("not-title")
            self.style().unpolish(self)
            self.style().polish(self)


class PushButton(QPushButton):
    def set_active_button(self):
        self.setObjectName("active")
        self.style().unpolish(self)
        self.style().polish(self)

    def set_inactive_button(self):
        self.setObjectName("inactive")
        self.style().unpolish(self)
        self.style().polish(self)


class ButtonIcon(PushButton):
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


class Header(QWidget):
    button_reset: PushButton | None = None

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
