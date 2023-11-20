from typing import TYPE_CHECKING

from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QSizePolicy

from app.gui.components.common import Widget, ButtonIcon
from app.gui.components.organization import HorizontalLayout

if TYPE_CHECKING:
    from app.gui.app import MainWindow


class HeaderItem(ButtonIcon):
    def __init__(self, height=50, icon_size=20, text: str = "", *args, **kwargs) -> None:
        super().__init__(height=height, icon_size=icon_size, *args, **kwargs)
        self.setFixedWidth(50)

    def set_active_button(self):
        self.setObjectName("around-app-active")
        self.style().unpolish(self)
        self.style().polish(self)

    def set_inactive_button(self):
        self.setObjectName("around-app-inactive")
        self.style().unpolish(self)
        self.style().polish(self)


class Header(Widget):
    HEIGHT = 50

    def __init__(self, parent: 'MainWindow', *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.installEventFilter(self)
        self.parent = parent
        self.is_full_screen = False

        self.set_object_name("around-app")
        self.setAttribute(Qt.WA_StyledBackground, True)  # to apply style to whole widget
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setFixedHeight(self.HEIGHT)

        self.main_layout = HorizontalLayout()
        self.main_layout.setAlignment(Qt.AlignRight)
        self.setLayout(self.main_layout)

        self.minimize_button = HeaderItem(height=self.HEIGHT, filename="minus.svg", parent=self)
        self.minimize_button.clicked.connect(self.on_minimize)
        self.minimize_button.set_inactive_button()
        self.main_layout.addWidget(self.minimize_button)

        self.resize_button = HeaderItem(height=self.HEIGHT, icon_size=15, filename="square_big.svg", parent=self)
        self.resize_button.clicked.connect(self.on_resize)
        self.resize_button.set_inactive_button()
        self.main_layout.addWidget(self.resize_button)

        self.quit_button = HeaderItem(height=self.HEIGHT, filename="quit.svg", parent=self)
        self.quit_button.clicked.connect(self.on_quit)
        self.quit_button.set_inactive_button()
        self.main_layout.addWidget(self.quit_button)

    def on_minimize(self):
        self.parent.showMinimized()

    def on_resize(self):
        if not self.is_full_screen:
            self.parent.showFullScreen()
        else:
            self.parent.showNormal()
        self.is_full_screen = not self.is_full_screen

    def on_quit(self):
        self.parent.close()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseMove:
            if event.buttons() == Qt.LeftButton:
                self.parent.move(self.parent.pos() + event.globalPos() - self.drag_position)
                self.drag_position = event.globalPos()
                event.accept()
                return True
        elif event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos()
            event.accept()
            return True
        return super().eventFilter(obj, event)
