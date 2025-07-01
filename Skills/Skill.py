from abc import ABC, abstractmethod

from Exceptions.CharacterCreationError import CharacterCreationError
from Proficiency.ProficiencyLevel import ProficiencyLevel


class Skill(ABC):

    def __init__(self, name: str, governing_attribute_name: str):
        self._name = name
        self._governing_attribute_name = governing_attribute_name

    def get_name(self) -> str:
        return self._name

    def get_governing_attribute_name(self) -> str:
        return self._governing_attribute_name

    @abstractmethod
    def get_proficiency_level(self) -> ProficiencyLevel:

        pass

    @abstractmethod
    def get_proficiency_bonus(self, character_level: int) -> int:

        pass

    def calculate_total_bonus(self, character_level: int, attribute_modifier: int) -> int:

        return self.get_proficiency_bonus(character_level) + attribute_modifier

    def _to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self._name,
            "governing_attribute_name": self._governing_attribute_name,
            "proficiency_level": self.get_proficiency_level()._to_dict()
        }

    @staticmethod
    def _from_dict(data: dict):
        skill_type = globals().get(data["type"], UntrainedSkill)
        skill = UntrainedSkill(data["name"], data["governing_attribute_name"])

        proficiency_level = ProficiencyLevel._from_dict(data["proficiency_level"])
        if proficiency_level == ProficiencyLevel.TRAINED:
            skill = TrainedSkill(skill)
        elif proficiency_level == ProficiencyLevel.EXPERT:
            skill = ExpertSkill(skill)
        elif proficiency_level == ProficiencyLevel.MASTER:
            skill = MasterSkill(skill)
        elif proficiency_level == ProficiencyLevel.LEGENDARY:
            skill = LegendarySkill(skill)
        return skill

class SkillDecorator(Skill, ABC):

    def __init__(self, skill: Skill):
        super().__init__(skill.get_name(), skill.get_governing_attribute_name())
        self._decorated_skill = skill

    def get_proficiency_level(self) -> ProficiencyLevel:
        return self._decorated_skill.get_proficiency_level()

    @abstractmethod
    def get_proficiency_bonus(self, character_level: int) -> int:
        pass

class ExpertSkill(SkillDecorator):

    def __init__(self, skill: Skill):
        super().__init__(skill)
        if skill.get_proficiency_level().value >= ProficiencyLevel.EXPERT.value:
            raise CharacterCreationError("Umiejętność jest już biegła lub ma wyższy poziom.")

    def get_proficiency_level(self) -> ProficiencyLevel:
        return ProficiencyLevel.EXPERT

    def get_proficiency_bonus(self, character_level: int) -> int:
        return 4 + character_level

class LegendarySkill(SkillDecorator):

    def __init__(self, skill: Skill):
        super().__init__(skill)
        if skill.get_proficiency_level().value >= ProficiencyLevel.LEGENDARY.value:
            raise CharacterCreationError("Umiejętność jest już legendarna.")

    def get_proficiency_level(self) -> ProficiencyLevel:
        return ProficiencyLevel.LEGENDARY

    def get_proficiency_bonus(self, character_level: int) -> int:
        return 8 + character_level


class MasterSkill(SkillDecorator):

    def __init__(self, skill: Skill):
        super().__init__(skill)
        if skill.get_proficiency_level().value >= ProficiencyLevel.MASTER.value:
            raise CharacterCreationError("Umiejętność jest już mistrzowska lub ma wyższy poziom.")

    def get_proficiency_level(self) -> ProficiencyLevel:
        return ProficiencyLevel.MASTER

    def get_proficiency_bonus(self, character_level: int) -> int:
        return 6 + character_level

class TrainedSkill(SkillDecorator):

    def __init__(self, skill: Skill):
        super().__init__(skill)
        if skill.get_proficiency_level().value >= ProficiencyLevel.TRAINED.value:
            raise CharacterCreationError("Umiejętność jest już wyszkolona lub ma wyższy poziom.")

    def get_proficiency_level(self) -> ProficiencyLevel:
        return ProficiencyLevel.TRAINED

    def get_proficiency_bonus(self, character_level: int) -> int:
        return 2 + character_level


class UntrainedSkill(Skill):

    def __init__(self, name: str, governing_attribute_name: str):
        super().__init__(name, governing_attribute_name)

    def get_proficiency_level(self) -> ProficiencyLevel:
        return ProficiencyLevel.UNTRAINED

    def get_proficiency_bonus(self, character_level: int) -> int:
        return 0

