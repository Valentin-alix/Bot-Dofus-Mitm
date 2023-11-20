from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.dialog.LeaveDialogMessage import LeaveDialogMessage
if TYPE_CHECKING:
	...
class ExchangeLeaveMessage(LeaveDialogMessage):
	def __init__(self, success:bool, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.success=success