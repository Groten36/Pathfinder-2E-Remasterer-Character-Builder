from Exceptions.CharacterCreationError import CharacterCreationError
from Attributtes.Attribute import Attribute

class Ability(Attribute):
    def __init__(self, name: str, value: int):
        super().__init__(name, value)

    def modifier(self) -> int:
        return (self.value - 10) // 2

