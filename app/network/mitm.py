import logging
import random
from copy import deepcopy
from datetime import datetime
from queue import Empty
from socket import socket as Socket, SHUT_WR
from threading import Thread
from time import sleep

import fritm
import psutil
import select
from PyQt5.QtCore import QObject

from app.gui.signals import AppSignals
from app.network.parser import MessageRawDataParser
from app.types_ import BotInfo
from app.types_.models.data import BufferInfos
from app.types_.models.message import Message

logger = logging.getLogger(__name__)


class Mitm(QObject):
    def __init__(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        super().__init__()
        self.app_signals = app_signals
        self.bridges: list[InjectorBridgeHandler] = []
        self.bot_info = bot_info
        self.app_signals.close.connect(self.on_close)

    def on_close(self) -> None:
        for bridge in self.bridges:
            if not bridge.is_server_closed():
                bridge.connection_server.shutdown(SHUT_WR)

    def on_connection_callback(
            self, connection_game: fritm.proxy.ConnectionWrapper, connection_server: Socket
    ):
        bridge = InjectorBridgeHandler(
            connection_game, connection_server, self.bot_info
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
            bot_info: BotInfo,
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

        self.bot_info = bot_info
        self.last_message_send_date: datetime | None = None
        self.raw_parser = MessageRawDataParser(self.bot_info)

        self.msgs_to_send: list[dict] = []

        send_basic_ping_recurrent_thread = Thread(
            target=self.send_basic_ping_recurrent, daemon=True
        )
        send_basic_ping_recurrent_thread.start()

        check_send_msg_recurrent_thread = Thread(
            target=self.check_send_msg_recurrent, daemon=True
        )
        check_send_msg_recurrent_thread.start()

    def send_basic_ping_recurrent(self):
        while not self.is_server_closed():
            self.send_to_server(
                Message.get_message_from_json(
                    {"__type__": "BasicPingMessage", "quiet": True}
                )
            )
            sleep(random.uniform(7, 10))

    def check_send_msg_recurrent(self):
        while not self.is_server_closed():
            try:
                parsed_msg = (
                    self.bot_info.common_info.message_to_send_queue.get_nowait()
                )
                message = Message.get_message_from_json(parsed_msg)
                self.send_to_server(message)
            except Empty:
                pass
            sleep(random.uniform(*self.TIME_BETWEEN_SEND))

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
        buffer_info = self.buffers[origin]
        from_client = origin == self.connection_game
        buffer_info.data += _bytes

        message = Message.from_raw(from_client, buffer_info)
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

            message = Message.from_raw(from_client, buffer_info)

    def loop(self):
        conns = self.connections
        is_active = True
        try:
            while is_active:
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
            self.raw_parser.parse(deepcopy(data), False)
            data = data.bytes()
        self.injected_to_client += 1
        self.connection_game.sendall(data)

    def send_to_server(self, data):
        if not self.is_server_closed():
            if isinstance(data, Message):
                data.count = self.counter + 1
                self.raw_parser.parse(deepcopy(data), True)
                data = data.bytes()
            self.injected_to_server += 1
            self.connection_server.sendall(data)

    def send_message(self, content: str):
        msg = Message.get_message_from_json(
            {"__type__": "ChatClientMultiMessage", "content": content, "channel": 0}
        )
        self.send_to_server(msg)
