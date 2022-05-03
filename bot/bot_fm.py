import logging
import threading

from bot.gui import ui
from bot.gui.ui import Ui
from network.sniffer import Sniffer

if __name__ == '__main__':
    logging.basicConfig(filename="../logs/bot_fm.log", level=logging.INFO)

    ui.interface = Ui()
    sniffer = Sniffer()

    interface_thread = threading.Thread(target=ui.interface.window)
    sniffer_thread = threading.Thread(target=sniffer.launch_sniffer)

    interface_thread.start()
    sniffer_thread.start()

    ui.interface.mainloop()
