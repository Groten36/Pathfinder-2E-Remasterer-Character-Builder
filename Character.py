from Ancentries.Ancestry import Ancestry
from AttributeFactory.AbstractAttributeFactory import AbstractAttributeFactory
from AttributeFactory.StandardAttributeFactory import StandardAttributeFactory
from Attributtes.Attribute import Attribute
from Attributtes.SavingThrows.Fortitude import Fortitude
from Attributtes.SavingThrows.Reflex import Reflex
from Attributtes.SavingThrows.SavingThrow import SavingThrow
from Attributtes.SavingThrows.Will import Will
from CharacterClasses.CharacterClass import CharacterClass
from Equipment.Equipment import Equipment
from Exceptions.CharacterCreationError import CharacterCreationError
from Proficiency.ProficiencyLevel import ProficiencyLevel
from Skills.Skill import Skill, TrainedSkill, ExpertSkill, MasterSkill, LegendarySkill, UntrainedSkill


class Character:
    def __init__(self, name: str, ancestry: Ancestry, attributes: dict[str, Attribute], level: int = 1):
        if not isinstance(name, str) or not name:
            raise CharacterCreationError("Imię postaci musi być niepustym ciągiem znaków.")
        if not isinstance(ancestry, Ancestry):
            raise CharacterCreationError("Rasa musi być obiektem klasy Rasa.")
        if not isinstance(attributes, dict) or not all(isinstance(a, Attribute) for a in attributes.values()):
            raise CharacterCreationError("Atrybuty muszą być słownikiem obiektów Atrybut.")
        if not isinstance(level, int) or level < 1:
            raise CharacterCreationError("Poziom postaci musi być dodatnią liczbą całkowitą.")

        self._name = name
        self._ancestry = ancestry
        self._level = level
        self._character_class = None
        self._attributes = attributes
        self._hit_points = 0
        self._saving_throws = {}
        self._skills = {}
        self._inventory: list[Equipment] = []
        self._ancestry.apply_bonuses(self._attributes)
        self._initialize_saving_throws()
        self._initialize_skills()


    @classmethod
    def create_base_character(cls, name: str, ancestry: Ancestry, level: int = 1,attribute_factory: AbstractAttributeFactory = None):

        if attribute_factory is None:
            attribute_factory = StandardAttributeFactory()
        standard_attributes = attribute_factory.create_all_attributes()
        return cls(name, ancestry, standard_attributes, level)


    @staticmethod
    def check_name_validity(name: str) -> bool:
        return bool(name)

    def get_name(self) -> str: return self._name
    def set_name(self, new_name: str):
        if not self.check_name_validity(new_name):
            raise CharacterCreationError("Imię nie może być puste.")
        self._name = new_name

    def get_ancestry(self) -> Ancestry: return self._ancestry
    def get_level(self) -> int: return self._level
    def set_level(self, new_level: int):
        if not isinstance(new_level, int) or new_level < 1:
            raise CharacterCreationError("Poziom postaci musi być dodatnią liczbą całkowitą.")
        self._level = new_level

        self._initialize_saving_throws()
        self._initialize_skills()
        if self._character_class:
            self._hit_points = self._character_class.calculate_hit_points(self._attributes['Constitution'].modifier()) + self._ancestry.get_hp_bonus()



    def get_class(self): return self._character_class
    def set_class(self, new_class: CharacterClass):
        if not hasattr(new_class, 'class_name') or not callable(getattr(new_class, 'class_name')):
             raise CharacterCreationError("Obiekt klasy musi mieć metodę 'class_name()'.")
        self._character_class = new_class

        self._hit_points = self._character_class.calculate_hit_points(self._attributes['Constitution'].modifier()) + self._ancestry.get_hp_bonus()


    def get_attribute(self, attribute_name: str) -> Attribute:
        if attribute_name not in self._attributes:
            raise CharacterCreationError(f"Atrybut '{attribute_name}' nie istnieje.")
        return self._attributes[attribute_name]

    def get_saving_throw(self, save_type: str) -> SavingThrow:

        if save_type not in self._saving_throws:
            raise CharacterCreationError(f"Rzut obronny typu '{save_type}' nie istnieje.")
        return self._saving_throws[save_type]

    def _initialize_saving_throws(self):

        self._saving_throws["Fortitude"] = Fortitude(ProficiencyLevel.UNTRAINED, self._level)
        self._saving_throws["Reflex"] = Reflex(ProficiencyLevel.UNTRAINED, self._level)
        self._saving_throws["Will"] = Will(ProficiencyLevel.UNTRAINED, self._level)

    def _initialize_skills(self):

        self._skills["Akrobatyka"] = UntrainedSkill("Akrobatyka", "Dexterity")
        self._skills["Atletyka"] = UntrainedSkill("Atletyka", "Strength")
        self._skills["Dyplomacja"] = UntrainedSkill("Dyplomacja", "Charisma")
        self._skills["Wiedza Tajemna"] = UntrainedSkill("Wiedza Tajemna", "Inteligence")
        self._skills["Medycyna"] = UntrainedSkill("Medycyna", "Wisdom")

    def get_skill(self, skill_name: str) -> Skill:

        if skill_name not in self._skills:
            raise CharacterCreationError(f"Umiejętność '{skill_name}' nie istnieje.")
        return self._skills[skill_name]

    def set_skill_proficiency(self, skill_name: str, new_proficiency_level: ProficiencyLevel):

        if skill_name not in self._skills:
            raise CharacterCreationError(f"Umiejętność '{skill_name}' nie istnieje.")

        current_skill = self._skills[skill_name]
        current_level_value = current_skill.get_proficiency_level().value
        new_level_value = new_proficiency_level.value

        if new_level_value < current_level_value:
            raise CharacterCreationError(f"Nie można obniżyć poziomu wyszkolenia umiejętności '{skill_name}'.")
        if new_level_value == current_level_value:
            print(f"Umiejętność '{skill_name}' jest już na poziomie {new_proficiency_level.value}.")
            return


        if new_proficiency_level == ProficiencyLevel.TRAINED:
            self._skills[skill_name] = TrainedSkill(current_skill)
        elif new_proficiency_level == ProficiencyLevel.EXPERT:
            self._skills[skill_name] = ExpertSkill(current_skill)
        elif new_proficiency_level == ProficiencyLevel.MASTER:
            self._skills[skill_name] = MasterSkill(current_skill)
        elif new_proficiency_level == ProficiencyLevel.LEGENDARY:
            self._skills[skill_name] = LegendarySkill(current_skill)
        else:
            raise CharacterCreationError(f"Nieprawidłowy poziom wyszkolenia: {new_proficiency_level.value}")


    def add_to_inventory(self, item: Equipment) -> None:

        if not isinstance(item, Equipment):
            raise CharacterCreationError("Można dodawać tylko obiekty dziedziczące po Equipment.")
        self._inventory.append(item)
        print(f"{self.get_name()} dodaje '{item.get_name()}' do swojego ekwipunku.")

    def remove_from_inventory(self, item_name: str) -> Equipment:

        for i, item in enumerate(self._inventory):
            if item.get_name() == item_name:
                removed_item = self._inventory.pop(i)
                print(f"{self.get_name()} usunął '{removed_item.get_name()}' ze swojego ekwipunku.")
                return removed_item
        raise CharacterCreationError(f"Przedmiot '{item_name}' nie znaleziono w ekwipunku {self.get_name()}.")

    def get_total_inventory_weight(self) -> float:

        return sum(item.get_total_weight() for item in self._inventory)

    def display_stats(self):

        print(f"--- Statystyki Postaci: {self._name} ---")
        print(f"Rasa: {self._ancestry.get_ancestry_name()}")
        print(f"Poziom: {self._level}")
        print(f"Klasa: {self._character_class.class_name() if self._character_class else 'Nieustalona'}")
        print(f"Punkty Zdrowia: {self._hit_points}")
        print("Atrybuty:")
        for attribute in self._attributes.values():
            print(f"  - {attribute}")
        print("Rzuty Obronne:")
        for st_name, st_obj in self._saving_throws.items():
            ability_mod = self._attributes[st_obj.ability_score_name].modifier()
            total_bonus = st_obj.calculate_total_bonus(ability_mod)
            print(f"  - {st_name}: {st_obj.get_proficiency_level().value} (Bonus: {total_bonus})")
        print("Umiejętności:")
        for skill_name, skill_obj in self._skills.items():
            governing_attr = self._attributes[skill_obj.get_governing_attribute_name()]
            total_skill_bonus = skill_obj.calculate_total_bonus(self._level, governing_attr.modifier())
            print(f"  - {skill_name}: {skill_obj.get_proficiency_level().value} (Atrybut: {governing_attr.get_name()}, Bonus: {total_skill_bonus})")
        print("Ekwipunek (Całkowita waga: {:.1f} kg):".format(self.get_total_inventory_weight()))
        if self._inventory:
            for item in self._inventory:
                item.display(indent=1)
        else:
            print("  (Ekwipunek pusty)")
        print("---------------------------------")

    def _to_dict(self):

        return {
            "name": self._name,
            "race": self._ancestry._to_dict(),
            "level": self._level,
            "character_class": self._character_class._to_dict() if self._character_class else None,
            "attributes": {name: attr._to_dict() for name, attr in self._attributes.items()},
            "saving_throws": {name: st._to_dict() for name, st in self._saving_throws.items()},
            "skills": {name: skill._to_dict() for name, skill in self._skills.items()},
            "inventory": [item._to_dict() for item in self._inventory]
        }

    @staticmethod
    def from_dict(data: dict):

        name = data["name"]
        race = Ancestry._from_dict(data["race"])
        level = data["level"]


        attributes = {name: Attribute._from_dict(attr_data) for name, attr_data in data["attributes"].items()}


        char = Character(name, race, attributes, level)


        if data["character_class"]:
            char_class = CharacterClass._from_dict(data["character_class"])
            char.set_class(char_class)


        for st_name, st_data in data["saving_throws"].items():
            st_obj = SavingThrow._from_dict(st_data)
            char._saving_throws[st_name] = st_obj


        for skill_name, skill_data in data["skills"].items():
            skill_obj = Skill._from_dict(skill_data)
            char._skills[skill_name] = skill_obj


        char._inventory = [Equipment._from_dict(item_data) for item_data in data["inventory"]]

        return char


