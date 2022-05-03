import logging
import threading
from bot.gui import interface
from bot.gui.interface import Interface
from network.sniffer import Sniffer

if __name__ == '__main__':
    logging.basicConfig(filename="../logs/bot_fm.log", level=logging.INFO)

    interface.interface = Interface()
    sniffer = Sniffer()

    interface_thread = threading.Thread(target=interface.interface.window)
    sniffer_thread = threading.Thread(target=sniffer.launch_sniffer)

    interface_thread.start()
    sniffer_thread.start()

    interface.interface.root.mainloop()
