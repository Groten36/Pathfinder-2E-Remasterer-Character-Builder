from Ancentries.Ancestry import Ancestry
from Attributtes.Attribute import Attribute


class Human(Ancestry):
    _ancestry_name = "Human"

    def __init__(self):
        super().__init__()

    def apply_bonuses(self, character_attributes: dict[str, Attribute]) -> None:
        print(f"Ancentry {self.get_ancestry_name()} doesn't give specific bonuses.")
        pass

    def get_race_name(self):
        return self._ancestry_name