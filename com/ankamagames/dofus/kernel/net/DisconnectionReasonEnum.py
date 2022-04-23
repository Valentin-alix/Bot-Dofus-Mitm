from enum import Enum


class DisconnectionReasonEnum(Enum):

    UNEXPECTED: int = 0

    SWITCHING_TO_GAME_SERVER: int = 1

    SWITCHING_TO_HUMAN_VENDOR: int = 2

    DISCONNECTED_BY_POPUP_WITHOUT_RESET: int = 5

    DISCONNECTED_BY_POPUP: int = 3

    NEVER_CONNECTED: int = 4
