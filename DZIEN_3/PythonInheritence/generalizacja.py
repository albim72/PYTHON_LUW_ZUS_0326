class Animal:
    def __init__(self,name: str):
        self.name = name

    def speak(self) -> str:
        return f"(Silence)"

class Dog(Animal):
    def speak(self) -> str:
        return f"Chau chau!"

a = Animal("stworzenie..")
d = Dog("Ludvik")

print(a.name, a.speak())
print(d.name, d.speak())
