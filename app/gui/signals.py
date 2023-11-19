from PyQt5.QtCore import QObject, pyqtSignal


class AppSignals(QObject):
    on_close = pyqtSignal()
    on_parsed_msg_info = pyqtSignal(dict)
    on_new_server_id = pyqtSignal()
    on_new_scraping_current_state = pyqtSignal(dict)
    on_new_sale_info = pyqtSignal()
