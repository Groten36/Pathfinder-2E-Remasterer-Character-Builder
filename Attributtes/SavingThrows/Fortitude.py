from Attributtes.SavingThrows.SavingThrow import SavingThrow
from Proficiency.ProficiencyLevel import ProficiencyLevel

class Fortitude(SavingThrow):
    ability_score_name = "Constitution"

    def __init__(self, proficiency_level: ProficiencyLevel, character_level: int):
        super().__init__("Fortitude",proficiency_level, character_level)