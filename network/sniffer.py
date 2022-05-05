import logging
import socket
from asyncio import Queue, Event
from dataclasses import dataclass

from databases.database import Database
from models.data import Data
from network.async_pyshark import AsyncLiveCapture
from network.message import Message

FILTER_DOFUS: str = 'tcp port 5555'


def get_local_ip() -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        ip_local = s.getsockname()[0]
    except Exception as e:
        print("Exception on get local ip")
        print(e)
        ip_local = '127.0.0.1'
    finally:
        s.close()
    return ip_local


@dataclass
class Sniffer:
    event_ready: Event
    queue_actual_item: Queue
    queue_inserted_item: Queue
    event_is_playing: Event
    database: Database
    buffer_client: Data = Data()
    buffer_server: Data = Data()
    ip_local: str = get_local_ip()

    async def launch_sniffer(self) -> None:
        capture = AsyncLiveCapture(bpf_filter=FILTER_DOFUS)
        async for packet in capture.sniff_continuously():
            await self.on_receive(packet)

    async def on_receive(self, packet) -> None:
        try:
            if packet.ip.src == self.ip_local:
                try:
                    logging.warning(f"tcp segment : {packet.tcp.segment_data}")
                    data: str = str(packet.tcp.segment_data).replace(":", "")
                    self.buffer_client += bytearray.fromhex(data)
                    await self.from_raw(self.buffer_client, True)
                    return
                except AttributeError:
                    pass
                logging.info(f"Data receive : {packet.data.data}")
                self.buffer_client += bytearray.fromhex(packet.data.data)
                await self.from_raw(self.buffer_client, True)
            else:
                try:
                    logging.warning(f"tcp segment : {packet.tcp.segment_data}")
                    data = str(packet.tcp.segment_data).replace(":", "")
                    self.buffer_server += bytearray.fromhex(data)
                    await self.from_raw(self.buffer_server, False)
                    return
                except AttributeError:
                    pass
                logging.info(f"Data receive : {packet.data.data}")
                self.buffer_server += bytearray.fromhex(packet.data.data)
                await self.from_raw(self.buffer_server, False)
        except AttributeError:
            pass

    async def from_raw(self, buffer: Data, from_client: bool) -> None:
        while True:
            try:
                logging.info(f"{from_client} | Trying to extract these data : {buffer}")

                header = buffer.readUnsignedShort()
                message_id = header >> 2

                if from_client:
                    buffer.readUnsignedInt()

                if id == 2:
                    logging.info("Message is NetworkDataContainerMessage! Uncompressing...")
                    new_buffer = Data(buffer.readByteArray())
                    new_buffer.uncompress()
                    await self.from_raw(new_buffer, from_client)
                    break

                len_data = int.from_bytes(buffer.read(header & 3), "big")

                if not self.database.select_message_by_id(message_id):
                    logging.error("Can't get corresponding message to id")
                    print("Error Sniffer, réinitialisation buffer...")
                    buffer.__init__()
                    break
                if self.database.select_message_by_id(
                        message_id) == "ExchangeReadyMessage" and self.event_is_playing.is_set():
                    self.event_ready.set()
                logging.info(f"Message :{self.database.select_message_by_id(message_id)}")
                data = Data(buffer.read(len_data))
                message = Message(message_id, data)
                await message.event(self.queue_actual_item, self.queue_inserted_item, self.event_is_playing,
                                    self.database)
                buffer.end()
            except IndexError:
                buffer.reset_pos()
                break
