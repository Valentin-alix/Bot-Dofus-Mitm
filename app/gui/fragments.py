from __future__ import annotations

from functools import partial
from typing import TYPE_CHECKING

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import (
    QBoxLayout,
    QWidget,
)

from app.gui.components.common import PushButtonUtils
from app.gui.components.organization import VerticalLayout

if TYPE_CHECKING:
    from app.gui.app import MainWindow


class SideMenu(QWidget):
    WIDTH = 110

    def __init__(self, parent: MainWindow, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.parent_ = parent
        self.setFixedWidth(self.WIDTH)
        self.setup_menu()
        self.show_menu()

        self.parent_.signals.on_change_frame.connect(self.on_change_frame)

    def on_change_frame(self) -> None:
        self.side_menu_layout.clear_list()
        self.show_menu()

    def setup_menu(self) -> None:
        self.side_menu_layout = VerticalLayout()
        self.side_menu_layout.addStretch()
        self.side_menu_layout.setDirection(QBoxLayout.Direction.BottomToTop)
        self.setLayout(self.side_menu_layout)

    def show_menu(self):
        for index_widget in reversed(range(self.parent_.stacked_frames.count())):
            current_widget = self.parent_.stacked_frames.widget(index_widget)
            if (name := getattr(current_widget, "name", None)) is not None:
                button = PushButtonUtils(parent=self, text=name)
                button.setFixedHeight(100)
                self.side_menu_layout.addWidget(button)
                if index_widget == 0:
                    button.set_active_button()
                button.clicked.connect(partial(self.on_switch_frame, index_widget))

    def update_state_button(self, index_widget):
        buttons_layout = [
            button
            for index in reversed(range(self.side_menu_layout.count()))
            if isinstance(
                (button := self.side_menu_layout.itemAt(index).widget()),
                PushButtonUtils,
            )
        ]
        for index, button in enumerate(buttons_layout):
            if index == index_widget:
                button.set_active_button()
            else:
                button.set_inactive_button()

    def on_switch_frame(self, index_widget):
        self.update_state_button(index_widget)
        self.parent_.stacked_frames.setCurrentIndex(index_widget)


class DarkThemePalette(QPalette):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setColor(QPalette.Window, QColor(53, 53, 53))
        self.setColor(QPalette.WindowText, Qt.white)
        self.setColor(QPalette.Base, QColor(25, 25, 25))
        self.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        self.setColor(QPalette.ToolTipBase, Qt.black)
        self.setColor(QPalette.ToolTipText, Qt.white)
        self.setColor(QPalette.Text, Qt.white)
        self.setColor(QPalette.Button, QColor(53, 53, 53))
        self.setColor(QPalette.ButtonText, Qt.white)
        self.setColor(QPalette.BrightText, Qt.red)
        self.setColor(QPalette.Link, QColor(42, 130, 218))
        self.setColor(QPalette.Highlight, QColor(42, 130, 218))
        self.setColor(QPalette.HighlightedText, Qt.black)
