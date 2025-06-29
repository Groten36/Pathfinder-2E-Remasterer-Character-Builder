from Exceptions.CharacterCreationError import CharacterCreationError


class Attribute:
    def __init__(self, name: str, value: int):
        if not isinstance(name, str) or not name:
            raise CharacterCreationError("Attribute name must be a string.")
        if not isinstance(value, int):
            raise CharacterCreationError("Attribute value must be a integer.")
        self.name = name
        self.value = value

    def get_name(self) -> str:
        return self.name

    def get_value(self) -> int:
        return self.value

    def set_value(self, new_value: int):
        if not isinstance(new_value, int):
            raise CharacterCreationError("Value must be a integer.")
        self.value = new_value

    def __str__(self):
        return f"{self.name}: {self.value} (Modificator: {self.modifikator()})"