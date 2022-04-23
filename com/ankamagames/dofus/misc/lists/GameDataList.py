# from com.ankamagames.dofus.datacenter.alignments.AlignmentGift import AlignmentGift
# from com.ankamagames.dofus.datacenter.alignments.AlignmentOrder import AlignmentOrder
# from com.ankamagames.dofus.datacenter.alignments.AlignmentRank import AlignmentRank
# from com.ankamagames.dofus.datacenter.alignments.AlignmentRankJntGift import AlignmentRankJntGift
# from com.ankamagames.dofus.datacenter.alignments.AlignmentSide import AlignmentSide
# from com.ankamagames.dofus.datacenter.alignments.AlignmentTitle import AlignmentTitle
# from com.ankamagames.dofus.datacenter.effects.Effect import Effect
# from com.ankamagames.dofus.datacenter.effects.EffectInstance import EffectInstance
# from com.ankamagames.dofus.datacenter.items.EvolutiveItemType import EvolutiveItemType
# from com.ankamagames.dofus.datacenter.items.ItemSet import ItemSet
# from com.ankamagames.dofus.datacenter.items.ItemType import ItemType
# from com.ankamagames.dofus.datacenter.items.Weapon import Weapon
# from com.ankamagames.dofus.datacenter.jobs.Job import Job
# from com.ankamagames.dofus.datacenter.monsters.Monster import Monster
# from com.ankamagames.dofus.datacenter.monsters.MonsterDrop import MonsterDrop
# from com.ankamagames.dofus.datacenter.monsters.MonsterGrade import MonsterGrade
# from com.ankamagames.dofus.datacenter.monsters.MonsterRace import MonsterRace
# from com.ankamagames.dofus.datacenter.monsters.MonsterSuperRace import MonsterSuperRace
# from com.ankamagames.dofus.datacenter.servers.Server import Server
# from com.ankamagames.dofus.datacenter.servers.ServerCommunity import ServerCommunity
# from com.ankamagames.dofus.datacenter.servers.ServerGameType import ServerGameType
# from com.ankamagames.dofus.datacenter.servers.ServerPopulation import ServerPopulation
# from com.ankamagames.dofus.datacenter.spells.SpellState import SpellState
# from com.ankamagames.dofus.datacenter.world.Area import Area
# from com.ankamagames.dofus.datacenter.world.MapPosition import MapPosition
# from com.ankamagames.dofus.datacenter.world.MapScrollAction import MapScrollAction
from com.ankamagames.dofus.datacenter.world.SubArea import SubArea

# from com.ankamagames.dofus.datacenter.world.SuperArea import SuperArea
# from com.ankamagames.dofus.datacenter.world.WorldMap import WorldMap


class GameDataList:

    CLASSES: list[object] = [
        # Server,
        # ServerCommunity,
        # ServerGameType,
        # ServerPopulation,
        # Monster,
        # MonsterGrade,
        # MonsterRace,
        # MonsterSuperRace,
        # MonsterDrop,
        # Effect,
        # EffectInstance,
        # SpellState,
        # SuperArea,
        # Area,
        # WorldMap,
        SubArea,
        # MapPosition,
        # MapScrollAction,
        # Item,
        # Weapon,
        # Job,
        # ItemSet,
        # AlignmentGift,
        # AlignmentOrder,
        # AlignmentRank,
        # AlignmentRankJntGift,
        # AlignmentSide,
        # AlignmentTitle,
        # ItemType,
        # EvolutiveItemType
    ]

    def __init__(self):
        super().__init__()
