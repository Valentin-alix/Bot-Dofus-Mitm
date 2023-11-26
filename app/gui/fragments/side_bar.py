from __future__ import annotations

from functools import partial
from typing import TYPE_CHECKING

from PyQt5.QtCore import Qt, QObject, pyqtSignal
from PyQt5.QtWidgets import QSizePolicy

from app.gui.components.common import Widget, ButtonIcon, Frame
from app.gui.components.organization import VerticalLayout

if TYPE_CHECKING:
    from app.gui.app import MainWindow


class SideBarItem(ButtonIcon):
    def __init__(self, text: str = "", *args, **kwargs) -> None:
        super().__init__(height=50, *args, **kwargs)
        self.text = text

    def set_active_button(self):
        self.setObjectName("around-app-active")
        self.style().unpolish(self)
        self.style().polish(self)

    def set_inactive_button(self):
        self.setObjectName("around-app-inactive")
        self.style().unpolish(self)
        self.style().polish(self)


class SideBarSignals(QObject):
    on_click_item = pyqtSignal(SideBarItem)
    on_expanded = pyqtSignal()
    on_collapsed = pyqtSignal()


class SideBar(Widget):
    COLLAPSED_WIDTH = 60
    EXPANDED_WIDTH = 200
    ICON_BY_NAME = {
        "Sniffer": "search.svg",
        "Scraping": "activity.svg",
        "Vendeur": "sell.svg",
        "Fm": "magic-icon.svg",
    }

    def __init__(self, parent: MainWindow, frames: list[Frame], *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.set_object_name("around-app")
        self.setAttribute(Qt.WA_StyledBackground, True)  # to apply style to whole widget
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setFixedWidth(self.COLLAPSED_WIDTH)

        self.frames = frames
        self.signals = SideBarSignals()
        self.parent = parent
        self.is_expanded = False
        self.max_len_text = 0

        self.main_layout = VerticalLayout()
        self.main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.main_layout)
        self.setup_menu()
        self.show_items()

    def setup_menu(self):
        self.item_menu = SideBarItem(filename="menu.svg", parent=self)
        self.item_menu.setObjectName("sidebar-item-menu")
        self.item_menu.style().unpolish(self)
        self.item_menu.style().polish(self)
        self.item_menu.clicked.connect(self.on_expanded)
        self.main_layout.addWidget(self.item_menu)

        self.items = Widget(parent=self)
        self.items_layout = VerticalLayout()
        self.items.setLayout(self.items_layout)
        self.main_layout.addWidget(self.items)

    def on_expanded(self):
        if self.is_expanded:
            self.setFixedWidth(self.COLLAPSED_WIDTH)
            self.item_menu.set_icon('menu.svg')
            self.signals.on_collapsed.emit()
        else:
            self.setFixedWidth(self.EXPANDED_WIDTH)
            self.item_menu.set_icon('menu_open.svg')
            self.signals.on_expanded.emit()
        self.is_expanded = not self.is_expanded

    def show_items(self):
        for index, frame in enumerate(self.frames):
            side_bar_item = SideBarItem(filename=self.ICON_BY_NAME.get(frame.name), parent=self, text=frame.name)
            side_bar_item.clicked.connect(partial(self.on_clicked_item, side_bar_item))
            self.items_layout.addWidget(side_bar_item)
            if index == 0:
                side_bar_item.set_active_button()
            else:
                side_bar_item.set_inactive_button()
            if self.max_len_text < len(frame.name):
                self.max_len_text = len(frame.name)
            self.signals.on_expanded.connect(partial(self.set_text, side_bar_item))
            self.signals.on_collapsed.connect(partial(side_bar_item.setText, ""))

    def set_text(self, item: SideBarItem):
        """ workaround to center text inside pushbutton"""
        item.setText(
            f"{(self.max_len_text - len(item.text)) // 2 * ' '}{item.text}{(self.max_len_text - len(item.text)) // 2 * ' '}")

    def on_clicked_item(self, item: SideBarItem):
        items = [
            _item
            for index in range(self.items_layout.count())
            if isinstance(
                (_item := self.items_layout.itemAt(index).widget()),
                SideBarItem,
            )
        ]
        for _item in items:
            if _item == item:
                _item.set_active_button()
            else:
                _item.set_inactive_button()

        self.parent.stacked_frames.setCurrentIndex(items.index(item))
