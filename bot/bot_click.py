from dataclasses import dataclass, field
from threading import Event
import time

import win32api
import win32con
import win32gui

LINES_POS: tuple = (251, 282, 313, 344, 375, 406, 437, 468, 499, 530, 561, 592, 623)
COLUMNS_POS: tuple = (891, 930, 969)
POS_EXO_RUNE = win32api.MAKELONG(1050, 150)
FUSION_RUNE_EXO = win32api.MAKELONG(800, 170)

@dataclass
class BotClick:
    nickname: str
    event_is_playing: Event
    event_ready: Event
    event_magic: Event
    event_move: Event
    windows_name: str = field(default=None, init=False)
    hwnd: int = field(default=None, init=False)

    def click(self, l_param: win32api.MAKELONG) -> None:
        win32gui.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, l_param)
        win32gui.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, None, l_param)

    def click_on_rune(self, num_column, num_line) -> None:
        self.event_ready.clear()
        self.event_magic.clear()
        before_click = time.perf_counter()
        self.click(win32api.MAKELONG(COLUMNS_POS[num_column], LINES_POS[num_line]))
        while self.event_is_playing.is_set() and not self.event_ready.is_set() and not self.event_magic.is_set():
            time.sleep(0.001)
            if time.perf_counter() - before_click > 5.0:
                self.click(win32api.MAKELONG(COLUMNS_POS[num_column], LINES_POS[num_line]))
                before_click = time.perf_counter()
        
    
    def click_exo(self) -> None:
        self.event_ready.clear()
        self.event_move.clear()
        before_click = time.perf_counter()
        self.click(POS_EXO_RUNE)
        self.click(POS_EXO_RUNE)
        while self.event_is_playing.is_set() and not self.event_move.is_set():
            time.sleep(0.001)
            if time.perf_counter() - before_click > 5.0:
                self.click(POS_EXO_RUNE)
                self.click(POS_EXO_RUNE)
                before_click = time.perf_counter()
        before_click = time.perf_counter()
        time.sleep(0.5)
        self.click(FUSION_RUNE_EXO)
        while self.event_is_playing.is_set() and not self.event_ready.is_set():
            time.sleep(0.001)
            if time.perf_counter() - before_click > 5.0:
                self.click(FUSION_RUNE_EXO)
                before_click = time.perf_counter()
        
    def find_windows_name(self) -> None:
        def win_enum_handler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd) and self.nickname in win32gui.GetWindowText(hwnd):
                self.windows_name = win32gui.GetWindowText(hwnd)

        win32gui.EnumWindows(win_enum_handler, None)
