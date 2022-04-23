from enum import Enum


class ServerStatusEnum(Enum):
    STATUS_UNKNOWN = 0
    OFFLINE = 1
    STARTING = 2
    ONLINE = 3
    NOJOIN = 4
    SAVING = 5
    STOPING = 6
    FULL = 7

    def __str__(self):
        matched = {
            0: "STATUS_UNKNOWN",
            1: "OFFLINE",
            2: "STARTING",
            3: "ONLINE",
            4: "NOJOIN",
            5: "SAVING",
            6: "STOPING",
            7: "FULL",
        }
        return matched[self.value]
