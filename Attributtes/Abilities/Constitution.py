from Attributtes.Abilities.Ability import Ability


class Constitution(Ability):
    def __init__(self, value: int):
        super().__init__("Constitution", value)