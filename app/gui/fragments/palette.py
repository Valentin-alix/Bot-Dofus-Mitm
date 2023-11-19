from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor


class DarkThemePalette(QPalette):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setColor(QPalette.Window, QColor(31, 35, 75))
        self.setColor(QPalette.Base, QColor(50, 50, 50))  # bg for entry widget (tables, edit etc)
        self.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        self.setColor(QPalette.ToolTipBase, Qt.black)
        self.setColor(QPalette.Button, QColor(39, 39, 39))
        self.setColor(QPalette.Link, QColor(42, 130, 218))
        self.setColor(QPalette.Highlight, QColor(42, 130, 218))
