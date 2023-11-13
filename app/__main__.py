import argparse
import logging.config
import os.path
import sys
from pathlib import Path
from threading import Thread

from alembic import command
from alembic.config import Config

from app.database.models import get_engine

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.types_ import BotInfo
from gui.app import Application, MainWindow
from logs.config import LOGGING_CONFIG
from network.mitm import Mitm
from network.sniffer import Sniffer

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)


def run_migrations():
    current_path = os.getcwd()
    os.chdir(os.path.join(os.path.join(Path(__file__).parent)))
    engine = get_engine()
    alembic_cfg = Config(os.path.join(Path(__file__).parent, "alembic.ini"))
    with engine.begin() as connection:
        command.revision(alembic_cfg, autogenerate=True)
        command.upgrade(alembic_cfg, "head")

    os.chdir(current_path)


if __name__ == "__main__":
    arg_parsed = argparse.ArgumentParser()
    arg_parsed.add_argument(
        "-s", "--sniffer", required=False, help="y/n to use sniffer", default="n"
    )
    arg_parsed.add_argument(
        "-m", "--migrations", required=False, help="y/n to make migrations", default="n"
    )
    args = vars(arg_parsed.parse_args())

    if args["migrations"] == "y":
        run_migrations()

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
