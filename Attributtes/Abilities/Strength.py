from Attributtes.Abilities.Ability import Ability


class Strength(Ability):
    def __init__(self, value: int):
        super().__init__("Strength", value)