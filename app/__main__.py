import argparse
import logging.config
import os.path
import sys
from queue import Queue
from threading import Event, Lock, Thread

from gui.app import Application, MainWindow
from logs.config import LOGGING_CONFIG
from network.mitm import Mitm
from network.sniffer import Sniffer
from types_ import ThreadsInfos

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

if __name__ == "__main__":
    arg_parsed = argparse.ArgumentParser()
    arg_parsed.add_argument(
        "-s", "--sniffer", required=False, help="y/n to use sniffer", default="n"
    )
    args = vars(arg_parsed.parse_args())

    threads_infos: ThreadsInfos = {
        "event_play_sniffer": Event(),
        "event_play_hdv_scrapping": Event(),
        "event_play_hdv_selling": Event(),
        "event_close": Event(),
        "event_connected": Event(),
        "queue_msg_to_send": Queue(),
        "queue_handler_message": Queue(),
        "queue_for_sale_object": Queue(),
        "character_with_lock": {"lock": Lock(), "character": None},
        "buying_hdv_with_lock": {"lock": Lock(), "buying_hdv": None},
        "selling_hdv_with_lock": {"lock": Lock(), "selling_hdv": None},
        "server_id_with_lock": {"lock": Lock(), "server_id": None},
    }
    threads_infos["event_play_sniffer"].set()

    if args["sniffer"] == "y":
        sniffer = Sniffer(threads_infos)
        sniffer_thread = Thread(target=sniffer.launch_sniffer, daemon=True)
        sniffer_thread.start()
    else:
        mitm = Mitm(threads_infos)
        mitm_thread = Thread(target=mitm.launch, daemon=True)
        mitm_thread.start()

    app = Application(sys.argv)
    main_window = MainWindow(threads_infos)
    sys.exit(app.exec_())
