from typing import Callable, Dict, Optional, Type
from functools import partial
from gui.components import ListWidgetItem, PushButtonUtils, VerticalLayout
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
    PAGES = ["Sniffer", "BotFM"]
    WIDTH = 100

    on_change_page_signal = pyqtSignal(int)

    def __init__(self, parent) -> None:
        super().__init__(parent)

        self.setFixedWidth(self.WIDTH)

        self.side_menu_layout = VerticalLayout()
        self.side_menu_layout.addStretch()
        self.side_menu_layout.setDirection(QBoxLayout.Direction.BottomToTop)
        self.side_menu_layout.setSpacing(0)
        self.setLayout(self.side_menu_layout)

        for page_name in reversed(self.PAGES):
            button = PushButtonUtils(text=page_name)
            button.setFixedHeight(100)
            self.side_menu_layout.addWidget(button)
            if self.PAGES.index(page_name) == 0:
                button.set_active_button()
            button.clicked.connect(partial(self.on_change_page, page_name))

    def on_change_page(self, page_name: str):
        for index in range(self.side_menu_layout.count()):
            child = self.side_menu_layout.itemAt(index)
            if child is not None:
                child_widget = child.widget()
                if isinstance(child_widget, PushButtonUtils):
                    if child_widget.text() == page_name:
                        child_widget.set_active_button()
                    else:
                        child_widget.set_inactive_button()
        self.on_change_page_signal.emit(self.PAGES.index(page_name))
