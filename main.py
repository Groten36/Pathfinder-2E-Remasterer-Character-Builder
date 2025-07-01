import json

from Ancentries.Dwarf import Dwarf
from Ancentries.Elf import Elf
from Ancentries.Human import Human
from AttributeFactory.HeroicAttributeFactory import HeroicAttributeFactory
from AttributeFactory.StandardAttributeFactory import StandardAttributeFactory
from Character import Character
from CharacterClasses.Cleric import Cleric
from CharacterClasses.Fighter import Fighter
from CharacterClasses.Rogue import Rogue
from CharacterClasses.Wizard import Wizard
from Equipment.Equipment import EquipmentContainer, SimpleItem
from Exceptions.CharacterCreationError import CharacterCreationError
from Proficiency.ProficiencyLevel import ProficiencyLevel

def save_character_to_file(character: Character, filename: str):

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(character._to_dict(), f, indent=4, ensure_ascii=False)
        print(f"Postać '{character.get_name()}' została zapisana do pliku '{filename}'.")
    except Exception as e:
        print(f"Błąd podczas zapisywania postaci: {e}")

def load_character_from_file(filename: str) -> Character | None:

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        character = Character.from_dict(data)
        print(f"Postać '{character.get_name()}' została wczytana z pliku '{filename}'.")
        return character
    except FileNotFoundError:
        print(f"Błąd: Plik '{filename}' nie istnieje.")
        return None
    except json.JSONDecodeError:
        print(f"Błąd: Nieprawidłowy format JSON w pliku '{filename}'.")
        return None
    except Exception as e:
        print(f"Błąd podczas wczytywania postaci: {e}")
        return None

def create_new_character_interactive() -> Character:

    print("\n--- Tworzenie Nowej Postaci ---")
    name = input("Podaj imię postaci: ")
    while not name:
        print("Imię nie może być puste.")
        name = input("Podaj imię postaci: ")

    print("\nWybierz rasę:")
    print("1. Człowiek")
    print("2. Elf")
    print("3. Krasnolud")
    race_choice = input("Wybierz numer rasy (1-3): ")
    chosen_race = None
    if race_choice == '1':
        chosen_race = Human()
    elif race_choice == '2':
        chosen_race = Elf()
    elif race_choice == '3':
        chosen_race = Dwarf()
    else:
        print("Nieprawidłowy wybór rasy. Domyślnie ustawiono Człowiek.")
        chosen_race = Human()

    level = 1

    print("\nWybierz typ atrybutów:")
    print("1. Standardowe (wszystko 10)")
    print("2. Heroiczne (wyższe wartości początkowe)")
    attr_choice = input("Wybierz numer typu atrybutów (1-2): ")
    attr_factory = None
    if attr_choice == '1':
        attr_factory = StandardAttributeFactory()
    elif attr_choice == '2':
        attr_factory = HeroicAttributeFactory()
    else:
        print("Nieprawidłowy wybór typu atrybutów. Domyślnie ustawiono Standardowe.")
        attr_factory = StandardAttributeFactory()

    new_character = Character.create_base_character(name, chosen_race, level, attr_factory)

    print("\nWybierz klasę postaci:")
    print("1. Wojownik")
    print("2. Czarodziej")
    print("3. Rogue")
    print("3. Cleric")
    class_choice = input("Wybierz numer klasy (1-3): ")
    if class_choice == '1':
        new_character.set_class(Fighter())
    elif class_choice == '2':
        new_character.set_class(Wizard())
    elif class_choice == '3':
        new_character.set_class(Rogue())
    elif class_choice == '4':
        new_character.set_class(Cleric())
    else:
        print("Nieprawidłowy wybór klasy. Klasa nie została ustawiona.")


    if new_character.get_class():
        if new_character.get_class().class_name() == "Wojownik":
            new_character.get_saving_throw("Fortitude").set_proficiency_level(ProficiencyLevel.TRAINED)
            new_character.set_skill_proficiency("Atletyka", ProficiencyLevel.TRAINED)
        elif new_character.get_class().class_name() == "Czarodziej":
            new_character.get_saving_throw("Will").set_proficiency_level(ProficiencyLevel.TRAINED)
            new_character.set_skill_proficiency("Wiedza Tajemna", ProficiencyLevel.TRAINED)
        elif new_character.get_class().class_name() == "Łowca":
            new_character.get_saving_throw("Reflex").set_proficiency_level(ProficiencyLevel.TRAINED)
            new_character.set_skill_proficiency("Przetrwanie", ProficiencyLevel.TRAINED)


    print("\nDodaję przykładowy ekwipunek...")
    new_character.add_to_inventory(SimpleItem("Pochodnia", 0.3))
    new_character.add_to_inventory(SimpleItem("Racja Żywnościowa", 0.2))
    backpack = EquipmentContainer("Plecak Podróżnika", 1.0, capacity_kg=10.0)
    backpack.add_item(SimpleItem("Lina (15m)", 0.5))
    new_character.add_to_inventory(backpack)


    print(f"\nPostać '{name}' została stworzona!")
    return new_character

def run_character_creator():

    current_character: Character | None = None
    filename = "character_data.json"

    while True:
        print("\n--- Menu Kreatora Postaci Pathfinder 2e ---")
        print("1. Stwórz nową postać")
        print("2. Wczytaj postać z pliku")
        if current_character:
            print("3. Wyświetl statystyki aktualnej postaci")
            print("4. Zapisz aktualną postać do pliku")
            print("5. Zmień poziom postaci")
            print("6. Zmień wyszkolenie umiejętności")
            print("7. Dodaj/Usuń przedmiot z ekwipunku")
        print("0. Wyjdź")

        choice = input("Wybierz opcję: ")

        if choice == '1':
            try:
                current_character = create_new_character_interactive()
            except CharacterCreationError as e:
                print(f"Błąd tworzenia postaci: {e.message}")
            except Exception as e:
                print(f"Wystąpił nieoczekiwany błąd podczas tworzenia postaci: {e}")
        elif choice == '2':
            current_character = load_character_from_file(filename)
        elif choice == '3' and current_character:
            current_character.display_stats()
        elif choice == '4' and current_character:
            save_character_to_file(current_character, filename)
        elif choice == '5' and current_character:
            try:
                new_level = int(input(f"Podaj nowy poziom dla {current_character.get_name()}: "))
                current_character.set_level(new_level)
            except ValueError:
                print("Nieprawidłowy poziom. Podaj liczbę całkowitą.")
            except CharacterCreationError as e:
                print(f"Błąd: {e.message}")
        elif choice == '6' and current_character:
            print("\nDostępne umiejętności:")
            for skill_name in current_character._skills.keys():
                print(f"- {skill_name}")
            skill_to_set = input("Podaj nazwę umiejętności do zmiany wyszkolenia: ")
            if skill_to_set in current_character._skills:
                print("Wybierz nowy poziom wyszkolenia:")
                for i, level_enum in enumerate(ProficiencyLevel):
                    print(f"{i+1}. {level_enum.value}")
                try:
                    level_choice = int(input("Wybierz numer poziomu: "))
                    if 1 <= level_choice <= len(ProficiencyLevel._member_map_):
                        new_prof_level = list(ProficiencyLevel)[level_choice - 1]
                        current_character.set_skill_proficiency(skill_to_set, new_prof_level)
                    else:
                        print("Nieprawidłowy wybór poziomu.")
                except ValueError:
                    print("Nieprawidłowy numer. Podaj liczbę całkowitą.")
                except CharacterCreationError as e:
                    print(f"Błąd: {e.message}")
            else:
                print("Nieprawidłowa nazwa umiejętności.")
        elif choice == '7' and current_character:
            print("\nZarządzanie ekwipunkiem:")
            print("1. Dodaj prosty przedmiot")
            print("2. Usuń przedmiot (tylko z głównego ekwipunku)")
            eq_choice = input("Wybierz opcję: ")
            if eq_choice == '1':
                item_name = input("Nazwa przedmiotu: ")
                try:
                    item_weight = float(input("Waga przedmiotu (kg): "))
                    item_desc = input("Opis (opcjonalnie): ")
                    new_item = SimpleItem(item_name, item_weight, item_desc)
                    current_character.add_to_inventory(new_item)
                except ValueError:
                    print("Nieprawidłowa waga.")
                except CharacterCreationError as e:
                    print(f"Błąd: {e.message}")
            elif eq_choice == '2':
                item_name = input("Nazwa przedmiotu do usunięcia: ")
                try:
                    current_character.remove_from_inventory(item_name)
                except CharacterCreationError as e:
                    print(f"Błąd: {e.message}")
            else:
                print("Nieprawidłowa opcja.")
        elif choice == '0':
            print("Dziękuję za skorzystanie z kreatora postaci!")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


if __name__ == "__main__":
    run_character_creator()