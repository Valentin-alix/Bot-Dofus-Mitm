import datetime
import logging
import time
from operator import itemgetter

from bot.databases.database import Database
from bot.factory.click import Click
from bot.models.item import Item

bot_is_playing: bool = False
target_item: Item = Item()
actual_item: Item = Item()
click_item: Click = Click()
waiting_click: bool = False


class Action:
    @staticmethod
    def click_based_on_values() -> None:
        global waiting_click
        global bot_is_playing

        priorities: list[dict] = []
        for i, target_rune, in enumerate(target_item.runes):
            priorities.append({"value": 0, "line": target_rune.get("line"),
                               "column": target_rune.get("column")})
            for rune in actual_item.runes:
                if target_rune.get("type") == rune.get("type"):
                    priorities[i]["value"] = rune.get("value") / target_rune.get("value")
                    priorities[i]["type"] = rune.get("type")

        high_priority = min(priorities, key=itemgetter('value'))

        waiting_click = True

        before_click_time: datetime = datetime.datetime.now()

        if high_priority.get("value") >= 1:
            click_item.click_exo()
            logging.info("Click Exo")
            Database().update_exo_on_item_by_name(target_item.name)
        else:
            click_item.click_rune(high_priority.get("column"), high_priority.get("line"))
            logging.info(f"Click {high_priority.get('column')} {high_priority.get('line')}")
            Database().update_quantity_on_target_line_by_type_rune(high_priority.get('type'), target_item.name)

        while waiting_click and bot_is_playing:
            if (datetime.datetime.now() - before_click_time).total_seconds() > 5:
                if high_priority.get("value") >= 1:
                    click_item.click_exo()
                    before_click_time = datetime.datetime.now()
                else:
                    click_item.click_rune(high_priority.get("column"), high_priority.get("line"))
                    before_click_time = datetime.datetime.now()
            else:
                time.sleep(0.001)


