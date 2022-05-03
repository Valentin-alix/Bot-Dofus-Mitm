import time

import win32gui
import win32api
import win32con

LINES_POS: tuple = (251, 282, 313, 344, 375, 406, 437, 468, 499, 530, 561, 592, 623)
COLUMNS_POS: tuple = (891, 930, 969)
LINES_HDV: tuple = (160, 195, 230, 265, 300, 335, 370, 405, 440, 475, 510, 545, 580, 615)
SCROLL_HDV: tuple = (220, 290, 360, 430, 500, 570, 640)
POS_EXO_RUNE = win32api.MAKELONG(1050, 150)
FUSION_RUNE_EXO = win32api.MAKELONG(800, 170)
NICKNAME: str = "Ezrealeeuu"
TIME_CLICK: float = 0.1
window_name: str = ""


def click_auto(x: int, y: int) -> None:
    global window_name
    time.sleep(TIME_CLICK)
    hwnd = win32gui.FindWindow(None, window_name)
    l_param = win32api.MAKELONG(x, y)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, l_param)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, l_param)


def click_rune(num_column: int, num_line: int) -> None:
    global COLUMNS_POS
    global LINES_POS
    click_auto(COLUMNS_POS[num_column], LINES_POS[num_line])


def click_exo() -> None:
    global window_name
    global POS_EXO_RUNE
    global FUSION_RUNE_EXO
    hwnd = win32gui.FindWindow(None, window_name)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, POS_EXO_RUNE)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, POS_EXO_RUNE)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, POS_EXO_RUNE)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, POS_EXO_RUNE)

    time.sleep(0.5)

    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, FUSION_RUNE_EXO)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, FUSION_RUNE_EXO)


def find_windows_name() -> None:
    def win_enum_handler(hwnd, ctx):
        global window_name
        global NICKNAME
        if win32gui.IsWindowVisible(hwnd):
            if NICKNAME in win32gui.GetWindowText(hwnd):
                window_name = win32gui.GetWindowText(hwnd)

    win32gui.EnumWindows(win_enum_handler, None)