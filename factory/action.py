from models.click import Click
from models.item import Item

bot_is_playing = False
item = Item()
click_item = Click()


def click_based_on_values():

    priorities = []
    state = False

    for i in range(len(item.id_runes)):
        for j in range(len(item.actual_id_values)):
            if item.id_runes[i] == item.actual_id_values[j]:
                priorities.append([item.actual_values[j] / item.value_runes[i], item.line_runes[i], item.column_runes[i]])
                state = True
                break
        if not state:
            priorities.append([0 / item.value_runes[i], item.line_runes[i], item.column_runes[i]])
        state = False

    minimum = 10000
    num_line = 0
    num_column = 0
    cpt_good = 0
    for priority in priorities:
        if priority[0] >= 1:
            cpt_good += 1
    if cpt_good == len(item.id_runes):
        click_item.click_exo()
        return

    for priority in priorities:
        if priority[0] < minimum:
            minimum = priority[0]
            num_line = priority[1]
            num_column = priority[2]

    click_item.click_rune(num_column, num_line)
