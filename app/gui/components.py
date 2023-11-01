import pprint

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
    QListWidgetItem,
    QTextEdit,
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPalette

from network.models.message import Message


class ListWidgetItem(QListWidgetItem):
    def __init__(self) -> None:
        super().__init__()
        self.setSizeHint(QSize(90, 100))
        self.setTextAlignment(Qt.AlignmentFlag.AlignCenter)


class DetailMessageDialog(QDialog):
    def __init__(self, parent, message: Message) -> None:
        super().__init__(parent)
        self.setFixedSize(500, 300)
        self.setWindowTitle(f"{message.message_type}")

        main_layout = QVBoxLayout()

        from_client_label = QLabel(
            text="From client" if message.from_client else "From server"
        )
        main_layout.addWidget(from_client_label)

        text_edit = QTextEdit(self)
        text_edit.setPlainText(pprint.pformat(message.content))
        text_edit.setReadOnly(True)
        main_layout.addWidget(text_edit)

        self.setLayout(main_layout)
