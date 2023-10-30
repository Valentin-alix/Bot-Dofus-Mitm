import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QGroupBox,
    QVBoxLayout,
    QHBoxLayout,
    QSizePolicy,
    QLabel,
    QDialogButtonBox,
    QDialog,
    QMessageBox,
    QColorDialog,
    QLayout,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        # Dark Theme
        super().__init__()
        self.setFixedSize(500, 500)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.black)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.black)
        self.setPalette(palette)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Bot dofus")
    app.setStyle("Fusion")

    main_window = MainWindow()

    main_box = QGroupBox(parent=main_window)
    main_box.setTitle("Messages reçus")
    main_box.setAlignment(Qt.AlignmentFlag.AlignCenter)

    vertical_layout = QVBoxLayout(main_box)

    def show_info_message_dialog(message_name):
        dlg = QDialog(main_window)
        dlg.setFixedSize(300, 300)
        dlg.setWindowTitle(f"{message_name} details")

        layout = QVBoxLayout(dlg)

        label = QLabel(text="zfedsc")
        label2 = QLabel(text="oheeee")

        label.setLayout(layout)
        label2.setLayout(layout)

        dlg.exec()

    for i in range(5):
        button = QPushButton(text="ExampleNetworkMessage", parent=main_box)
        vertical_layout.addWidget(button)
        button.clicked.connect(lambda state, i=i: show_info_message_dialog(i))

    main_window.setCentralWidget(main_box)
    main_window.show()
    app.exec_()
