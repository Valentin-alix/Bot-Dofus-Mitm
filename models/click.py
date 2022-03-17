import time

import win32gui
import win32api
import win32con
from pywinauto import Desktop


def find_good_dofus_window(nickname: str):
    windows = Desktop(backend="uia").windows()
    for window in windows:
        if nickname in window.window_text():
            return window.window_text()


class Click:

    def __init__(self, nickname):
        self.__lines_pos = (251, 282, 313, 344, 375, 406, 437, 468, 499, 530, 561, 592, 623)
        self.__columns_pos = (891, 930, 969)
        self.__pos_exo_rune = win32api.MAKELONG(1050, 150)
        self.__fusion_rune_exo = win32api.MAKELONG(800, 170)
        self.__window_name = find_good_dofus_window(nickname)

    @property
    def lines_pos(self):
        return self.__lines_pos

    @property
    def columns_pos(self):
        return self.__columns_pos

    @property
    def pos_exo_rune(self):
        return self.__pos_exo_rune

    @property
    def fusion_rune_exo(self):
        return self.__fusion_rune_exo

    @property
    def window_name(self):
        return self.__window_name

    def click_auto(self, x, y):
        hwnd = win32gui.FindWindow(None, self.window_name)
        l_param = win32api.MAKELONG(x, y)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, l_param)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, l_param)

    def click_rune(self, num_column: int, num_line: int):
        self.click_auto(self.columns_pos[num_column], self.lines_pos[num_line])

    def click_exo(self):
        hwnd = win32gui.FindWindow(None, self.window_name)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, self.pos_exo_rune)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, self.pos_exo_rune)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, self.pos_exo_rune)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, self.pos_exo_rune)

        time.sleep(0.5)

        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, self.fusion_rune_exo)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, self.fusion_rune_exo)

        time.sleep(0.5)
