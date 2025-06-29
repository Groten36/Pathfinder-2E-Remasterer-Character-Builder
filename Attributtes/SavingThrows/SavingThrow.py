from Attributtes.Attribute import Attribute
from Proficiency.Proficiency import ProficiencyLevel
from Exceptions.CharacterCreationError import CharacterCreationError

class SavingThrow(Attribute):

    _proficiency_base_bonus = {
        ProficiencyLevel.UNTRAINED: 0,
        ProficiencyLevel.TRAINED: 2,
        ProficiencyLevel.EXPERT: 4,
        ProficiencyLevel.MASTER: 6,
        ProficiencyLevel.LEGENDARY: 8,
    }

    _ability_score_name: str = None

    def __init__(self, name, proficiency_level: ProficiencyLevel, character_level: int,value=0):
        super().__init__(name, value)
        if not isinstance(proficiency_level, ProficiencyLevel):
            raise CharacterCreationError("Proficiency Level must be valid.")
        if not isinstance(character_level, int) or character_level < 0:
            raise CharacterCreationError("Character Level must be valid.")
        if self._ability_score_name is None:
            raise NotImplementedError("Subclasses must have valid 'ability_score_name'.")

        self.proficiency_level = proficiency_level
        self.character_level = character_level
        self.item_bonus = 0
        self.other_bonuses = 0

    def get_proficiency_level(self) -> ProficiencyLevel:
        return self.proficiency_level

    def set_proficiency_level(self, new_level: ProficiencyLevel):
        if not isinstance(new_level, ProficiencyLevel):
            raise CharacterCreationError(" ProficiencyLevel must be valid.")
        self.proficiency_level = new_level

    def get_character_level(self) -> int:
        return self.character_level

    def set_character_level(self, new_level: int):
        if not isinstance(new_level, int) or new_level < 0:
            raise CharacterCreationError("Character Level must be valid.")
        self.character_level = new_level

    def get_item_bonus(self) -> int:
        return self.item_bonus

    def set_item_bonus(self, bonus: int):
        if not isinstance(bonus, int):
            raise CharacterCreationError("Character Bonus must be valid.")
        self.item_bonus = bonus

    def get_other_bonuses(self) -> int:
        return self.other_bonuses

    def set_other_bonuses(self, bonus: int):
        if not isinstance(bonus, int):
            raise CharacterCreationError("Inne premie muszą być liczbą całkowitą.")
        self.other_bonuses = bonus

    def calculate_proficiency_bonus(self) -> int:
        base_bonus = self._proficiency_base_bonus[self.proficiency_level]
        if self.proficiency_level != ProficiencyLevel.UNTRAINED:
            return base_bonus + self.character_level
        return base_bonus

    def calculate_total_bonus(self, ability_modifier: int) -> int:
        if not isinstance(ability_modifier, int):
            raise CharacterCreationError("Modyfikator atrybutu musi być liczbą całkowitą.")

        proficiency_bonus = self.calculate_proficiency_bonus()
        return (proficiency_bonus +
                ability_modifier +
                self.item_bonus +
                self.other_bonuses)

    def upgrade(self):
        self.value = self.calculate_total_bonus(self.get_character_level())

    def __str__(self):
        return (f"{self.__class__.__name__} (Proficiensy: {self.proficiency_level.value}, "
                f"Character level: {self.character_level})")

    @staticmethod
    def get_all_saving_throw_types() -> list[str]:
        return ["Fortitude", "Reflex", "Will"]