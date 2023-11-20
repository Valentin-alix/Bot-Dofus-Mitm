from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformation import AllianceInformation
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.collector.tax.AdditionalTaxCollectorInformation import AdditionalTaxCollectorInformation
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.collector.tax.TaxCollectorComplementaryInformations import TaxCollectorComplementaryInformations
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristics import CharacterCharacteristics
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.collector.tax.TaxCollectorOrderedSpell import TaxCollectorOrderedSpell
class TaxCollectorInformations:
	def __init__(self, uniqueId:float, firstNameId:int, lastNameId:int, allianceIdentity:AllianceInformation, additionalInfos:AdditionalTaxCollectorInformation, worldX:int, worldY:int, subAreaId:int, state:int, look:EntityLook, complements:list[TaxCollectorComplementaryInformations], characteristics:CharacterCharacteristics, equipments:list[ObjectItem], spells:list[TaxCollectorOrderedSpell]):
		self.uniqueId=uniqueId
		self.firstNameId=firstNameId
		self.lastNameId=lastNameId
		self.allianceIdentity=allianceIdentity
		self.additionalInfos=additionalInfos
		self.worldX=worldX
		self.worldY=worldY
		self.subAreaId=subAreaId
		self.state=state
		self.look=look
		self.complements=complements
		self.characteristics=characteristics
		self.equipments=equipments
		self.spells=spells