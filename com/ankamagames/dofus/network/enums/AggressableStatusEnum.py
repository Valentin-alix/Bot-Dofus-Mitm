class AggressableStatusEnum:

    NON_AGGRESSABLE: int = 0

    PvP_ENABLED_AGGRESSABLE: int = 10

    PvP_ENABLED_NON_AGGRESSABLE: int = 11

    AvA_ENABLED_AGGRESSABLE: int = 20

    AvA_ENABLED_NON_AGGRESSABLE: int = 21

    AvA_DISQUALIFIED: int = 22

    AvA_PREQUALIFIED_AGGRESSABLE: int = 23

    def __init__(self):
        super().__init__()
