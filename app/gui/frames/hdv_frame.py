from queue import Empty
from types_.interface import CurrentHdv, ThreadsInfos
from gui.components import (
    ButtonIcon,
    DetailMessageDialog,
    Frame,
    GroupBox,
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


class HDVFrame(Frame):
    def __init__(self, threads_infos: ThreadsInfos, name: str) -> None:
        super().__init__(name)
        self.threads_infos = threads_infos

        self.main_frame_layout = VerticalLayout()
        self.main_frame_layout.setSpacing(0)

        self.set_header_sniffer()
        self.setup_processing_content()

        self.setLayout(self.main_frame_layout)

        self.hdv_name: str | None = None

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_remaining_objects_signal)
        self.timer.start(100)

    def check_remaining_objects_signal(self):
        try:
            remaining_hdv = self.threads_infos.get("queue_current_hdv").get_nowait()
            if remaining_hdv is not None:
                self.set_hdv_text(remaining_hdv)
            else:
                self.clear_hdv_text()
        except Empty:
            pass

    def set_header_sniffer(self):
        self.box_header = GroupBox(with_title=False)

        self.header_layout = HorizontalLayout()
        self.header_layout.setSpacing(8)
        self.box_header.setLayout(self.header_layout)
        self.box_header.setFixedHeight(80)

        # Buttons
        self.button_play = ButtonIcon("play.svg")
        self.button_play.clicked.connect(self.on_play)
        self.header_layout.addWidget(self.button_play)

        self.button_stop = ButtonIcon("stop")
        self.button_stop.clicked.connect(self.on_stop)
        self.header_layout.addWidget(self.button_stop)

        self.update_state_buttons()

        self.main_frame_layout.addWidget(self.box_header)

    def setup_processing_content(self):
        self.label_remaining_objects = QLabel()
        self.label_remaining_objects.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_frame_layout.addWidget(self.label_remaining_objects)

    def update_state_buttons(self):
        if self.threads_infos.get("event_play_hdv").is_set():
            self.button_play.set_active_button()
            self.button_stop.set_inactive_button()
        else:
            self.button_play.set_inactive_button()
            self.button_stop.set_active_button()

    def set_hdv_text(self, current_hdv: CurrentHdv):
        self.label_remaining_objects.setText(
            f"Nombre d'objets restantes à traiter dans la catégorie : {current_hdv.get('objects_remaining')}\n\
            Nombre de catégories restantes : {current_hdv.get('categories_remaining')}"
        )

    def clear_hdv_text(self):
        self.label_remaining_objects.setText("")

    def on_play(self):
        self.threads_infos["event_play_hdv"].set()
        self.update_state_buttons()

    def on_stop(self):
        self.threads_infos["event_play_hdv"].clear()
        self.update_state_buttons()
