from Attributtes.Abilities.Ability import Ability


class Intelligence(Ability):
    def __init__(self, value: int):
        super().__init__("Intelligence", value)