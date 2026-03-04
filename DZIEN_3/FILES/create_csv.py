import csv

students = [
    ["Imię","Nazwisko","Punkty"],
    ["Anna","Nowak",85],
    ["Piotr","Kot",86],
    ["Olga","Kowal",56],
    ["Robert","Nowik",78],
    ["Kinga","Rupek",95],
]

try:
    with open('students.csv', 'w', newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        for row in students:
            writer.writerow(row)

    print("plik csv został utworzony")
except IOError:
    print("Bład zapisu do pliku")
