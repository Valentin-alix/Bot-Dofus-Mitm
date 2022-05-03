import logging
import threading

from bot.factory import action, hdv_graphic, click
from bot.network.sniffer import Sniffer

if __name__ == '__main__':
    logging.basicConfig(filename="../logs/bot_fm.log", level=logging.INFO)
    click.find_windows_name()
    action.bot_hdv_is_playing = True
    sniffer = Sniffer()
    click_thread = threading.Thread(target=action.click_hdv_runes())
    sniffer_thread = threading.Thread(target=sniffer.launch_sniffer())
    try:
        click_thread.start()
        sniffer_thread.start()
    except Exception as e:
        exit()
    finally:
        hdv_graphic.save_graphic()
