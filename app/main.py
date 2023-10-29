import logging
import os
from pathlib import Path
from threading import Thread

from network.sniffer import Sniffer

if not (
    os.path.exists(path_logs := os.path.join(Path(__file__).parent.parent, "logs"))
):
    os.makedirs(path_logs)
logging.basicConfig(
    level=logging.INFO,
    filename=os.path.join(path_logs, "bot.log"),
    filemode="w+",
    format="%(levelname)s-%(funcName)s-%(lineno)d:%(message)s",
)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    logger.info("Starting Bot")

    sniffer = Sniffer()

    sniffer_thread = Thread(target=sniffer.launch_sniffer, daemon=False)

    sniffer_thread.start()
