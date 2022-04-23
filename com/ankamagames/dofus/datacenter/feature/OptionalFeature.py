from com.ankamagames.dofus.datacenter.feature.criterion.GroupFeatureCriterion import (
    GroupFeatureCriterion,
)
from com.ankamagames.dofus.types.IdAccessors import IdAccessors
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class OptionalFeature(IDataCenter):

    MODULE: str = "OptionalFeatures"

    _keywords: dict

    id: int

    keyword: str = None

    isClient: bool

    isServer: bool

    isActivationOnLaunch: bool = False

    isActivationOnServerConnection: bool = False

    activationCriterions: str = None

    def __init__(self):
        super().__init__()

    @classmethod
    def getOptionalFeatureById(cls, id: int) -> "OptionalFeature":
        return GameData.getObject(cls.MODULE, id)

    @classmethod
    def getOptionalFeatureByKeyword(cls, key: str) -> "OptionalFeature":
        feature: OptionalFeature = None
        if not cls._keywords or not cls._keywords.get(key):
            cls._keywords = dict()
            for feature in cls.getAllOptionalFeatures():
                cls._keywords[feature.keyword] = feature
        return cls._keywords[key]

    @classmethod
    def getAllOptionalFeatures(cls) -> list["OptionalFeature"]:
        return GameData.getObjects(cls.MODULE)

    @property
    def canBeEnabled(self) -> bool:
        if not self.activationCriterions:
            return True
        groupFeatureCriterion: GroupFeatureCriterion = GroupFeatureCriterion(
            self.activationCriterions
        )
        return groupFeatureCriterion.isRespected

    def __str__(self) -> str:
        featureTypeLabel: str = None
        if self.isClient and not self.isServer:
            featureTypeLabel = "Client"
        elif not self.isClient and self.isServer:
            featureTypeLabel = "Server"
        elif self.isClient and self.isServer:
            featureTypeLabel = "Client/Server"
        else:
            featureTypeLabel = "???"
        return (
            "Feature "
            + self.keyword
            + " (ID: "
            + str(self.id)
            + ") ["
            + featureTypeLabel
            + "]"
        )

    idAccessors: IdAccessors = IdAccessors(
        getOptionalFeatureById, getAllOptionalFeatures
    )
