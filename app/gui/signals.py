from PyQt5.QtCore import QObject, pyqtSignal


class AppSignals(QObject):
    close = pyqtSignal()
