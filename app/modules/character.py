from network.parsed_message.dicts import ObjectItem


class Character:
    def __init__(self, objects: list[ObjectItem]) -> None:
        self.objects = objects

    def on_object_added_msg(self, object_: ObjectItem) -> None:
        self.objects.append(object_)

    def on_object_deleted_msg(self, object_uid: int) -> None:
        self.objects = [
            _object
            for _object in self.objects
            if _object.get("objectUID") != object_uid
        ]
