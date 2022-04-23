from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AllianceVersatileInformations(NetworkMessage):
    allianceId: int
    nbGuilds: int
    nbMembers: int
    nbSubarea: int

    def init(self, allianceId_: int, nbGuilds_: int, nbMembers_: int, nbSubarea_: int):
        self.allianceId = allianceId_
        self.nbGuilds = nbGuilds_
        self.nbMembers = nbMembers_
        self.nbSubarea = nbSubarea_

        super().__init__()
