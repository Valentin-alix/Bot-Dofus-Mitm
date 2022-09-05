import datetime
import logging
from time import perf_counter
import eel
import matplotlib.pyplot as plt
import numpy as np
import pandas as pandas

from bot.bot_click import BotClick

logger = logging.getLogger(__name__)

LINES_HDV = np.arange(160, 645, 35)
SCROLL_HDV = np.arange(220, 710, 70)
FILENAME: str = "gui/assets/csv/prices_runes.csv"


@eel.expose
def save_graphic() -> None:
    avant = perf_counter()
    data_frame = pandas.read_csv(FILENAME, sep=";")
    data_frame_test = data_frame.copy()
    data_frame_test.drop_duplicates(subset="Type", keep="first", inplace=True)
    fig, ax = plt.subplots()
    data_frame = data_frame.sort_index()
    [
        ax.plot(
            data_frame[data_frame.Type == type_rune].Time,
            data_frame[data_frame.Type == type_rune].Costs,
            label=type_rune,
        )
        for type_rune in data_frame_test["Type"]
    ]

    ax.set_xlabel("Time")

    ax.set_ylabel("Costs")
    ax.legend(loc="best")
    plt.legend(loc=2, prop={"size": 3.5})
    plt.yticks(np.arange(0.0, 45000.0, 2000.0))
    plt.savefig(fname="gui/assets/images/cost_rune_graph.png", dpi=130)
    plt.close()
    logger.info(f"Refresh graphic in : {perf_counter() - avant}")


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
