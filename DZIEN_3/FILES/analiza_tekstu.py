try:
    with open("shopping_list.txt", "r", encoding="UTF-8") as file:
        text = file.read()

        #liczba znaków
        char_count = len(text)

        #liczba słów
        words =text.split()
        word_count = len(words)

        #liczba linii
        lines = text.split("\n")
        line_count = len(lines)

    print("ANALIZA PLIKU TEKSTOWEGO")
    print("_"*70)
    print(f"Liczba linii: {line_count}")
    print(f"liczba słów: {word_count}")
    print(f"liczba znaków: {char_count}")

except FileNotFoundError:
    print("Nie znaleziono pliku")
except IOError:
    print("Błąd odczytu pliku")
