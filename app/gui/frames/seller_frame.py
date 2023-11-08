from queue import Empty
from modules.hdv.buying_hdv import BuyingHdv
from types_ import ThreadsInfos
from gui.components import (
    ButtonIcon,
    DetailMessageDialog,
    Frame,
    GroupBox,
    Header,
    HorizontalLayout,
    VerticalLayout,
)
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
from PyQt5.QtCore import (
    QEvent,
    QObject,
    QRunnable,
    QSize,
    QTimer,
    Qt,
    QThreadPool,
    pyqtSignal,
)
from PyQt5.QtGui import QCloseEvent, QColor, QPalette, QFont


class SellerFrame(Frame):
    def __init__(self, threads_infos: ThreadsInfos, name: str) -> None:
        super().__init__(name)
        self.threads_infos = threads_infos

        self.main_frame_layout = VerticalLayout()
        self.main_frame_layout.setSpacing(0)

        self.set_header()
        self.setup_content()

        self.setLayout(self.main_frame_layout)

    def set_header(self):
        self.header = Header()
        self.header.setTitle("Hdv pour vendre")
        self.header.button_play.clicked.connect(lambda: self.on_update_do_play(True))
        self.header.button_stop.clicked.connect(lambda: self.on_update_do_play(False))
        self.main_frame_layout.addWidget(self.header)
        self.update_state_buttons()

    def setup_content(self):
        self.box_content = GroupBox()
        self.box_content.setTitle("Informations")
        self.box_content.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_content = VerticalLayout()
        self.layout_content.setContentsMargins(0, 0, 0, 0)
        self.layout_content.addStretch()
        self.layout_content.setDirection(QBoxLayout.Direction.BottomToTop)
        self.box_content.setLayout(self.layout_content)

        self.label_sellable_objects = QLabel()
        self.label_sellable_objects.setText("bientot")
        self.label_sellable_objects.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout_content.addWidget(self.label_sellable_objects)

        self.main_frame_layout.addWidget(self.box_content)

    def update_state_buttons(self):
        self.header.do_play(self.threads_infos.get("event_play_hdv_selling").is_set())

    def on_update_do_play(self, do_play: bool):
        if do_play:
            self.threads_infos["event_play_hdv_selling"].set()
            self.update_state_buttons()
        else:
            self.threads_infos["event_play_hdv_selling"].clear()
            self.update_state_buttons()
