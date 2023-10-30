class Message:
    content = None
    message_type = None

    def __init__(self, message_type, content=None) -> None:
        self.message_type = message_type
        self.content = content
