import win32api

from static.assets.colors import Colors

FILTER_DOFUS: str = 'tcp port 5555'
TITLE: str = 'Bot FM'
BACKGROUND_COLOR: str = Colors.background_color
WIDTH_SIZE: int = 900
HEIGHT_SIZE: int = 700
ICON_MENU_SIZE: int = 20
ICON_SIZE: int = 26
LINES_POS: tuple = (251, 282, 313, 344, 375, 406, 437, 468, 499, 530, 561, 592, 623)
COLUMNS_POS: tuple = (891, 930, 969)
LINES_HDV: tuple = (160, 195, 230, 265, 300, 335, 370, 405, 440, 475, 510, 545, 580, 615)
SCROLL_HDV: tuple = (220, 290, 360, 430, 500, 570, 640)
POS_EXO_RUNE = win32api.MAKELONG(1050, 150)
FUSION_RUNE_EXO = win32api.MAKELONG(800, 170)
NICKNAME: str = "Ezrealeeuu"
TIME_CLICK: float = 0.1
HOST: str = "localhost"
LOGIN: str = "root"
PASSWORD: str = ""
DATABASE_NAME: str = "bot_sniffer"
