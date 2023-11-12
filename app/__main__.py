import argparse
import logging.config
import os.path
import sys
from threading import Thread

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.types_ import BotInfo
from gui.app import Application, MainWindow
from logs.config import LOGGING_CONFIG
from network.mitm import Mitm
from network.sniffer import Sniffer

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    arg_parsed = argparse.ArgumentParser()
    arg_parsed.add_argument(
        "-s", "--sniffer", required=False, help="y/n to use sniffer", default="n"
    )
    args = vars(arg_parsed.parse_args())

    bot_info = BotInfo()
    bot_info.sniffer_info.is_playing_event.set()

    if args["sniffer"] == "y":
        sniffer = Sniffer(bot_info)
        sniffer_thread = Thread(target=sniffer.launch_sniffer, daemon=True)
        sniffer_thread.start()
    else:
        mitm = Mitm(bot_info)
        mitm_thread = Thread(target=mitm.launch, daemon=True)
        mitm_thread.start()

    app = Application(sys.argv)

    main_window = MainWindow(bot_info)
    sys.exit(app.exec_())
