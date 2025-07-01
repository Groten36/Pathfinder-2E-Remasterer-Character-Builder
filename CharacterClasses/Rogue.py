from CharacterClasses.CharacterClass import CharacterClass


class Rogue(CharacterClass):
    _default_hp_start = 8
    def __init__(self):
        super().__init__("Rogue", Rogue._default_hp_start)

    def modify_base_hp(self, base_hp: int) -> int:
        return base_hp