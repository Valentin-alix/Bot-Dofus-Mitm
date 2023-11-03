import select
from socket import socket as Socket
from time import sleep
import psutil
import fritm
from network.models.data import BufferInfos, Data
from network.models.message import Message, ParsedMessage
from network.parser import MessageRawDataParser


class InjectorBridgeHandler:
    def __init__(
        self, connection_game: fritm.proxy.ConnectionWrapper, connection_server: Socket
    ):
        self.connection_game = connection_game
        self.connection_server = connection_server

        self.other = {
            connection_game: connection_server,
            connection_server: connection_game,
        }

        self.connections = [connection_game, connection_server]

        self.buffer_client: BufferInfos = BufferInfos()
        self.buffer_server: BufferInfos = BufferInfos()

        self.raw_parser = MessageRawDataParser()

        self.injected_to_client = 0
        self.injected_to_server = 0
        self.counter = 0

    def handle(self, _bytes: bytes, origin):
        from_client = origin == self.connection_game

        buffer_infos = self.buffer_client if from_client else self.buffer_server

        data = Data(_bytes)

        message = Message.from_raw(data, from_client, buffer_infos)
        while message is not None:
            parsed_message = self.raw_parser.parse(message, from_client)
            if from_client:
                if message.count is None:
                    message.count = 0
                message.count += self.injected_to_server - self.injected_to_client
                self.counter = message.count
            else:
                self.counter += 1
            self.other[origin].sendall(message.bytes())
            self.handle_message(parsed_message, origin)
            message = Message.from_raw(data, from_client, buffer_infos)

    def handle_message(self, parsed_message: ParsedMessage | None, origin):
        print(parsed_message)

    @classmethod
    def proxy_callback(cls, connection_game, connection_server):
        bridge_handler = cls(connection_game, connection_server)
        bridge_handler.loop()

    def loop(self):
        is_active = True
        try:
            while is_active:
                rlist, wlist, xlist = select.select(
                    self.connections, [], self.connections
                )
                if xlist or not rlist:
                    break
                for r in rlist:
                    data = r.recv(8192)
                    if not data:
                        is_active = False
                        break
                    self.handle(data, origin=r)

        finally:
            for connection in self.connections:
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
        self.connection_server.sendall(data)

    def send_message(self, content: str):
        msg = Message.get_message_from_json(
            {"__type__": "ChatClientMultiMessage", "content": content, "channel": 0}
        )
        self.send_to_server(msg)


if __name__ == "__main__":
    # TODO Launch dofus from ankama launcher, voir :
    #   - https://cadernis.fr/index.php?threads/bypass-ankama-launcher.2909/#post-28075
    while "Dofus.exe" not in (process.name() for process in psutil.process_iter()):
        print("Waiting for dofus.exe")
        sleep(1)

    bridges = []

    def my_callback(connection_game, connection_server):
        bridge = InjectorBridgeHandler(connection_game, connection_server)
        bridges.append(bridge)
        bridge.loop()

    httpd = fritm.start_proxy_server(my_callback, 8080)
    fritm.hook("Dofus.exe", 8080, "port==5555")
