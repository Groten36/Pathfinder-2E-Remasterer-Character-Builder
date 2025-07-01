from CharacterClasses.CharacterClass import CharacterClass


class Fighter(CharacterClass):
    _default_hp_start = 10
    def __init__(self):
        super().__init__("Fighter", Fighter._default_hp_start)

    def modify_base_hp(self, base_hp: int) -> int:
        return base_hp + 2