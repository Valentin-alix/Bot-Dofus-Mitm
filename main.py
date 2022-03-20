import threading
from gui import interface
from gui.interface import Interface
from models.sniffer import Sniffer

if __name__ == '__main__':

    interface.interface = Interface()
    sniffer = Sniffer()

    interface_thread = threading.Thread(target=interface.interface.window)
    sniffer_thread = threading.Thread(target=sniffer.launch_sniffer)

    interface_thread.start()
    sniffer_thread.start()

    interface.interface.root.mainloop()
