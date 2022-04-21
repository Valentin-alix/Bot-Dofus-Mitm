import time

import win32gui
import win32api
import win32con


class Click:

    def __init__(self):
        self.__lines_pos = (251, 282, 313, 344, 375, 406, 437, 468, 499, 530, 561, 592, 623)
        self.__columns_pos = (891, 930, 969)
        self.__pos_exo_rune = win32api.MAKELONG(1050, 150)
        self.__fusion_rune_exo = win32api.MAKELONG(800, 170)
        self.__nickname = "Ezrealeeuu"
        self.__window_name = ""
        self.__time_click = 0.2
        self.find_windows_name()

    @property
    def lines_pos(self):
        return self.__lines_pos

    @property
    def columns_pos(self):
        return self.__columns_pos

    @property
    def windows_name(self):
        return self.__window_name

    @property
    def pos_exo_rune(self):
        return self.__pos_exo_rune

    @property
    def fusion_rune_exo(self):
        return self.__fusion_rune_exo

    @windows_name.setter
    def windows_name(self, value):
        self.__window_name = value

    @property
    def nickname(self):
        return self.__nickname

    @property
    def time_click(self):
        return self.__time_click

    def click_auto(self, x: int, y: int):
        time.sleep(self.time_click)
        hwnd = win32gui.FindWindow(None, self.windows_name)
        l_param = win32api.MAKELONG(x, y)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, l_param)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, l_param)

    def click_rune(self, num_column: int, num_line: int):
        self.click_auto(self.columns_pos[num_column], self.lines_pos[num_line])

    def click_exo(self):
        hwnd = win32gui.FindWindow(None, self.windows_name)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, self.pos_exo_rune)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, self.pos_exo_rune)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, self.pos_exo_rune)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, self.pos_exo_rune)

        time.sleep(0.5)

        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, self.fusion_rune_exo)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, self.fusion_rune_exo)

    def find_windows_name(self):
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                if self.nickname in win32gui.GetWindowText(hwnd):
                    self.windows_name = win32gui.GetWindowText(hwnd)

        win32gui.EnumWindows(winEnumHandler, None)
