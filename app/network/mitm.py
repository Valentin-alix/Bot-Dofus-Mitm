import logging
from queue import Empty
from threading import Timer
import select
import random
from time import perf_counter
from datetime import datetime, timedelta
from socket import socket as Socket
from time import sleep
import psutil
import fritm
from network.models.data import BufferInfos
from network.models.message import Message
from types_ import ThreadsInfos, ParsedMessage
from network.parser import MessageRawDataParser
from types_.constants import GAME_SERVER

logger = logging.getLogger(__name__)


class Mitm:
    def __init__(self, threads_infos: ThreadsInfos) -> None:
        self.bridges: list[InjectorBridgeHandler] = []
        self.threads_infos = threads_infos

    def on_connection_callback(
        self, connection_game: fritm.proxy.ConnectionWrapper, connection_server: Socket
    ):
        bridge = InjectorBridgeHandler(
            connection_game, connection_server, self.threads_infos
        )
        self.bridges.append(bridge)

        bridge.loop()

    def launch(self):
        # TODO Launch dofus from ankama launcher, voir :
        #   - https://cadernis.fr/index.php?threads/bypass-ankama-launcher.2909/#post-28075
        while "Dofus.exe" not in (process.name() for process in psutil.process_iter()):
            print("Waiting for dofus.exe")
            sleep(1)
        fritm.start_proxy_server(self.on_connection_callback, 8080)
        fritm.hook("Dofus.exe", 8080, "port==5555")


class InjectorBridgeHandler:
    TIME_BETWEEN_SEND = [0.1, 0.2]

    def __init__(
        self,
        connection_game: fritm.proxy.ConnectionWrapper,
        connection_server: Socket,
        threads_infos: ThreadsInfos,
    ):
        self.connection_game = connection_game
        self.connection_server = connection_server
        self.opposite_connection = {
            connection_game: connection_server,
            connection_server: connection_game,
        }
        self.connections = [connection_game, connection_server]

        self.buffers = {
            connection_game: BufferInfos(),
            connection_server: BufferInfos(),
        }

        self.injected_to_client = 0
        self.injected_to_server = 0
        self.counter = 0

        self.threads_infos = threads_infos
        self.last_message_send_date: datetime | None = None
        self.raw_parser = MessageRawDataParser(self.threads_infos)

        if self.connection_server.getpeername()[0] == GAME_SERVER:
            self.threads_infos["event_connected"].set()

        self.msgs_to_send: list[dict] = []

        Timer(5, self.send_basic_ping_recurrent).start()
        Timer(
            random.uniform(*self.TIME_BETWEEN_SEND), self.check_send_msg_recurrent
        ).start()

    def send_basic_ping_recurrent(self):
        if (
            not self.threads_infos["event_close"].is_set()
            and not self.is_server_closed()
        ):
            self.send_to_server(
                Message.get_message_from_json(
                    {"__type__": "BasicPingMessage", "from_client": True, "quiet": True}
                )
            )
            Timer(5, self.send_basic_ping_recurrent).start()

    def check_send_msg_recurrent(self):
        if (
            not self.threads_infos["event_close"].is_set()
            and not self.is_server_closed()
        ):
            try:
                parsed_msg = self.threads_infos.get("queue_msg_to_send").get_nowait()
                message = Message.get_message_from_json(parsed_msg)
                self.send_to_server(message)
            except Empty:
                pass
            Timer(
                random.uniform(*self.TIME_BETWEEN_SEND), self.check_send_msg_recurrent
            ).start()

    def is_server_closed(self):
        return self.connection_server.fileno() == -1

    @classmethod
    def proxy_callback(cls, connection_game, connection_server, threads_infos):
        """Callback that can be called by the proxy

        It creates an instance of the class and
        calls `handle` on every packet

        coJeu: socket to the game
        coSer: socket to the server
        """
        bridge_handler = cls(connection_game, connection_server, threads_infos)
        bridge_handler.loop()

    def handle(self, _bytes: bytes, origin):
        buffer_infos = self.buffers[origin]
        from_client = origin == self.connection_game
        buffer_infos.data += _bytes

        message = Message.from_raw(from_client, buffer_infos)
        while message is not None:
            self.raw_parser.parse(message, from_client)
            if from_client:
                if message.count is None:
                    message.count = 0
                message.count += self.injected_to_server - self.injected_to_client
                self.counter = message.count
            else:
                self.counter += 1
            self.opposite_connection[origin].sendall(message.bytes())

            message = Message.from_raw(from_client, buffer_infos)

    def loop(self):
        conns = self.connections
        is_active = True
        try:
            while is_active and not self.threads_infos["event_close"].is_set():
                # Waiting for datas
                read_list, write_list, error_list = select.select(conns, [], conns)
                if error_list or not read_list:
                    break
                for read in read_list:
                    data = read.recv(8192)
                    if not data:
                        is_active = False
                        break
                    self.handle(data, origin=read)

        finally:
            for connection in conns:
                connection.close()

    def send_to_client(self, data):
        if isinstance(data, Message):
            data = data.bytes()
        self.injected_to_client += 1
        self.connection_game.sendall(data)

    def send_to_server(self, data):
        if not self.is_server_closed():
            if isinstance(data, Message):
                data.count = self.counter + 1
                data = data.bytes()
            self.injected_to_server += 1
            self.connection_server.sendall(data)

    def send_message(self, content: str):
        msg = Message.get_message_from_json(
            {"__type__": "ChatClientMultiMessage", "content": content, "channel": 0}
        )
        self.send_to_server(msg)
