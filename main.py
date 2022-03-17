import socket
import threading
import time

import pyshark as pyshark

from databases.database_management import DatabaseManagement
from gui import interface
from gui.interface import Interface
from models.sniffer import Sniffer

if __name__ == '__main__':
    '''db = DatabaseManagement()
    types_rune = ["Vitalité", "Portée", "Puissance", "Résistance Air"]
    values_rune = [136, 5, 10, 15]
    lines_rune = [0, 2, 1, 3]
    columns_rune = [1, 1, 0, 0]
    name_item = "Quatre-Feuilles"
    # db.insert_item(name_item)
    # db.insert_or_update_target_lines_item(name_item, types_rune, values_rune, lines_rune, columns_rune)
    interface = Interface()
    interface.database.close()'''

    interface.interface = Interface()
    sniffer = Sniffer()

    interface_thread = threading.Thread(target=interface.interface.window)
    sniffer_thread = threading.Thread(target=sniffer.launch_sniffer)

    interface_thread.start()
    sniffer_thread.start()

    interface.interface.root.mainloop()
