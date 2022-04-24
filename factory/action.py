import datetime

from factory.click import Click
from models.item import Item
import numpy as np

BOT_IS_PLAYING: bool = False
ITEM: Item = Item()
CLICK_ITEM: Click = Click()
WAITING_CLICK: bool = False


class Action:
    @staticmethod
    def click_based_on_values():
        global WAITING_CLICK
        global BOT_IS_PLAYING

        priorities = np.zeros((len(ITEM), 3))

        for i, id_rune, in enumerate(ITEM.id_runes):
            for j, actual_id_rune, in enumerate(ITEM.actual_id_values):
                if id_rune == actual_id_rune:
                    priorities[i][0] = ITEM.actual_values[j] / ITEM.value_runes[i]

                priorities[i][1] = ITEM.line_runes[i]
                priorities[i][2] = ITEM.column_runes[i]

        number_good_line: int = 0

        for priority in priorities:
            if priority[0] >= 1:
                number_good_line += 1
            elif 'minimum' not in locals() or priority[0] < minimum:
                minimum = priority[0]
                num_line = int(priority[1])
                num_column = int(priority[2])

        WAITING_CLICK = True

        first_time = datetime.datetime.now()

        if number_good_line == len(ITEM):
            print("Click Exo")
            CLICK_ITEM.click_exo()
            while WAITING_CLICK and BOT_IS_PLAYING:
                if (datetime.datetime.now()-first_time).total_seconds() > 5:
                    CLICK_ITEM.click_exo()
                    first_time = datetime.datetime.now()
                else:
                    print()
            return

        CLICK_ITEM.click_rune(num_column, num_line)

        while WAITING_CLICK and BOT_IS_PLAYING:
            if (datetime.datetime.now()-first_time).total_seconds() > 5:
                CLICK_ITEM.click_rune(num_column, num_line)
                first_time = datetime.datetime.now()
            else:
                print()

        print(f"Click {num_column} {num_line}")
