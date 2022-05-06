import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pandas

from bot.bot_click import BotClick

LINES_HDV: tuple = (160, 195, 230, 265, 300, 335, 370, 405, 440, 475, 510, 545, 580, 615)
SCROLL_HDV: tuple = (220, 290, 360, 430, 500, 570, 640)
FILENAME: str = 'static/resources/prices_runes.csv'


class BotHDV(BotClick):
    # FIXME
    """def click_hdv_runes(self) -> None:
        for scroll_y in SCROLL_HDV:
            for line in LINES_HDV:
                before_click_time: float = time.perf_counter()
                self.click(win32api.MAKELONG(891, line))
                while not self.event_ready.is_set() and not self.event_is_playing.is_set():
                    if (time.perf_counter() - before_click_time) > 5.0:
                        self.click(win32api.MAKELONG(891, line))
                        before_click_time: float = time.perf_counter()
                    else:
                        time.sleep(0.001)
                time.sleep(1)
                before_click_time: float = time.perf_counter()
                self.click(win32api.MAKELONG(891, line))
                while not self.event_ready.is_set() and self.event_is_playing.is_set():
                    if (time.perf_counter() - before_click_time) > 5.0:
                        self.click(win32api.MAKELONG(891, line))
                        before_click_time: float = time.perf_counter()
                    else:
                        time.sleep(0.001)
                time.sleep(1)
            before_click_time: float = time.perf_counter()
            self.click(win32api.MAKELONG(969, scroll_y))
            while not self.event_ready.is_set() and self.event_is_playing.is_set():
                if (time.perf_counter() - before_click_time) > 5.0:
                    self.click(win32api.MAKELONG(969, scroll_y))
                    before_click_time: float = time.perf_counter()
                else:
                    time.sleep(0.001)"""

    @staticmethod
    def maj_csv_value(time_when_maj: datetime.date, type_rune: str, cost: int) -> None:
        if BotHDV.check_if_same_day(type_rune):
            return
        data_frame = pandas.DataFrame(pandas.read_csv(FILENAME, sep=';'), columns=['Time', 'Type', 'Costs'])
        data_frame = pandas.concat(
            [data_frame, pandas.DataFrame({'Time': [time_when_maj], 'Type': [type_rune], 'Costs': [cost]})])
        data_frame.to_csv(FILENAME, mode='w', index=False, header=True, sep=';')

    @staticmethod
    def check_if_same_day(type_rune: str) -> bool:
        data = pandas.read_csv(FILENAME, sep=';')
        data.query(f"Type == \"{type_rune}\"", inplace=True)

        return any(str(time_rune) == str(datetime.date.today()) for time_rune in
                   pandas.to_datetime(data['Time']).dt.strftime('%Y-%m-%d'))

    @staticmethod
    def save_graphic() -> None:
        data_frame = pandas.read_csv(FILENAME, sep=';')
        data_frame_test = data_frame.copy()
        data_frame_test.drop_duplicates(subset="Type", keep='first', inplace=True)
        fig, ax = plt.subplots()
        [ax.plot(data_frame[data_frame.Type == type_rune].Time, data_frame[data_frame.Type == type_rune].Costs,
                 label=type_rune) for type_rune in data_frame_test['Type']]

        ax.set_xlabel("Time")
        ax.set_ylabel("Costs")
        ax.legend(loc='best')
        plt.legend(loc=2, prop={'size': 3.5})
        plt.yticks(np.arange(0.0, 45000.0, 2000.0))
        plt.savefig(fname="static/assets/images/cost_rune_graph.png", dpi=130)
        plt.close()
