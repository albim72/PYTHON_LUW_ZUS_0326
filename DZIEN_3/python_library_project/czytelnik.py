#Klasy: Reader i Address

class Address:
    def __init__(self, city, street, postal_code):
        self.city = city
        self.street = street
        self.postal_code = postal_code

    def __str__(self):
        return f"{self.street}, {self.postal_code} {self.city}"

class Reader:
    def __init__(self, first_name, last_name, city, street, postal_code):
        self.first_name = first_name
        self.last_name = last_name

        # kompozycja – tworzymy adres wewnątrz klasy
        self.address = Address(city, street, postal_code)

    def __str__(self):
        return f"Reader: {self.first_name} {self.last_name}\nAddress: {self.address}"

reader = Reader(
    "Jan",
    "Kowalski",
    "Warszawa",
    "Marszałkowska 10",
    "00-001"
)

print(reader)
