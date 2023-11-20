from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.job.JobBookSubscription import JobBookSubscription
class JobBookSubscriptionMessage:
	def __init__(self, subscriptions:list[JobBookSubscription]):
		self.subscriptions=subscriptions