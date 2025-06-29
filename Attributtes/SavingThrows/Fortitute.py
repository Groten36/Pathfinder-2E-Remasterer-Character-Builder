from Attributtes.SavingThrows import SavingThrow
from Proficiency.Proficiency import ProficiencyLevel

class Fortitude(SavingThrow):
    ability_score_name = "Constitution"

    def __init__(self, proficiency_level: ProficiencyLevel, character_level: int,name="Fortitude"):
        super().__init__(name,proficiency_level, character_level)