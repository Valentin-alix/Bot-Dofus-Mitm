import logging
import random
import select
from datetime import datetime
from queue import Empty
from socket import SHUT_WR
from socket import socket as Socket
from threading import Thread
from time import sleep

import psutil
from PyQt5.QtCore import QObject

from app.gui.signals import AppSignals
from app.interfaces.models.common import BotInfo
from app.interfaces.models.network.data import BufferInfos
from app.interfaces.models.network.message import Message
from app.network.fritm.hook import hook
from app.network.fritm.proxy import ConnectionWrapper, start_proxy_server
from app.network.parser import MessageRawDataParser

logger = logging.getLogger(__name__)


class Mitm(QObject):
    def __init__(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        super().__init__()
        self.app_signals = app_signals
        self.app_signals.on_close.connect(self.on_close)
        self.bridges: list[InjectorBridgeHandler] = []
        self.bot_info = bot_info

    def on_close(self) -> None:
        for bridge in self.bridges:
            if not bridge.is_server_closed():
                bridge.connection_server.shutdown(SHUT_WR)

    def on_connection_callback(
        self, connection_game: ConnectionWrapper, connection_server: Socket
    ):
        bridge = InjectorBridgeHandler(
            connection_game, connection_server, self.bot_info, self.app_signals
        )

        self.bridges.append(bridge)

        bridge.loop()

    def launch(self):
        while "Dofus.exe" not in (process.name() for process in psutil.process_iter()):
            print("Waiting for dofus.exe")
            sleep(1)
        start_proxy_server(self.on_connection_callback, 8080)
        hook("Dofus.exe", 8080, "port==5555")


class InjectorBridgeHandler:
    TIME_BETWEEN_SEND = [0.1, 0.2]

    def __init__(
        self,
        connection_game: ConnectionWrapper,
        connection_server: Socket,
        bot_info: BotInfo,
        app_signals: AppSignals,
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
        self.app_signals = app_signals

        self.last_message_send_date: datetime | None = None
        self.raw_parser = MessageRawDataParser(self.bot_info, self.app_signals)

        self.msgs_to_send: list[dict] = []

        check_send_msg_recurrent_thread = Thread(
            target=self.check_send_msg_recurrent, daemon=True
        )
        check_send_msg_recurrent_thread.start()

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
            data = data.bytes()
        self.injected_to_client += 1
        self.connection_game.sendall(data)

    def send_to_server(self, data):
        if isinstance(data, Message):
            data.count = self.counter + 1
            data = data.bytes()
        self.injected_to_server += 1
        if not self.is_server_closed():
            self.connection_server.sendall(data)
