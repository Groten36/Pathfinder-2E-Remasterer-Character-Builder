from Attributtes.Abilities.Ability import Ability


class Wisdom(Ability):
    def __init__(self, value: int):
        super().__init__("Wisdom", value)