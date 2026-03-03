class Person:

    def __init__(self, name, age):
        self.name = name
        setattr(self, "_age", None) #ustawieni get/set przez builtins
        self.set_age(age) #walidacja przez setter

    def get_age(self):
        return getattr(self, "_age")

    def set_age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        setattr(self, "_age", value)

p = Person("Marcin",50)
print(p.get_age())
p.set_age(53)
print(p.get_age())

#dynamiczny dostęp do atrybutów
attr_name =  "_age"
print(getattr(p, attr_name))

setattr(p, attr_name, 55)
print(getattr(p, attr_name))

#sprawdzenie pola
if hasattr(p, "_age"):
    print("Atrybut istnieje!")
delattr(p, "_age")

print(hasattr(p, "_age"))

print(p.__getattribute__("name"))
