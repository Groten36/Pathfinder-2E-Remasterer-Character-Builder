from Attributtes.Abilities.Ability import Ability


class Dexterity(Ability):
    def __init__(self, value: int):
        super().__init__("Dexterity", value)