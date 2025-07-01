from Attributtes.SavingThrows.SavingThrow import SavingThrow
from Proficiency.ProficiencyLevel import ProficiencyLevel


class Reflex(SavingThrow):
    ability_score_name = "Dexterity"

    def __init__(self, proficiency_level: ProficiencyLevel, character_level: int,name="Reflex"):
        super().__init__(name,proficiency_level, character_level)
