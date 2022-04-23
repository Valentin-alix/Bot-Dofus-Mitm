class StatsUpgradeResultEnum:

    NONE: int = -1

    SUCCESS: int = 0

    RESTRICTED: int = 1

    GUEST: int = 2

    IN_FIGHT: int = 3

    NOT_ENOUGH_POINT: int = 4

    def __init__(self):
        super().__init__()
