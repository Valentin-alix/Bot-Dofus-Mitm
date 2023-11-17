from PyQt5 import QtCore
from PyQt5.QtWidgets import QLayout, QVBoxLayout, QHBoxLayout, QStyledItemDelegate, QSpacerItem, QGridLayout


class Layout(QLayout):
    def set_not_margins(self):
        self.setContentsMargins(0, 0, 0, 0)

    def clear_list(self, proportion: float = 1, clear_spacer=False):
        for i in reversed(range(int(self.count() * proportion))):
            if (item := self.itemAt(i)) is not None:
                if clear_spacer and isinstance(item, QSpacerItem):
                    self.removeItem(item)

                if (item_widget := item.widget()) is not None:
                    item_widget.deleteLater()


class VerticalLayout(QVBoxLayout, Layout):
    def __init__(self, without_space: bool = True, without_margins: bool = True):
        super().__init__()
        if without_space:
            self.setSpacing(0)
        if without_margins:
            self.set_not_margins()


class HorizontalLayout(QHBoxLayout, Layout):
    def __init__(self, without_space: bool = True, without_margins: bool = True):
        super().__init__()
        if without_space:
            self.setSpacing(0)
        if without_margins:
            self.set_not_margins()


class GridLayout(QGridLayout, Layout):
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
