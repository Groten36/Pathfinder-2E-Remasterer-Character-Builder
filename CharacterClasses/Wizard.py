from CharacterClasses.CharacterClass import CharacterClass


class Wizard(CharacterClass):
    _default_hp_start = 6
    def __init__(self):
        super().__init__("Wizard", Wizard._default_hp_start)

    def modify_base_hp(self, base_hp: int) -> int:
        return base_hp