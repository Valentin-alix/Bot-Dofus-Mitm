import logging
from dataclasses import dataclass

from sqlalchemy.orm import sessionmaker

from app.database.models import get_engine, Rune
from app.types_ import MagicPoolStatus
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItem import (
    ObjectItem,
)
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import (
    ObjectEffect,
)
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectInteger import (
    ObjectEffectInteger,
)

logger = logging.getLogger(__name__)


@dataclass
class Fm:
    current_item: ObjectItem
    selected_rune: ObjectItem | None = None
    _remainder: int = 0

    @property
    def remainder(self):
        return self._remainder

    @remainder.setter
    def remainder(self, value):
        if value < 0:
            raise ValueError("remainder should be positive")
        self._remainder = value

    def process(self):
        logger.info("fm gonna process")
        self.place_rune()
        # find what to move
        ...

    def place_rune(self):
        logger.info("place rune")
        ...
        # send exchangeObjectMoveMessage

    def merge_rune(self):
        logger.info("merging rune")
        # send ExchangeReadyMessage
        ...

    def get_remainder(
        self, new_item_effects: list[ObjectEffect], magic_pool_status: MagicPoolStatus
    ):
        def get_weight_item(effects: list[ObjectEffect]):
            weight_item = 0
            for effect in effects:
                if isinstance(effect, ObjectEffectInteger):
                    _rune = session.query(Rune).get(effect.actionId)
                    weight_item += _rune.weight * effect.value
                else:
                    raise ValueError("effect should be type ObjectEffectInteger")
            return weight_item

        if magic_pool_status != MagicPoolStatus.NEUTRAL:
            engine = get_engine()
            session = sessionmaker(engine)()

            weight_current_item = get_weight_item(self.current_item.effects)
            weight_new_item = get_weight_item(new_item_effects)

            session.query(Rune)

            remainder = weight_current_item - weight_new_item

            if len(self.selected_rune.effects) != 1:
                raise ValueError("selected rune effects len should be one")
            current_effect_item = next(
                (
                    _effect
                    for _effect in self.current_item.effects
                    if _effect.actionId == self.selected_rune.effects[0].actionId
                ),
                None,
            )
            next_effect_item = next(
                (
                    _effect
                    for _effect in new_item_effects
                    if _effect.actionId == self.selected_rune.effects[0].actionId
                ),
                None,
            )
            if current_effect_item == next_effect_item:
                remainder += get_weight_item(self.selected_rune.effects)

            self.remainder += round(remainder, 2)
