from Attributtes.Abilities.Ability import Ability


class Charisma(Ability):
    def __init__(self, value: int):
        super().__init__("Charisma", value)