from Attributtes.Attribute import Attribute


class Ancestry:

    _ancestry_name: str = "Unknown"

    def __init__(self):
        if self._ancestry_name == "Unknown":
            raise NotImplementedError("Subclasses must define ancestry name.")

    def get_ancestry_name(self) -> str:
        return self._ancestry_name

    def apply_bonuses(self, character_attributes: dict[str, Attribute]) -> None:
        pass

    def get_hp_bonus(self) -> int:
        return 0

    def _to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self._ancestry_name
        }

    @staticmethod
    def _from_dict(data: dict):
        race_type = globals().get(data["type"], Ancestry)
        return race_type()