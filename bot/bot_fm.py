import asyncio
import logging
import time
from asyncio import Queue
from dataclasses import dataclass
from operator import itemgetter

import win32api
import win32gui

from bot.bot_click import BotClick
from models.item import Item

LINES_POS: tuple = (251, 282, 313, 344, 375, 406, 437, 468, 499, 530, 561, 592, 623)
COLUMNS_POS: tuple = (891, 930, 969)
POS_EXO_RUNE = win32api.MAKELONG(1050, 150)
FUSION_RUNE_EXO = win32api.MAKELONG(800, 170)


@dataclass
class BotFM(BotClick):
    queue_target_item: Queue
    queue_actual_item: Queue
    target_item: Item = None

    async def start(self) -> None:
        while True:
            await asyncio.sleep(0.001)
            if not self.event_is_playing.is_set():
                continue
            if not self.queue_target_item.empty():
                self.target_item = await self.queue_target_item.get()
            if not self.queue_actual_item.empty():
                await self.click_rune(await self.queue_actual_item.get())

    async def click_rune(self, actual_item: Item) -> None:
        if self.windows_name is None:
            self.find_windows_name()
            self.hwnd = win32gui.FindWindow(None, self.windows_name)

        priorities: list[dict] = []
        for i, target_rune, in enumerate(self.target_item.runes):
            priorities.append({"value": 0, "line": target_rune.get("line"),
                               "column": target_rune.get("column")})
            for rune in actual_item.runes:
                if target_rune.get("type") == rune.get("type"):
                    priorities[i]["value"] = rune.get("value") / target_rune.get("value")
                    priorities[i]["type"] = rune.get("type")

        high_priority = min(priorities, key=itemgetter('value'))
        self.event_ready.clear()
        before_click_time: float = time.perf_counter()
        if high_priority.get("value") >= 1:
            self.click(POS_EXO_RUNE)
            self.click(POS_EXO_RUNE)
            await asyncio.sleep(0.5)
            self.click(FUSION_RUNE_EXO)
            logging.info("Click Exo")
            self.database.update_exo_on_item_by_name(self.target_item.name)
        else:
            quantity: int = 1
            if high_priority.get('column') == 2:
                quantity = 3
            elif high_priority.get('column') == 3:
                quantity = 10
            await asyncio.sleep(0.1)
            self.click(win32api.MAKELONG(COLUMNS_POS[high_priority.get("column")],
                                         LINES_POS[high_priority.get("line")]))
            logging.info(f"Click {high_priority.get('column')} {high_priority.get('line')}")
            self.database.update_quantity_on_target_line_by_type_rune(high_priority.get('type'), self.target_item.name,
                                                                      quantity)
        while not self.event_ready.is_set() and self.event_is_playing.is_set():
            await asyncio.sleep(0.001)
            if time.perf_counter() - before_click_time < 6.0:
                continue
            before_click_time: float = time.perf_counter()
            if high_priority.get("value") >= 1:
                self.click(POS_EXO_RUNE)
                self.click(POS_EXO_RUNE)
                await asyncio.sleep(0.5)
                self.click(FUSION_RUNE_EXO)
                logging.info("Click Exo")
            else:
                self.click(win32api.MAKELONG(COLUMNS_POS[high_priority.get("column")],
                                             LINES_POS[high_priority.get("line")]))
                logging.info(f"Click {high_priority.get('column')} {high_priority.get('line')}")
