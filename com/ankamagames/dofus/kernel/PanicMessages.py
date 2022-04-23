class PanicMessages:

    SUPPORT_URL: str = "https://support.ankama.com/"

    CONFIG_LOADING_FAILED: int = 1

    I18N_LOADING_FAILED: int = 2

    WRONG_CONTEXT_CREATED: int = 3

    PROTOCOL_TOO_OLD: int = 4

    PROTOCOL_TOO_NEW: int = 5

    TOO_MANY_CLIENTS: int = 6

    UNABLE_TO_GET_FLASHKEY: int = 7

    OUT_OF_MEMORY: int = 8

    MALFORMED_PROTOCOL: int = 9

    PROTOCOL_MISMATCH: int = 10

    def __init__(self):
        super().__init__()

    def getMessage(self, errorId: int, args: list) -> str:
        return f"Call support dumbass here is the url {self.SUPPORT_URL}"
