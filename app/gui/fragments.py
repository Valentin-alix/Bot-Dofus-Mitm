from typing import Callable, Dict, Optional, Type
from functools import partial
from gui.components import Frame, ListWidgetItem, PushButtonUtils, VerticalLayout
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QBoxLayout,
    QColorDialog,
    QDialog,
    QDialogButtonBox,
    QDockWidget,
    QFrame,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLayout,
    QListWidget,
    QMainWindow,
    QMenu,
    QMessageBox,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSpacerItem,
    QStackedLayout,
    QStackedWidget,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)


class SideMenu(QWidget):
    WIDTH = 100

    def __init__(self, parent) -> None:
        super().__init__(parent.all_content)
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
        self.side_menu_layout.setSpacing(0)
        self.setLayout(self.side_menu_layout)

    def show_menu(self):
        for index_widget in reversed(range(self.parent_.stacked_frames.count())):
            current_widget = self.parent_.stacked_frames.widget(index_widget)
            if (name := getattr(current_widget, "name", None)) is not None:
                button = PushButtonUtils(text=name)
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
