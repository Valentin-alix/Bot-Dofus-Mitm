from typing import Optional, Dict, Type, Callable

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QGroupBox,
    QVBoxLayout,
    QHBoxLayout,
    QSizePolicy,
    QLabel,
    QBoxLayout,
    QDialogButtonBox,
    QDialog,
    QMessageBox,
    QColorDialog,
    QLayout,
    QWidget,
    QFrame,
    QAction,
    QListWidget,
    QStatusBar,
    QMenu,
    QStackedWidget,
    QStackedLayout,
    QScrollArea,
    QDockWidget,
    QSpacerItem,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor

from gui.components import ListWidgetItem


class QDarkThemePalette(QPalette):
    def __init__(self) -> None:
        super().__init__()
        self.setColor(QPalette.Window, QColor(53, 53, 53))
        self.setColor(QPalette.WindowText, QColor(255, 255, 255))
        self.setColor(QPalette.Base, QColor(25, 25, 25))
        self.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        self.setColor(QPalette.ToolTipBase, QColor(0, 0, 0))
        self.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
        self.setColor(QPalette.Text, QColor(255, 255, 255))
        self.setColor(QPalette.Button, QColor(53, 53, 53))
        self.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        self.setColor(QPalette.BrightText, QColor(255, 0, 0))
        self.setColor(QPalette.Link, QColor(42, 130, 218))
        self.setColor(QPalette.Highlight, QColor(42, 130, 218))
        self.setColor(QPalette.HighlightedText, QColor(0, 0, 0))


class SideMenu(QWidget):
    PAGES = ["Sniffer", "BotFM"]

    def __init__(self, parent, on_change_page: Callable[[int], None]) -> None:
        super().__init__(parent)
        self.setFixedWidth(100)

        v_layout = QVBoxLayout()
        v_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(v_layout)

        list_widget = QListWidget(parent=self)

        for index, page_name in enumerate(self.PAGES):
            page_link = ListWidgetItem()
            page_link.setText(page_name)
            list_widget.addItem(page_link)
            if index == 0:
                page_link.setSelected(True)

        list_widget.currentRowChanged.connect(on_change_page)
        v_layout.addWidget(list_widget)
