import logging
from queue import Queue
from threading import Event, Thread
from time import time

import eel

from bot.bot_fm import BotFM
from databases.database import *
from network.sniffer import Sniffer

logging.basicConfig(level=logging.INFO, filename="logs/bot.log", filemode="w+", format=" %(filename)s: %(asctime)s - %("
                                                                                           "levelname)s - %(message)s")
logger = logging.getLogger(__name__)

queue_target_item: Queue = Queue()
queue_actual_item: Queue = Queue()
event_ready: Event = Event()
event_move: Event = Event()
event_is_playing: Event = Event()

@eel.expose
def play_item(item_name):
    event_is_playing.set()
    queue_target_item.put(item_name)

@eel.expose
def stop_item():
    event_is_playing.clear()
    while not queue_actual_item.empty():
        queue_actual_item.get()
    while not queue_target_item.empty():
        queue_target_item.get()
    event_ready.clear()
    event_move.clear()

if __name__ == "__main__":
    eel.init('gui')
    
    logger.info("Starting Bot")

    bot_fm = BotFM("Ezrealeeuu", event_is_playing, event_ready, event_move, queue_target_item, queue_actual_item)
    sniffer = Sniffer(queue_actual_item, event_ready, event_move, event_is_playing)

    sniffer_thread = Thread(target=sniffer.launch_sniffer, daemon=True)
    bot_fm_thread = Thread(target=bot_fm.start, daemon=True)
    
    sniffer_thread.start()
    bot_fm_thread.start()
    
    eel.start('templates/home.html', jinja_templates='templates', block=True)
