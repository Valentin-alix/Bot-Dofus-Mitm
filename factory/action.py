from models.click import Click
from models.item import Item
import numpy as np

bot_is_playing = False
item = Item()
click_item = Click()


def click_based_on_values():
    priorities = np.zeros((len(item), 3))

    for i, id_rune, in enumerate(item.id_runes):
        for j, actual_id_rune, in enumerate(item.actual_id_values):
            if id_rune == actual_id_rune:
                priorities[i][0] = item.actual_values[j] / item.value_runes[i]

            priorities[i][1] = item.line_runes[i]
            priorities[i][2] = item.column_runes[i]

    number_good_line: int = 0

    for priority in priorities:
        if priority[0] >= 1:
            number_good_line += 1
        elif 'minimum' not in locals() or priority[0] < minimum:
            minimum = priority[0]
            num_line = int(priority[1])
            num_column = int(priority[2])

    if number_good_line == len(item):
        click_item.click_exo()
        return

    click_item.click_rune(num_column, num_line)
