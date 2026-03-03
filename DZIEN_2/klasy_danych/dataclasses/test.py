from dataclasses import dataclass

@dataclass
class Car:
    mark: str
    model: str
    engine: str
    power:int

    def __init__(self, mark, model, year, power, distance=0):
        self.mark = mark
        self.model = model
        self.year = year
        self.power = power
        self.distance = distance



C = Car("BMW", "M3", "1.6", 160)

print(C)
