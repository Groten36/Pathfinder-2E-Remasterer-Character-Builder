from abc import ABC, abstractmethod

from Exceptions.CharacterCreationError import CharacterCreationError


class Equipment(ABC):

    def __init__(self, name: str, weight: float):
        if not isinstance(name, str) or not name:
            raise CharacterCreationError("Nazwa przedmiotu ekwipunku musi być niepustym ciągiem znaków.")
        if not isinstance(weight, (int, float)) or weight < 0:
            raise CharacterCreationError("Waga przedmiotu ekwipunku musi być nieujemną liczbą.")
        self._name = name
        self._weight = weight

    def get_name(self) -> str:
        return self._name

    @abstractmethod
    def get_total_weight(self) -> float:

        pass

    @abstractmethod
    def display(self, indent: int = 0) -> None:

        pass

    def _to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self._name,
            "weight": self._weight
        }

    @staticmethod
    def _from_dict(data: dict):
        eq_type = globals().get(data["type"], Equipment)
        if eq_type == SimpleItem:
            return SimpleItem(data["name"], data["weight"], data.get("description", ""))
        elif eq_type == EquipmentContainer:
            container = EquipmentContainer(data["name"], data["weight"], data.get("capacity_kg", float('inf')))
            for item_data in data.get("items", []):
                container.add_item(Equipment._from_dict(item_data))
            return container
        else:
            raise CharacterCreationError(f"Nieznany typ ekwipunku: {data['type']}")

class EquipmentContainer(Equipment):

    def __init__(self, name: str, weight: float, capacity_kg: float = float('inf')):
        super().__init__(name, weight)
        if not isinstance(capacity_kg, (int, float)) or capacity_kg < 0:
            raise CharacterCreationError("Pojemność kontenera musi być nieujemną liczbą.")
        self._items: list[Equipment] = []
        self._capacity_kg = capacity_kg

    def add_item(self, item: Equipment) -> None:

        if not isinstance(item, Equipment):
            raise CharacterCreationError("Można dodawać tylko obiekty dziedziczące po Equipment.")
        if self.get_current_content_weight() + item.get_total_weight() > self._capacity_kg:
            raise CharacterCreationError(f"Kontener '{self._name}' jest pełny. Nie można dodać {item.get_name()}.")
        self._items.append(item)
        print(f"Dodano '{item.get_name()}' do '{self._name}'.")

    def remove_item(self, item_name: str) -> Equipment:

        for i, item in enumerate(self._items):
            if item.get_name() == item_name:
                return self._items.pop(i)
        raise CharacterCreationError(f"Przedmiot '{item_name}' nie znaleziono w '{self._name}'.")

    def get_current_content_weight(self) -> float:

        return sum(item.get_total_weight() for item in self._items)

    def get_total_weight(self) -> float:

        return self._weight + self.get_current_content_weight()

    def display(self, indent: int = 0) -> None:
        prefix = "  " * indent
        print(f"{prefix}+ {self._name} ({self._weight:.1f} kg, Zawartość: {self.get_current_content_weight():.1f}/{self._capacity_kg:.1f} kg)")
        if self._items:
            print(f"{prefix}  Zawartość:")
            for item in self._items:
                item.display(indent + 1)
        else:
            print(f"{prefix}  (Pusty)")

    def _to_dict(self):
        data = super()._to_dict()
        data["capacity_kg"] = self._capacity_kg
        data["items"] = [item._to_dict() for item in self._items]
        return data

class SimpleItem(Equipment):

    def __init__(self, name: str, weight: float, description: str = ""):
        super().__init__(name, weight)
        self._description = description

    def get_total_weight(self) -> float:
        return self._weight

    def display(self, indent: int = 0) -> None:
        prefix = "  " * indent
        print(f"{prefix}- {self._name} ({self._weight:.1f} kg) - {self._description}")

    def _to_dict(self):
        data = super()._to_dict()
        data["description"] = self._description
        return data

