import datetime

import matplotlib.pyplot as plt
import pandas

filename: str = 'C:\\Users\\valen\\Documents\\Workspace\\Python\\bot_mitm\\bot\\factory\\resources\\prices_runes.csv'


def maj_csv_value(time: datetime.datetime, type_rune: str, cost: int) -> None:
    data = pandas.read_csv(filename, sep=';')
    data_frame = pandas.DataFrame(data, columns=['Time', 'Type', 'Costs'])
    data_new_row = pandas.DataFrame({'Time': [time], 'Type': [type_rune], 'Costs': [cost]})
    data_frame = pandas.concat([data_frame, data_new_row])
    data_frame.to_csv(filename, mode='w', index=False, header=True, sep=';')


def check_if_same_minutes(type_rune: str) -> bool:
    data = pandas.read_csv(filename, sep=';')
    data.query(f"Type == \"{type_rune}\"", inplace=True)
    time_test = pandas.to_datetime(data['Time'])

    base_dt = pandas.to_datetime(datetime.datetime.now())
    times_hdv = (base_dt - time_test).dt.total_seconds()
    for time_hdv in times_hdv:
        if time_hdv < 60:
            return True
    return False


def test_graphic() -> None:
    data_frame = pandas.read_csv(filename, sep=';')

    fig, ax = plt.subplots()
    for type_rune in data_frame['Type']:
        ax.plot(data_frame[data_frame.Type == type_rune].Time, data_frame[data_frame.Type == type_rune].Costs,
                label=type_rune)
        # data_frame_test = data_frame.query(f"Type == \"{type_rune}\"")
        # print(data_frame_test)

    ax.set_xlabel("Time")
    ax.set_ylabel("Costs")
    ax.legend(loc='best')
    plt.show()


if __name__ == "__main__":
    test_graphic()
