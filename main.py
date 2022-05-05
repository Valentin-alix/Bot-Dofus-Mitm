import asyncio
from asyncio import Queue, Event

from bot.bot_fm import BotFM
from databases.database import Database
from interface.ui import Ui
from network.sniffer import Sniffer


async def main_fm():
    database: Database = Database()

    queue_target_item: Queue = Queue()
    queue_actual_item: Queue = Queue()
    queue_inserted_item: Queue = Queue()

    event_ready: Event = Event()
    event_is_playing: Event = Event()

    ui = Ui(queue_target_item, queue_inserted_item, queue_actual_item, event_is_playing, database)
    await ui.window()
    sniffer = Sniffer(event_ready, queue_actual_item, queue_inserted_item, event_is_playing, database)
    bot_fm = BotFM(database, "Ezrealeeuu", event_ready, event_is_playing, queue_target_item, queue_actual_item)

    ui_task = asyncio.create_task(ui.updater())
    ui_check_item_task = asyncio.create_task(ui.check_inserted_item())
    sniffer_task = asyncio.create_task(sniffer.launch_sniffer())
    bot_fm_task = asyncio.create_task(bot_fm.start())

    await ui_check_item_task
    await bot_fm_task
    await ui_task
    await sniffer_task


if __name__ == '__main__':
    asyncio.run(main_fm())
