shopping_list = ["mleko","chleb","ser","jajka","parówki","sok malinowy","mozarella"]

try:
    with open("shopping_list.txt", "w", encoding="utf-8") as file:
        for item  in shopping_list:
            file.write(item + "\n")
    print("Zapisano do pliku")
except IOError:
    print("Błąd zapisu do pliku....")
