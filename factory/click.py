import time

import win32gui
import win32api
import win32con


class Click:
    LINES_POS: tuple = (251, 282, 313, 344, 375, 406, 437, 468, 499, 530, 561, 592, 623)
    COLUMNS_POS: tuple = (891, 930, 969)
    POS_EXO_RUNE = win32api.MAKELONG(1050, 150)
    FUSION_RUNE_EXO = win32api.MAKELONG(800, 170)
    NICKNAME: str = "Ezrealeeuu"
    TIME_CLICK: float = 0.1

    def __init__(self):
        self.__window_name = ""
        self.find_windows_name()

    @property
    def windows_name(self) -> str:
        return self.__window_name

    @windows_name.setter
    def windows_name(self, value : str):
        self.__window_name = value

    def click_auto(self, x: int, y: int):
        time.sleep(self.TIME_CLICK)
        hwnd = win32gui.FindWindow(None, self.windows_name)
        l_param = win32api.MAKELONG(x, y)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, l_param)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, l_param)

    def click_rune(self, num_column: int, num_line: int):
        self.click_auto(self.COLUMNS_POS[num_column], self.LINES_POS[num_line])

    def click_exo(self):
        hwnd = win32gui.FindWindow(None, self.windows_name)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, self.POS_EXO_RUNE)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, self.POS_EXO_RUNE)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, self.POS_EXO_RUNE)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, self.POS_EXO_RUNE)

        time.sleep(0.5)

        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, self.FUSION_RUNE_EXO)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, self.FUSION_RUNE_EXO)

    def find_windows_name(self):
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                if self.NICKNAME in win32gui.GetWindowText(hwnd):
                    self.windows_name = win32gui.GetWindowText(hwnd)

        win32gui.EnumWindows(winEnumHandler, None)
