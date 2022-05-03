import time
from static import constant
import win32gui
import win32api
import win32con

window_name: str = ""


def click_auto(x: int, y: int) -> None:
    global window_name
    time.sleep(constant.TIME_CLICK)
    hwnd = win32gui.FindWindow(None, window_name)
    l_param = win32api.MAKELONG(x, y)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, l_param)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, l_param)


def click_rune(num_column: int, num_line: int) -> None:
    click_auto(constant.COLUMNS_POS[num_column], constant.LINES_POS[num_line])


def click_exo() -> None:
    global window_name
    hwnd = win32gui.FindWindow(None, window_name)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, constant.POS_EXO_RUNE)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, constant.POS_EXO_RUNE)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, constant.POS_EXO_RUNE)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, constant.POS_EXO_RUNE)

    time.sleep(0.5)

    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, constant.FUSION_RUNE_EXO)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, constant.FUSION_RUNE_EXO)


def find_windows_name() -> None:
    def win_enum_handler(hwnd, ctx):
        global window_name
        if win32gui.IsWindowVisible(hwnd):
            if constant.NICKNAME in win32gui.GetWindowText(hwnd):
                window_name = win32gui.GetWindowText(hwnd)

    win32gui.EnumWindows(win_enum_handler, None)
