import datetime
import logging

import matplotlib.pyplot as plt
import numpy as np
import pandas


filename: str = '..\\static\\resources\\prices_runes.csv'


def maj_csv_value(time: datetime.date, type_rune: str, cost: int) -> None:
    data = pandas.read_csv(filename, sep=';')
    data_frame = pandas.DataFrame(data, columns=['Time', 'Type', 'Costs'])
    data_new_row = pandas.DataFrame({'Time': [time], 'Type': [type_rune], 'Costs': [cost]})
    data_frame = pandas.concat([data_frame, data_new_row])
    data_frame.to_csv(filename, mode='w', index=False, header=True, sep=';')


def check_if_same_day(type_rune: str) -> bool:
    data = pandas.read_csv(filename, sep=';')
    data.query(f"Type == \"{type_rune}\"", inplace=True)
    times_rune = pandas.to_datetime(data['Time']).dt.strftime('%Y-%m-%d')

    time_now = datetime.date.today()
    for time_rune in times_rune:
        if str(time_rune) == str(time_now):
            return True

    return False


def save_graphic() -> None:
    logging.info(msg="Download graphic...")
    data_frame = pandas.read_csv(filename, sep=';')
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
