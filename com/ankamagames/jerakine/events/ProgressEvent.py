from whistle import Event


class ProgressEvent(Event):
    SOCKET_DATA = "socketData"

    def __init__(self, data):
        self.data = data
