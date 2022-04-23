from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter
from com.ankamagames.jerakine.logger.Logger import Logger

logger = Logger(__name__)


class BreedRoleByBreed(IDataCenter):

    MODULE: str = "BreedRoleByBreeds"

    breedId: int

    roleId: int

    descriptionId: int

    value: int

    order: int

    _description: str

    def __init__(self):
        super().__init__()

    @property
    def description(self) -> str:
        if not self._description:
            self._description = I18n.getText(self.descriptionId)
        return self._description
