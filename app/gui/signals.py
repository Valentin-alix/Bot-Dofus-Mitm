from PyQt5.QtCore import QObject, pyqtSignal


class AppSignals(QObject):
    on_close = pyqtSignal()
    on_parsed_msg_info = pyqtSignal(dict)
    on_new_server_id = pyqtSignal()
    on_new_scraping_current_state = pyqtSignal(dict)
    on_new_hdv_inventory_progression = pyqtSignal(dict)
    on_new_hdv_update_progression = pyqtSignal(dict)
    on_leaving_hdv = pyqtSignal()

    on_new_buying_hdv_playing_value = pyqtSignal()
    on_new_selling_hdv_inventory_playing_value = pyqtSignal()
    on_new_selling_hdv_update_playing_value = pyqtSignal()
