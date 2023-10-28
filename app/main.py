import logging
import os
import sys
from pathlib import Path
from queue import Queue
from threading import Event, Thread

from bot.bot_fm import BotFM
from network.sniffer import Sniffer

if not (
    os.path.exists(path_logs := os.path.join(Path(__file__).parent.parent, "logs"))
):
    os.makedirs(path_logs)
logging.basicConfig(
    level=logging.INFO,
    filename=os.path.join(path_logs, "bot.log"),
    filemode="w+",
    format=" %(filename)s: %(asctime)s - %(" "levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    logger.info("Starting Bot")

    sniffer = Sniffer()

    sniffer_thread = Thread(target=sniffer.launch_sniffer, daemon=False)

    sniffer_thread.start()
