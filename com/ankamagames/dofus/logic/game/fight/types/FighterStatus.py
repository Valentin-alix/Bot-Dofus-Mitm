class FighterStatus:
    cantUseSpells: bool
    cantUseCloseQuarterAttack: bool
    cantDealDamage: bool
    invulnerable: bool
    incurable: bool
    cantBeMoved: bool
    cantBePushed: bool
    cantSwitchPosition: bool
    invulnerableMelee: bool
    invulnerableRange: bool
    cantTackle: bool
    cantBeTackled: bool

    def __init__(self):
        super().__init__()
