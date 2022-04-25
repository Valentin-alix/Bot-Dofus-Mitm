import datetime
import logging
import time

from factory.click import Click
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

        priorities: list[dict] = []
        for i, target_rune, in enumerate(target_item.runes):
            for rune in actual_item.runes:
                if target_rune.get("type") == rune.get("type"):
                    priorities.append(
                        {"value": rune.get("value") / target_rune.get("value"), "line": target_rune.get("line"),
                         "column": target_rune.get("column")})

        number_good_line: int = 0

        for priority in priorities:
            if priority.get("value") >= 1:
                number_good_line += 1
            elif 'minimum' not in locals() or priority.get("value") < minimum:
                minimum: float = priority.get("value")
                num_line: int = priority.get("line")
                num_column: int = priority.get("column")

        waiting_click = True

        first_time: datetime = datetime.datetime.now()

        if number_good_line == len(target_item.runes):
            click_item.click_exo()
            logging.info("Click Exo")
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

        logging.info(f"Click {num_column} {num_line}")
