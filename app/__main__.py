import argparse
import logging.config
import os.path
import sys
from pathlib import Path
from threading import Thread

from PyQt5.QtCore import QThread

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.gui.signals import AppSignals
from app.types_.models.common import BotInfo
from gui.app import Application, MainWindow
from logs.config import LOGGING_CONFIG
from network.mitm import Mitm
from network.sniffer import Sniffer

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)


def run_migrations():
    current_path = os.getcwd()
    os.chdir(os.path.join(os.path.join(Path(__file__).parent)))
    os.system("alembic revision --autogenerate")
    os.system("alembic upgrade head")
    os.chdir(current_path)


if __name__ == "__main__":
    arg_parsed = argparse.ArgumentParser()
    arg_parsed.add_argument(
        "-s", "--sniffer", required=False, help="y/n to use sniffer", default="n"
    )
    args = vars(arg_parsed.parse_args())

    run_migrations()

    app_signals = AppSignals()
    bot_info = BotInfo()
    bot_info.sniffer_info.is_playing_event.set()

    if args["sniffer"] == "y":
        sniffer = Sniffer(bot_info)
        sniffer_thread = Thread(target=sniffer.launch_sniffer, daemon=True)
        sniffer_thread.start()
    else:
        mitm_thread = QThread()
        mitm = Mitm(bot_info, app_signals)
        mitm.moveToThread(mitm_thread)
        mitm_thread.started.connect(mitm.launch)
        mitm_thread.start()

    app = Application(sys.argv)

    main_window = MainWindow(bot_info, app_signals, args["sniffer"] == "y")
    sys.exit(app.exec_())
