import logging
import logging.config
import os
from pathlib import Path
import sys
from queue import Queue
from threading import Thread, Event

from sqlalchemy import create_engine
from gui.app import Application, MainWindow
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

    queue_handler_message = Queue()
    event_play_sniffer = Event()
    event_play_sniffer.set()

    sniffer = Sniffer(
        queue_handler_message=queue_handler_message,
        event_play_sniffer=event_play_sniffer,
    )
    sniffer_thread = Thread(target=sniffer.launch_sniffer, daemon=True)
    sniffer_thread.start()

    app = Application(sys.argv)
    main_window = MainWindow(
        queue_handler_message=queue_handler_message,
        event_play_sniffer=event_play_sniffer,
    )
    sys.exit(app.exec_())
