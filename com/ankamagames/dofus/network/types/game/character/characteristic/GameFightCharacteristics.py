from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristics import (
    CharacterCharacteristics,
)


class GameFightCharacteristics:
    characteristics: CharacterCharacteristics
    summoner: float = 0
    summoned: bool = False
    invisibilityState: int = 0

    def __init__(self):
        self.characteristics = CharacterCharacteristics()

    def initGameFightCharacteristics(
        self,
        characteristics: CharacterCharacteristics = None,
        summoner: float = 0,
        summoned: bool = False,
        invisibilityState: int = 0,
    ) -> "GameFightCharacteristics":
        self.characteristics = characteristics
        self.summoner = summoner
        self.summoned = summoned
        self.invisibilityState = invisibilityState
        return self

    def reset(self) -> None:
        self.characteristics = CharacterCharacteristics()
        self.summoned = False
        self.invisibilityState = 0
