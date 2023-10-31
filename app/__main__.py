import logging
import logging.config
import os
from pathlib import Path
from threading import Thread

from sqlalchemy import create_engine
from init import update_resources
from database.models import Base
from logs.config import LOGGING_CONFIG

from network.sniffer import Sniffer


logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    engine = create_engine(
        f"sqlite:///{os.path.join(Path(__file__).parent, 'database', 'sqlite3.db')}",
        echo=False,
    )
    Base.metadata.create_all(engine)

    update_resources(engine)

    sniffer = Sniffer()
    sniffer_thread = Thread(target=sniffer.launch_sniffer, daemon=False)
    sniffer_thread.start()
