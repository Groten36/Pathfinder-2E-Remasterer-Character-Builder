from Ancentries.Ancestry import Ancestry
from Attributtes.Attribute import Attribute

class Elf(Ancestry):
    _ancestry_name = "Elf"

    def __init__(self):
        super().__init__()

    def apply_bonuses(self, character_attributes: dict[str, Attribute]) -> None:
        if "Dexterity" in character_attributes:
            current_dex = character_attributes["Dexterity"].get_value()
            character_attributes["Dexterity"].set_value(current_dex+2)
            print(f"Ancestry bonus: Dexterity increase by 2 {character_attributes['Dexterity'].get_value()}")
        if "Constitution" in character_attributes:
            current_con = character_attributes["Constitution"].get_value()
            character_attributes["Constitution"].set_value(current_con - 2)
            print(f"Ancestry penalty: Constitution decrease by 2 {character_attributes['Constitution'].get_value()}")
