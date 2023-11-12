from PyQt5 import QtCore
from PyQt5.QtWidgets import QLayout, QVBoxLayout, QHBoxLayout, QStyledItemDelegate


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
    def __init__(self, without_space: bool = True, without_margins: bool = True):
        super().__init__()
        if without_space:
            self.setSpacing(0)
        if without_margins:
            self.set_not_margins()


class HorizontalLayout(QHBoxLayout, LayoutUtils):
    def __init__(self, without_space: bool = True, without_margins: bool = True):
        super().__init__()
        if without_space:
            self.setSpacing(0)
        if without_margins:
            self.set_not_margins()


class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter
