from whistle import Event


class FramePulledEvent(Event):
    EVENT_FRAME_PULLED = "framePulled"

    def __init__(self, frame):
        super().__init__()
        self.frame = frame
