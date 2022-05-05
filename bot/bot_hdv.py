import datetime
import logging

import numpy as np
import pandas as pandas
import matplotlib.pyplot as plt

from bot.bot_click import BotClick

FILENAME: str = '..\\static\\resources\\prices_runes.csv'


class BotHDV(BotClick):
    # FIXME
    """def click_hdv_runes(self, ) -> None:
        # pass argument entre les 2 threads
        global bot_hdv_is_playing
        for scroll_y in constant.SCROLL_HDV:
            for line in constant.LINES_HDV:
                before_click_time: float = time.perf_counter()
                waiting_click = True
                click.click_auto(891, line)
                while click.waiting_click and bot_hdv_is_playing:
                    if (time.perf_counter() - before_click_time) > 5.0:
                        click.click_auto(891, line)
                        before_click_time: float = time.perf_counter()
                    else:
                        time.sleep(0.001)
                time.sleep(1)
                before_click_time: float = time.perf_counter()
                waiting_click = True
                click.click_auto(891, line)
                while click.waiting_click and bot_hdv_is_playing:
                    if (time.perf_counter() - before_click_time) > 5.0:
                        click.click_auto(891, line)
                        before_click_time: float = time.perf_counter()
                    else:
                        time.sleep(0.001)
                time.sleep(1)
            before_click_time: float = time.perf_counter()
            waiting_click = True
            click.click_auto(969, scroll_y)
            while waiting_click and bot_hdv_is_playing:
                if (time.perf_counter() - before_click_time) > 5.0:
                    click.click_auto(969, scroll_y)
                    before_click_time: float = time.perf_counter()
                else:
                    time.sleep(0.001)"""

    @staticmethod
    def maj_csv_value(time: datetime.date, type_rune: str, cost: int) -> None:
        data = pandas.read_csv(FILENAME, sep=';')
        data_frame = pandas.DataFrame(data, columns=['Time', 'Type', 'Costs'])
        data_new_row = pandas.DataFrame({'Time': [time], 'Type': [type_rune], 'Costs': [cost]})
        data_frame = pandas.concat([data_frame, data_new_row])
        data_frame.to_csv(FILENAME, mode='w', index=False, header=True, sep=';')

    @staticmethod
    def check_if_same_day(type_rune: str) -> bool:
        data = pandas.read_csv(FILENAME, sep=';')
        data.query(f"Type == \"{type_rune}\"", inplace=True)
        times_rune = pandas.to_datetime(data['Time']).dt.strftime('%Y-%m-%d')

        time_now = datetime.date.today()
        for time_rune in times_rune:
            if str(time_rune) == str(time_now):
                return True

        return False

    @staticmethod
    def save_graphic() -> None:
        logging.info(msg="Download graphic...")
        data_frame = pandas.read_csv(FILENAME, sep=';')
        data_frame_test = data_frame.copy()
        data_frame_test.drop_duplicates(subset="Type", keep='first', inplace=True)
        fig, ax = plt.subplots()
        for type_rune in data_frame_test['Type']:
            ax.plot(data_frame[data_frame.Type == type_rune].Time, data_frame[data_frame.Type == type_rune].Costs,
                    label=type_rune)

        ax.set_xlabel("Time")
        ax.set_ylabel("Costs")
        ax.legend(loc='best')
        plt.legend(loc=2, prop={'size': 3.5})
        plt.yticks(np.arange(0.0, 45000.0, 2000.0))
        plt.savefig(fname="..\\static\\assets\\images\\cost_rune_graph.png", dpi=130)
        plt.close()
        logging.info(msg="Done.")
