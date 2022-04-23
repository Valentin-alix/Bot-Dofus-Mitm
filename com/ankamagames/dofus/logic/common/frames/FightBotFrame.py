import math
import random
from threading import Timer
from types import FunctionType
from whistle import Event
from com.ankamagames.atouin.managers.EntitiesManager import EntitiesManager
from com.ankamagames.atouin.managers.MapDisplayManager import MapDisplayManager
from com.ankamagames.atouin.messages.CellClickMessage import CellClickMessage
from com.ankamagames.atouin.messages.MapLoadedMessage import MapLoadedMessage
from com.ankamagames.dofus.datacenter.world.MapPosition import MapPosition
from com.ankamagames.dofus.kernel.Kernel import Kernel
from com.ankamagames.dofus.kernel.net.ConnectionType import ConnectionType
from com.ankamagames.dofus.kernel.net.ConnectionsHandler import ConnectionsHandler
from com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager import PlayedCharacterManager
from com.ankamagames.dofus.logic.game.common.misc.DofusEntities import DofusEntities
from com.ankamagames.dofus.logic.game.fight.frames.FightEntitiesFrame import FightEntitiesFrame
from com.ankamagames.dofus.logic.game.fight.miscs.FightReachableCellsMaker import FightReachableCellsMaker
from com.ankamagames.dofus.logic.game.roleplay.frames.RoleplayEntitiesFrame import RoleplayEntitiesFrame
from com.ankamagames.dofus.network.messages.authorized.AdminQuietCommandMessage import AdminQuietCommandMessage
from com.ankamagames.dofus.network.messages.common.basic.BasicPingMessage import BasicPingMessage
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightCastRequestMessage import GameActionFightCastRequestMessage
from com.ankamagames.dofus.network.messages.game.actions.sequence.SequenceEndMessage import SequenceEndMessage
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightEndMessage import GameFightEndMessage
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightJoinMessage import GameFightJoinMessage
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightReadyMessage import GameFightReadyMessage
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightTurnFinishMessage import GameFightTurnFinishMessage
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightTurnStartMessage import GameFightTurnStartMessage
from com.ankamagames.dofus.network.messages.game.context.fight.character.GameFightShowFighterMessage import GameFightShowFighterMessage
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapFightCountMessage import MapFightCountMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import GameFightFighterInformations
from com.ankamagames.dofus.network.types.game.context.fight.GameFightMonsterInformations import GameFightMonsterInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayGroupMonsterInformations import GameRolePlayGroupMonsterInformations
from com.ankamagames.jerakine.entities.interfaces.IEntity import IEntity
from com.ankamagames.jerakine.entities.interfaces.IInteractive import IInteractive
from com.ankamagames.jerakine.messages.Frame import Frame
from com.ankamagames.jerakine.messages.Message import Message
from com.ankamagames.jerakine.metaclasses.Singleton import Singleton
from com.ankamagames.jerakine.pools.GenericPool import GenericPool
from com.ankamagames.jerakine.types.enums.Priority import Priority
from com.ankamagames.jerakine.types.positions.MapPoint import MapPoint

class FightBotFrame(Frame, metaclass=Singleton):   
   
   _frameFightListRequest:bool
   
   _fightCount:int = 0
   
   _mapPos:list
   
   _enabled:bool
   
   _inFight:bool
   
   _lastElemOver:Sprite
   
   _lastEntityOver:IInteractive
   
   _wait:bool
   
   _turnPlayed:int
   
   _myTurn:bool
   
   _turnAction:list
   
   def __init__(self):
      self._rollOverTimer = Timer(2, 0, self.randomOver)
      self._actionTimer = Timer(5, 0, self.onAction)
      self._turnAction = []
      super().__init__()
      self.initRight()
   
   def pushed(self) -> bool:
      self._enabled = True
      self.fakeActivity()
      self._myTurn = False
      self._actionTimer.start()
      self._rollOverTimer.start()
      self._mapPos = MapPosition.getMapPositions()
      mfcMsg:MapFightCountMessage = MapFightCountMessage()
      mfcMsg.init(fightCount_=1)
      self.process(mfcMsg)
      return True
   
   def pulled(self) -> bool:
      self._rollOverTimer.cancel()
      self._actionTimer.cancel()
      self._enabled = False
      return True
   
   @property
   def priority(self) -> int:
      return Priority.ULTIMATE_HIGHEST_DEPTH_OF_DOOM
   
   @property
   def fightCount(self) -> int:
      return self._fightCount
   
   def process(self, msg:Message) -> bool:
      
      if isinstance(msg, GameFightJoinMessage):
         self._fightCount += 1
         self._inFight = True
            
      if isinstance(msg, GameFightEndMessage):
         self._inFight = False
            
      if isinstance(msg, MapComplementaryInformationsDataMessage):
         self._wait = False
            
      if isinstance(msg, MapLoadedMessage):
         self._wait = True
            
      if isinstance(msg, GameFightShowFighterMessage):
         self.sendAdminCmd("givelife *")
         self.sendAdminCmd("giveenergy *")
         self._turnPlayed = 0
         self._myTurn = False
         startFightMsg = GameFightReadyMessage()
         startFightMsg.init(isReady_=True)
         ConnectionsHandler.getConnection().send(startFightMsg)
         
      if isinstance(msg, GameFightTurnStartMessage):
            turnStartMsg = msg
            self._turnAction = []
            if turnStartMsg.id == PlayedCharacterManager().id:
               self._myTurn = True
               self._turnPlayed+=1
               if self._turnPlayed > 2:
                  self.castSpell(411, True)
               else:
                  self.addTurnAction(self.fightRandomMove, [])
                  self.addTurnAction(self.castSpell, [173, False])
                  self.addTurnAction(self.castSpell, [173, False])
                  self.addTurnAction(self.castSpell, [173, False])
                  self.addTurnAction(self.turnEnd, [])
                  self.nextTurnAction()
            else:
               self._myTurn = False
               
      if isinstance(msg, SequenceEndMessage):
            self.nextTurnAction()
            
      return False
   
   def initRight(self) -> None:
      self.sendAdminCmd("adminaway")
      self.sendAdminCmd("givelevel * 200")
      self.sendAdminCmd("givespell * 173 6")
      self.sendAdminCmd("givespell * 411 6")
      self.sendAdminCmd("dring po=63, vita=8000, pa=100, agi=150 True")
   
   def sendAdminCmd(self, cmd:str) -> None:
      aqcmsg:AdminQuietCommandMessage = AdminQuietCommandMessage()
      aqcmsg.init(content_=cmd)
      ConnectionsHandler.getConnection().send(aqcmsg)
   
   def onAction(self, e:Event) -> None:
      if random.random() < 0.9:
         self.randomWalk()
      else:
         self.randomMove()
   
   def nextTurnAction(self) -> None:
      action:object = None
      if len(self._turnAction):
         action = self._turnAction.pop(0)
         action.fct.apply(self,action.args)
   
   def addTurnAction(self, fct:FunctionType, args:list) -> None:
         "fct":fct,
         "args":args
   
   def turnEnd(self) -> None:
      finDeTourMsg:GameFightTurnFinishMessage = GameFightTurnFinishMessage()
      finDeTourMsg.initGameFightTurnFinishMessage()
      ConnectionsHandler.getConnection().send(finDeTourMsg)
   
   def join(self, name:str) -> None:
      if self._inFight or self._wait:
         return
      aqcmsg:AdminQuietCommandMessage = AdminQuietCommandMessage()
      aqcmsg.init("join " + name)
      ConnectionsHandler.getConnection().send(aqcmsg)
      self._actionTimer.reset()
      self._actionTimer.start()
   
   def randomMove(self) -> None:
      if self._inFight or self._wait:
         return
      mapPos:MapPosition = self._mapPos[int(random.random() * len(self._mapPos))]
      aqcmsg:AdminQuietCommandMessage = AdminQuietCommandMessage()
      aqcmsg.init("moveto " + mapPos.id)
      ConnectionsHandler.getConnection().send(aqcmsg)
      self._actionTimer.cancel()
      self._actionTimer.start()
   
   def fakeActivity(self) -> None:
      if not self._enabled:
         return
      setTimeout(self.fakeActivity, 60 * 5)
      bpmgs:BasicPingMessage = BasicPingMessage()
      bpmgs.init(False)
      ConnectionsHandler.getConnection().send(bpmgs, ConnectionType.TO_ALL_SERVERS)
   
   def randomWalk(self) -> None:
      entity = None
      groupEntity:IEntity = None
      if self._inFight or self._wait:
         return
      rpEF:RoleplayEntitiesFrame = Kernel().getWorker().getFrame(RoleplayEntitiesFrame)
      if not rpEF:
         return
      avaibleCells:list = []
      for entity in rpEF.entities:
         if isinstance(entity, GameRolePlayGroupMonsterInformations):
            groupEntity = DofusEntities.getEntity(GameRolePlayGroupMonsterInformations(entity).contextualId)
            avaibleCells.append(MapPoint.fromCellId(groupEntity.position.cellId))
      if not avaibleCells or not len(avaibleCells):
         return
      ccmsg:CellClickMessage = CellClickMessage()
      ccmsg.cell = avaibleCells[math.floor(len(avaibleCells) * random.random())]
      ccmsg.cellId = ccmsg.cell.cellId
      ccmsg.id = MapDisplayManager().currentMapPoint.mapId
      Kernel.getWorker().process(ccmsg)
   
   def fightRandomMove(self) -> None:
      reachableCells:FightReachableCellsMaker = FightReachableCellsMakerFightEntitiesFrame.getCurrentInstance().getEntityInfos(PlayedCharacterManager().id)
      if not len(reachableCells.reachableCells):
         self.nextTurnAction()
         return
      ccmsg:CellClickMessage = CellClickMessage()
      ccmsg.cell = MapPoint.fromCellId(reachableCells.reachableCells[math.floor(len(reachableCells.reachableCells) * random.random())])
      ccmsg.cellId = ccmsg.cell.cellId
      ccmsg.id = MapDisplayManager().currentMapPoint.mapId
      Kernel.getWorker().process(ccmsg)
   
   def randomOver(self, *foo) -> None:
      e:IEntity = None
      entity:IInteractive = None
      if self._wait:
         return
      avaibleEntities:list = []
      for e in EntitiesManager().entities:
         if isinstance(e, IInteractive):
            avaibleEntities.append(e)
      entity = avaibleEntities[math.floor(len(avaibleEntities) * random.random())]
      if not entity:
         return
      if self._lastEntityOver:
         emomsg2 = EntityMouseOutMessage(self._lastEntityOver)
         Kernel.getWorker().process(emomsg2)
      self._lastEntityOver = entity
      emomsg:EntityMouseOverMessage = EntityMouseOverMessage(entity)
      Kernel.getWorker().process(emomsg)
      avaibleElem:list = []
      for ui in Berilia().uiList:
         for elem in ui.getElements():
            if elem.mouseChildren or elem.mouseEnabled:
               avaibleElem.append(elem)
      if not len(avaibleElem):
         return
      if self._lastElemOver:
         momsg2 = GenericPool.get(MouseOutMessage,self._lastElemOver,MouseEvent(MouseEvent.MOUSE_OUT))
         Kernel.getWorker().process(momsg2)
      target:GraphicContainer = avaibleElem[math.floor(len(avaibleElem) * Math.random())]
      momsg:MouseOverMessage = GenericPool.get(MouseOverMessage,target,MouseEvent(MouseEvent.MOUSE_OVER))
      Kernel.getWorker().process(momsg)
      self._lastElemOver = target
   
   def castSpell(self, spellId:int, onMySelf:bool) -> None:
      cellId:int = 0
      avaibleCells:list = None
      entity = None
      monster:GameFightMonsterInformations = None
      gafcrmsg:GameActionFightCastRequestMessage = GameActionFightCastRequestMessage()
      if onMySelf:
         cellId = FightEntitiesFrame.getCurrentInstance().getEntityInfos(PlayedCharacterManager().id).disposition.cellId
      else:
         avaibleCells = []
         for entity in FightEntitiesFrame.getCurrentInstance().entities:
            if entity.contextualId < 0 and isinstance(entity, GameFightMonsterInformations):
               monster = entity
               if monster.spawnInfo.alive:
                  avaibleCells.append(entity.disposition.cellId)
         cellId = avaibleCells[math.floor(len(avaibleCells) * random.random())]
      gafcrmsg.init(spellId, cellId)
      ConnectionsHandler.getConnection().send(gafcrmsg)
