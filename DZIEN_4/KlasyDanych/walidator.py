from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int

    def __post_init__(self):
        if self.price<=10:
            raise ValueError("Price must be greater than 10")
        if self.quantity<1:
            raise ValueError("Quantity must be equal or greater than 1")

    def total_value(self):
        return self.price * self.quantity

p1 = Product("Apple Air", 8900, 2)

p2 = Product("Apple Pro", 10900, 1)

p3 = Product("Apple Mouse", 11, 1)

print(p1.total_value())
print(p2.total_value())
print(p3.total_value())
