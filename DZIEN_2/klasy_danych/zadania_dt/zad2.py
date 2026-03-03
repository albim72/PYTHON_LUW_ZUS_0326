from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    model: str
    year: int
    price: float
    available: bool = True

    def __post_init__(self):
        # --- Walidacja tekstu ---
        if not self.brand.strip():
            raise ValueError("Brand cannot be empty")

        if not self.model.strip():
            raise ValueError("Model cannot be empty")

        # --- Walidacja roku ---
        if self.year < 1986:
            raise ValueError("Year must be >= 1986")

        # --- Walidacja ceny ---
        if self.price < 0:
            raise ValueError("Price cannot be negative")

    def apply_discount(self, percent: float):
        if not (0 < percent <= 40):
            raise ValueError("Discount percent must be between 0 and 40")

        discount_amount = self.price * (percent / 100)
        self.price -= discount_amount

    @property
    def is_new(self) -> bool:
        return self.year >= 2023

    def full_name(self) -> str:
        return f"{self.brand} {self.model} ({self.year})"


# --- Demo ---
if __name__ == "__main__":
    car = Car("BMW", "M3", 2022, 350000)

    print(car)
    car.apply_discount(10)
    print("After discount:", car.price)

    # Test błędu:
    bad = Car("BMW", "X5", 1998, 100000)
