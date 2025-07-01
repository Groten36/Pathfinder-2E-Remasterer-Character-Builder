from Attributtes.SavingThrows.SavingThrow import SavingThrow
from Proficiency.ProficiencyLevel import ProficiencyLevel


class Will(SavingThrow):
    ability_score_name = "Wisdom"

    def __init__(self, proficiency_level: ProficiencyLevel, character_level: int, name="Will",):
        super().__init__(name,proficiency_level, character_level)