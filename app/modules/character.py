from app.interfaces.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectDate import (
    ObjectEffectDate,
)
from app.interfaces.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItem import (
    ObjectItem,
)


class Character:
    def __init__(self, objects: list[ObjectItem]) -> None:
        self.objects = [
            _object
            for _object in objects
            if not any(
                [isinstance(_effect, ObjectEffectDate) for _effect in _object.effects]
            )
        ]

    def on_object_added_msg(self, object_: ObjectItem) -> None:
        if not any(
            [isinstance(_effect, ObjectEffectDate) for _effect in object_.effects]
        ):
            self.objects.append(object_)

    def on_object_deleted_msg(self, object_uid: int) -> None:
        self.objects = [
            _object for _object in self.objects if _object.objectUID != object_uid
        ]
