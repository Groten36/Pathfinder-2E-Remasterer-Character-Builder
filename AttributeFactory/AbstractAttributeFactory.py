from Attributtes.Abilities.Charisma import Charisma
from Attributtes.Abilities.Constitution import Constitution
from Attributtes.Abilities.Dexterity import Dexterity
from Attributtes.Abilities.Intelligence import Intelligence
from Attributtes.Abilities.Strength import Strength
from Attributtes.Abilities.Wisdom import Wisdom
from Attributtes.Attribute import Attribute


class AbstractAttributeFactory:

    def create_strength(self) -> Strength:
        raise NotImplementedError
    def create_dexterity(self) -> Dexterity:
        raise NotImplementedError
    def create_constitution(self) -> Constitution:
        raise NotImplementedError
    def create_intelligence(self) -> Intelligence:
        raise NotImplementedError
    def create_wisdom(self) -> Wisdom:
        raise NotImplementedError
    def create_charisma(self) -> Charisma:
        raise NotImplementedError

    def create_all_attributes(self) -> dict[str, Attribute]:
        return {
            "Strength": self.create_strength(),
            "Dexterity": self.create_dexterity(),
            "Constitution": self.create_constitution(),
            "Inteligence": self.create_intelligence(),
            "Wisdom": self.create_wisdom(),
            "Charisma": self.create_charisma()
        }