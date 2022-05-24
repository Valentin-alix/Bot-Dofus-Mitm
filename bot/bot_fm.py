import logging
from operator import itemgetter
from queue import Queue
import time
from dataclasses import dataclass, field

import win32gui

from bot.bot_click import BotClick
from databases.database import *

logger = logging.getLogger(__name__)

@dataclass
class BotFM(BotClick):
    queue_target_item: Queue
    queue_actual_item: Queue
    target_item: list[dict] = field(default_factory=list)
    actual_item: list[dict] = field(default_factory=list)

    def start(self) -> None:
        while True:
            self.target_item = select_target_line_by_name(self.queue_target_item.get())
            logger.info(f"Starting item... : {self.target_item}")
            while self.event_is_playing.is_set():
                self.actual_item = self.queue_actual_item.get()
                self.click_rune()
                time.sleep(0.001)
            time.sleep(0.001)


    def click_rune(self) -> None:
        logger.info(f"actual item : {self.actual_item}")
        logger.info(f"target item : {self.target_item}")
        if self.windows_name is None:
            self.find_windows_name()
            self.hwnd = win32gui.FindWindow(None, self.windows_name)
        
        priorities: list[dict] = []
        for i, target_rune, in enumerate(self.target_item):
            priorities.append({"value": 0, "line": target_rune.get("line"),
                               "column": target_rune.get("column")})
            for rune in self.actual_item:
                if target_rune.get("rune_name") == rune.get("rune_name"):
                    priorities[i]["value"] = rune.get("value") / target_rune.get("value")
                    priorities[i]["rune_name"] = rune.get("rune_name")
        
        high_priority = min(priorities, key=itemgetter('value'))
        
        if high_priority.get("value") >= 1:
            self.click_exo()
            logger.info("Click Exo")
        else:
            time.sleep(0.05)
            self.click_on_rune(high_priority.get("column"),high_priority.get("line"))
            logger.info(f"Click {high_priority.get('column')} {high_priority.get('line')}")
