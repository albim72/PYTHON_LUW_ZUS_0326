# Zadanie: Lista zakupów
# Cel: podstawowe operacje na kolekcji typu lista

# 1. Tworzymy listę zakupów
shopping_list = ["chleb", "masło", "mleko"]

# 2. Wypisujemy całą listę
print("Lista zakupów:")
print(shopping_list)

# 3. Wypisujemy każdy produkt osobno
print("\nProdukty:")

for product in shopping_list:
    print(product)

# 4. Dodajemy nowy produkt do listy
shopping_list.append("jajka")

# 5. Wypisujemy nową listę
print("\nNowa lista zakupów:")
print(shopping_list)

# 6. Wypisujemy liczbę produktów na liście
print("\nLiczba produktów:")
print(len(shopping_list))
