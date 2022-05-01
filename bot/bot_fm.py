import datetime
import logging
import threading

from gui.interface import Interface
from network.sniffer import Sniffer

if __name__ == '__main__':
    executed_time = str(datetime.datetime.now()).replace(':', '.')
    logging.basicConfig(filename=f"../logs/{str(executed_time)}.log", level=logging.INFO)

    interface = Interface()
    sniffer = Sniffer()

    interface_thread = threading.Thread(target=interface.window)
    sniffer_thread = threading.Thread(target=sniffer.launch_sniffer)

    interface_thread.start()
    sniffer_thread.start()

    interface.root.mainloop()
