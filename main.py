import logging
from queue import Queue
from threading import Event, Thread

import eel

from bot.bot_fm import BotFM
from databases.database import Database
from network.sniffer import Sniffer

queue_play_item: Queue = Queue()

@eel.expose
def play_item(item_name):
    queue_play_item.put(item_name)

if __name__ == "__main__":

    eel.init('gui')
    logging.basicConfig(level=logging.INFO, filename="logs/bot.log", filemode="w+", format="%(asctime)s - %("
                                                                                           "levelname)s - %(message)s")
    logger = logging.getLogger(__name__)
    logger.info("Starting Bot")

    database = Database()
    bot_fm = BotFM(database, "Ezrealeeuu", queue_play_item)
    sniffer = Sniffer(database)

    sniffer_thread = Thread(target=sniffer.launch_sniffer, daemon=True)
    bot_fm_thread = Thread(target=bot_fm.start, daemon=True)

    sniffer_thread.start()
    bot_fm_thread.start()
    eel.start('templates/home.html', jinja_templates='templates', block=True)
