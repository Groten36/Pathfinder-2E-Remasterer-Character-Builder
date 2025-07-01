from CharacterClasses.CharacterClass import CharacterClass


class Cleric(CharacterClass):
    _default_hp_start = 8
    def __init__(self):
        super().__init__("Cleric", Cleric._default_hp_start)

    def modify_base_hp(self, base_hp: int) -> int:
        return base_hp