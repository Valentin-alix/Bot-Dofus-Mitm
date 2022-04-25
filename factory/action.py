import datetime
import time

from factory.click import Click
import numpy as np

from models.item import Item

bot_is_playing: bool = False
target_item: Item = Item()
actual_item: Item = Item()
click_item: Click = Click()
waiting_click: bool = False


class Action:
    @staticmethod
    def click_based_on_values():
        global waiting_click
        global bot_is_playing

        priorities = np.zeros((len(target_item.runes), 3))

        for i, target_rune, in enumerate(target_item.runes):
            for rune in actual_item.runes:
                if target_rune.get("type") == rune.get("type"):
                    priorities[i][0] = rune.get("value") / target_rune.get("value")

                priorities[i][1] = target_rune.get("line")
                priorities[i][2] = target_rune.get("column")

        number_good_line: int = 0

        for priority in priorities:
            if priority[0] >= 1:
                number_good_line += 1
            elif 'minimum' not in locals() or priority[0] < minimum:
                minimum = priority[0]
                num_line = int(priority[1])
                num_column = int(priority[2])

        waiting_click = True

        first_time = datetime.datetime.now()

        if number_good_line == len(target_item.runes):
            print("Click Exo")
            click_item.click_exo()
            while waiting_click and bot_is_playing:
                if (datetime.datetime.now() - first_time).total_seconds() > 5:
                    click_item.click_exo()
                    first_time = datetime.datetime.now()
                else:
                    time.sleep(0.05)
            return

        click_item.click_rune(num_column, num_line)

        while waiting_click and bot_is_playing:
            if (datetime.datetime.now() - first_time).total_seconds() > 5:
                click_item.click_rune(num_column, num_line)
                first_time = datetime.datetime.now()
            else:
                time.sleep(0.05)

        print(f"Click {num_column} {num_line}")
