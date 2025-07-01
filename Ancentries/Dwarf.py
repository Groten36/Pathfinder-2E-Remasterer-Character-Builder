from Ancentries.Ancestry import Ancestry
from Attributtes.Attribute import Attribute


class Dwarf(Ancestry):
    _ancestry_name = "Dwarf"

    def __init__(self):
        super().__init__()

    def apply_bonuses(self, character_attributes: dict[str, Attribute]) -> None:
        if "Constitution" in character_attributes:
            current_con = character_attributes["Constitution"].get_value()
            character_attributes["Constitution"].set_value(current_con + 2)
            print(f"Ancentry bonus: Constitution increase by 2 {character_attributes['Constitution'].get_value()}")
        if "Charisma" in character_attributes:
            current_cha = character_attributes["Charisma"].get_value()
            character_attributes["Charisma"].set_value(current_cha - 2)
            print(f"Ancentry penalty: Charisma decrease by 2 {character_attributes['Charisma'].get_value()}")

    def get_hp_bonus(self) -> int:
        return 2