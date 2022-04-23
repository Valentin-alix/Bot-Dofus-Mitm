class AbstractAction:

    _parameters: list

    def __init__(self, params: list = None):
        super().__init__()
        if params == None:
            params = []
        self._parameters = params

    @property
    def parameters(self) -> list:
        return self._parameters
