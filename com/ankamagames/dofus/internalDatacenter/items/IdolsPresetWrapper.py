from com.ankamagames.dofus.internalDatacenter.items.PresetWrapper import PresetWrapper


class IdolsPresetWrapper(PresetWrapper):

    idolsIds: list[int]

    def __init__(self):
        super().__init__()

    def create(
        self, pPresetId: int, pIconId: int, pIdolsIds: list[int]
    ) -> "IdolsPresetWrapper":
        idolsPreset: IdolsPresetWrapper = IdolsPresetWrapper()
        idolsPreset.id = pPresetId
        idolsPreset.gfxId = pIconId
        idolsPreset.idolsIds = pIdolsIds
        return idolsPreset
