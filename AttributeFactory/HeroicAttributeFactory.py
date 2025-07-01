from AttributeFactory.AbstractAttributeFactory import AbstractAttributeFactory
from Attributtes.Abilities.Charisma import Charisma
from Attributtes.Abilities.Constitution import Constitution
from Attributtes.Abilities.Dexterity import Dexterity
from Attributtes.Abilities.Intelligence import Intelligence
from Attributtes.Abilities.Strength import Strength
from Attributtes.Abilities.Wisdom import Wisdom


class HeroicAttributeFactory(AbstractAttributeFactory):
    def create_strength(self) -> Strength: return Strength(14)
    def create_dexterity(self) -> Dexterity: return Dexterity(12)
    def create_constitution(self) -> Constitution: return Constitution(10)
    def create_intelligence(self) -> Intelligence: return Intelligence(10)
    def create_wisdom(self) -> Wisdom: return Wisdom(10)
    def create_charisma(self) -> Charisma: return Charisma(8)