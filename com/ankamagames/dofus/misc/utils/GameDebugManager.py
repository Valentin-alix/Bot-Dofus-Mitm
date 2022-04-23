from com.ankamagames.jerakine.metaclasses.Singleton import Singleton


class GameDebugManager(metaclass=Singleton):

    buffsDebugActivated: bool

    haxeGenerateTestFromNextSpellCast: bool

    haxeGenerateTestFromNextSpellCast_stats: bool

    haxeGenerateTestFromNextSpellCast_infos: bool

    detailedFightLog_unGroupEffects: bool

    detailedFightLog_showIds: bool

    detailedFightLog_showEverything: bool

    detailedFightLog_showBuffsInUi: bool
