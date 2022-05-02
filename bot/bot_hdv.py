import threading

from bot.factory import action
from bot.network.sniffer import Sniffer
from static.assets.colors import Colors

if __name__ == '__main__':
    print(Colors.WARNING + "Not fully implemented yet !" + Colors.RESET)
    action.bot_hdv_is_playing = True
    sniffer = Sniffer()
    sniffer_thread = threading.Thread(target=sniffer.launch_sniffer)
    sniffer_thread.start()
