from bot.factory import action, graphic
from bot.network.sniffer import Sniffer
from static.assets.colors import Colors

if __name__ == '__main__':
    try:
        print(Colors.WARNING + "Not fully implemented yet !" + Colors.RESET)
        action.bot_hdv_is_playing = True
        sniffer = Sniffer()
        sniffer.launch_sniffer()
    except Exception as e:
        exit()
    finally:
        graphic.test_graphic()
