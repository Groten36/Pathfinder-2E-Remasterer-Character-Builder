# Pathfinder-2E-Remasterer-Character-Builder
UWAGA:
Ze względu na ostateczny termin oddania projektu jego pierwotna wiersja musiała uleć uproszczeniu (zrezygnowałam z np. czarów i cech).
Jednakże planuje go kontunuować, stąd postanowiłam pozostawiłam w nim domyślny rokład katalogów, nawet jeśli ze względu na to, że zawiera on 1 plik jest to mało optymalne.

1. Użycie klas
W aplikacji każdy aspekt postaci (statystyka, umiejętność, ekwipunek itp.) jest reprezentowany przez inną klasę.
2. Użycie dziedziczenia
W aplikacji wielokrotnie zostało użyte dziedziczenie np. klasy Fighter i Wizard dziedziczą po klasie CharacterClass
Użycie atrybutów w klasach; pokazanie nadpisywania atrybutów w klasach potomnych
3. Użycie metod w klasach; pokazanie nadpisywania metod w klasach potomnych
Klasa Ascestry posiada metodę apply_bonus (modyfikującą statystyki według wybranej rasy postaci), każda z jej klas potomnych implementuje ją w sposób w zależnośći od cech ras.
4. Użycie dekoratora @classmethod lub @staticmethod
Jednym z przykłądowych użyć @classmethod jest metoda create_base_character z klasy Character, a @staticmethod check_name_validity z tej samej klasy.
5. Klasa zawierająca więcej niż jeden konstruktor
Klasa Character posiada 2 konstruktory. __init__ i create_base_character
6. Użycie enkapsulacji (settery i gettery)
Większośc klas w projekcie takie posiada np. klasa Attribute
7. Polimorfizm
Przykładem polimorfizmu jest użycie metody o nazwie get_name w wielu klasach w projekcie (każda taka metoda działa trochę inaczej).
8. Użycie implementacji z klasy rodzica: super()
Podklasy klasy Attribute
9. Utworzenie i użycie swojego wyjątku (własna klasa dziedziąca z wbudowanej klasy Exception)
Wyjątek CharacterCreationError
10. Zastosowanie trzech wzorców projektowych
• Jeden wybrany z:
– Strategia (strategy)
– Polecenie (command)
– Metoda szablonowa (template method)
• Dwa dowolne
 Zastosowane zostały wzorce: Metoda szbalonowa, Dekorator, Fabryka abstrakcyjna i kompozyt.