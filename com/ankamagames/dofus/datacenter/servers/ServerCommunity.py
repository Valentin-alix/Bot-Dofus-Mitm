from com.ankamagames.dofus.datacenter.communication.NamingRule import NamingRule
from com.ankamagames.dofus.types.IdAccessors import IdAccessors
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter
from com.ankamagames.jerakine.logger.Logger import Logger


class ServerCommunity(IDataCenter):

    MODULE: str = "ServerCommunities"

    logger = Logger(__name__)

    id: int

    nameId: int

    shortId: str

    defaultCountries: list[str]

    supportedLangIds: list[int]

    namingRulePlayerNameId: int

    namingRuleGuildNameId: int

    namingRuleAllianceNameId: int

    namingRuleAllianceTagId: int

    namingRulePartyNameId: int

    namingRuleMountNameId: int

    namingRuleNameGeneratorId: int

    namingRuleAdminId: int

    namingRuleModoId: int

    namingRulePresetNameId: int

    _name: str

    _namingRulePlayerName: NamingRule

    _namingRuleGuildName: NamingRule

    _namingRuleAllianceName: NamingRule

    _namingRuleAllianceTag: NamingRule

    _namingRulePartyName: NamingRule

    _namingRuleMountName: NamingRule

    _namingRuleNameGenerator: NamingRule

    _namingRuleAdmin: NamingRule

    _namingRuleModo: NamingRule

    _namingRulePresetName: NamingRule

    def __init__(self):
        super().__init__()

    @classmethod
    def getServerCommunityById(cls, id: int) -> "ServerCommunity":
        return GameData.getObject(cls.MODULE, id)

    @classmethod
    def getServerCommunities(cls) -> list["ServerCommunity"]:
        return GameData.getObjects(cls.MODULE)

    idAccessors: IdAccessors = IdAccessors(getServerCommunityById, getServerCommunities)

    @property
    def name(self) -> str:
        if not self._name:
            self._name = I18n.getText(self.nameId)
        return self._name

    @property
    def namingRulePlayerName(self) -> NamingRule:
        if not self._namingRulePlayerName:
            self._namingRulePlayerName = NamingRule.getNamingRuleById(
                self.namingRulePlayerNameId
            )
        return self._namingRulePlayerName

    @property
    def namingRuleGuildName(self) -> NamingRule:
        if not self._namingRuleGuildName:
            self._namingRuleGuildName = NamingRule.getNamingRuleById(
                self.namingRuleGuildNameId
            )
        return self._namingRuleGuildName

    @property
    def namingRuleAllianceName(self) -> NamingRule:
        if not self._namingRuleAllianceName:
            self._namingRuleAllianceName = NamingRule.getNamingRuleById(
                self.namingRuleAllianceNameId
            )
        return self._namingRuleAllianceName

    @property
    def namingRuleAllianceTag(self) -> NamingRule:
        if not self._namingRuleAllianceTag:
            self._namingRuleAllianceTag = NamingRule.getNamingRuleById(
                self.namingRuleAllianceTagId
            )
        return self._namingRuleAllianceTag

    @property
    def namingRulePartyName(self) -> NamingRule:
        if not self._namingRulePartyName:
            self._namingRulePartyName = NamingRule.getNamingRuleById(
                self.namingRulePartyNameId
            )
        return self._namingRulePartyName

    @property
    def namingRuleMountName(self) -> NamingRule:
        if not self._namingRuleMountName:
            self._namingRuleMountName = NamingRule.getNamingRuleById(
                self.namingRuleMountNameId
            )
        return self._namingRuleMountName

    @property
    def namingRuleNameGenerator(self) -> NamingRule:
        if not self._namingRuleNameGenerator:
            self._namingRuleNameGenerator = NamingRule.getNamingRuleById(
                self.namingRuleNameGeneratorId
            )
        return self._namingRuleNameGenerator

    @property
    def namingRuleAdmin(self) -> NamingRule:
        if not self._namingRuleAdmin:
            self._namingRuleAdmin = NamingRule.getNamingRuleById(self.namingRuleAdminId)
        return self._namingRuleAdmin

    @property
    def namingRuleModo(self) -> NamingRule:
        if not self._namingRuleModo:
            self._namingRuleModo = NamingRule.getNamingRuleById(self.namingRuleModoId)
        return self._namingRuleModo

    @property
    def namingRulePresetName(self) -> NamingRule:
        if not self._namingRulePresetName:
            self._namingRulePresetName = NamingRule.getNamingRuleById(
                self.namingRulePresetNameId
            )
        return self._namingRulePresetName
