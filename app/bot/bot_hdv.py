import datetime
import logging
from time import perf_counter

import matplotlib.pyplot as plt
import numpy as np
import pandas as pandas
from bot.bot_click import BotClick

logger = logging.getLogger(__name__)

LINES_HDV = np.arange(160, 645, 35)
SCROLL_HDV = np.arange(220, 710, 70)
FILENAME: str = "gui/assets/csv/prices_runes.csv"


class BotHDV(BotClick):
    # TODO AUTOMATE CLICKS

    @staticmethod
    def maj_csv_value(time_when_maj: datetime.date, type_rune: str, cost: int) -> None:
        if BotHDV.check_if_same_day(type_rune):
            return
        data_frame = pandas.DataFrame(
            pandas.read_csv(FILENAME, sep=";"), columns=["Time", "Type", "Costs"]
        )
        data_frame = pandas.concat(
            [
                data_frame,
                pandas.DataFrame(
                    {"Time": [time_when_maj], "Type": [type_rune], "Costs": [cost]}
                ),
            ]
        )
        data_frame.to_csv(FILENAME, mode="w", index=False, header=True, sep=";")

    @staticmethod
    def check_if_same_day(type_rune: str) -> bool:
        data = pandas.read_csv(FILENAME, sep=";")
        data.query(f'Type == "{type_rune}"', inplace=True)

        return any(
            str(time_rune) == str(datetime.date.today())
            for time_rune in pandas.to_datetime(data["Time"]).dt.strftime("%Y-%m-%d")
        )
