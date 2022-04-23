from pathlib import Path
from typing import Any
from whistle import Event


class ResourceLoadedEvent(Event):

    LOADED: str = "loaded"
    resource: Any
    resourceType: int = 255
    uri: Path

    def __init__(
        self,
        name: str = "",
        resource: Any = None,
        resourceType: int = 255,
        uri: Path = None,
    ):
        super().__init__()
        self.resource = resource
        self.resourceType = resourceType
        self.uri = uri
        self.name = name

    def clone(self) -> "ResourceLoadedEvent":
        re: ResourceLoadedEvent = ResourceLoadedEvent(self.name)
        re.resource = self.resource
        re.resourceType = self.resourceType
        re.uri = self.uri
        return re
