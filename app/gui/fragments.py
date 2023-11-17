from __future__ import annotations

from functools import partial
from typing import TYPE_CHECKING

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import (
    QWidget, )

from app.gui.components.common import PushButton
from app.gui.components.organization import VerticalLayout

if TYPE_CHECKING:
    from app.gui.app import MainWindow


class SideMenu(QWidget):
    WIDTH = 110

    def __init__(self, parent: MainWindow, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.parent_ = parent
        self.setFixedWidth(self.WIDTH)

        self.layout = VerticalLayout()
        self.setLayout(self.layout)
        self.show_menu()

        self.parent_.signals.on_new_frames.connect(self.on_new_frames)

    def on_new_frames(self) -> None:
        self.layout.clear_list(clear_spacer=True)
        self.show_menu()

    def show_menu(self):
        for index_widget in range(self.parent_.stacked_frames.count()):
            current_widget = self.parent_.stacked_frames.widget(index_widget)
            if (name := getattr(current_widget, "name", None)) is not None:
                button = PushButton(parent=self, text=name)
                button.setFixedHeight(100)
                self.layout.addWidget(button)
                if index_widget == 0:
                    button.set_active_button()
                button.clicked.connect(partial(self.on_switch_frame, index_widget))
        self.layout.addStretch()

    def update_state_button(self, index_widget):
        buttons_layout = [
            button
            for index in range(self.layout.count())
            if isinstance(
                (button := self.layout.itemAt(index).widget()),
                PushButton,
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
