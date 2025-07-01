class CharacterClass:

    def __init__(self, name: str, hp_die: int) -> object:
        self._name = name
        self._hp_die = hp_die

    def class_name(self) -> str:
        return self._name

    def calculate_hit_points(self, constitution_modifier: int) -> int:
        base_hp = self._hp_die + constitution_modifier
        final_hp = self.modify_base_hp(base_hp)
        return final_hp

    def modify_base_hp(self, base_hp: int) -> int:
        raise NotImplementedError("Subclasses must implement method 'modify_base_hp'.")

    def _to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self._name,
            "hp_die": self._hp_die
        }

    @staticmethod
    def _from_dict(data: dict):
        class_type = globals().get(data["type"], CharacterClass)
        return class_type() 