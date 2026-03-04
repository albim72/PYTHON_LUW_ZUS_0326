import logging


class AppError(Exception):
    """Baza dla wyjątków aplikacji."""
    pass


class InvalidFuelAmountError(AppError):
    """Gdy ilość paliwa (w litrach) jest <= 0."""
    pass


class TankOverflowError(AppError):
    """Gdy próbujemy zatankować więcej niż wolne miejsce w baku."""
    pass


class InvalidCommandError(AppError):
    """Gdy komenda ma zły format (np. 'pln' bez kwoty)."""
    pass


def setup_logging():
    logging.basicConfig(
        filename="fuel_app.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )
    logging.info("=== START APLIKACJI ===")


def parse_command(raw: str, price_per_liter: float) -> float:
    """
    Zwraca liczbę litrów do zatankowania na podstawie wpisu użytkownika.

    Obsługiwane formaty:
    - "10.5"        -> 10.5 litra
    - "pln 100"     -> (100 / cena) litrów

    Rzuca:
    - InvalidCommandError (format)
    - ValueError (gdy nie da się sparsować liczby)
    """
    raw = raw.strip()
    if not raw:
        raise InvalidCommandError(
            "Pusty input. Podaj liczbę litrów lub 'pln <kwota>' albo 'exit'."
        )

    parts = raw.split()

    # tryb "pln <kwota>"
    if parts[0].lower() == "pln":
        if len(parts) != 2:
            raise InvalidCommandError("Format: 'pln <kwota>', np. 'pln 100'.")

        try:
            amount_pln = float(parts[1])
        except ValueError as e:
            # ŁAŃCUCH WYJĄTKÓW: zachowujemy oryginalną przyczynę (np. "abc")
            raise InvalidCommandError("Kwota po 'pln' musi być liczbą, np. 'pln 100'.") from e

        return amount_pln / price_per_liter

    # tryb "liczba litrów"
    if len(parts) == 1:
        try:
            return float(parts[0])
        except ValueError as e:
            raise InvalidCommandError("Podaj liczbę litrów, np. '10.5'.") from e

    raise InvalidCommandError("Nieznany format. Podaj np. '12.5' albo 'pln 100' albo 'exit'.")


def main():
    setup_logging()

    capacity = 50.0
    fuel = 12.5
    price_per_liter = 6.49

    print("=== STACJA PALIW (PREMIUM) ===")
    print("Komendy:")
    print("  - litry:       10.5")
    print("  - za kwotę:    pln 100")
    print("  - zakończ:     exit\n")

    while True:
        free_space = capacity - fuel

        print(f"\nPojemność baku: {capacity:.1f} L")
        print(f"Aktualny stan:  {fuel:.1f} L")
        print(f"Wolne miejsce:  {free_space:.1f} L")
        print(f"Cena paliwa:    {price_per_liter:.2f} PLN/L")

        raw = input("\nIle tankujesz? ").strip()

        if raw.lower() == "exit":
            print("Koniec. Szerokiej drogi!")
            logging.info("Zakończono program komendą exit.")
            break

        liters = None

        try:
            liters = parse_command(raw, price_per_liter)

            if liters <= 0:
                raise InvalidFuelAmountError("Ilość paliwa musi być większa od zera.")

            if liters > free_space:
                raise TankOverflowError(
                    f"Za dużo paliwa. Maksymalnie możesz dolać: {free_space:.2f} L."
                )

        except AppError as e:
            # Obsługa wszystkich naszych błędów aplikacji
            print("Błąd:", e)
            logging.warning("Błąd aplikacji dla input='%s': %s", raw, e, exc_info=True)

        else:
            fuel += liters
            cost = liters * price_per_liter

            print("\nTankowanie zakończone")
            print(f"Zatankowano:    {liters:.2f} L")
            print(f"Koszt:          {cost:.2f} PLN")
            print(f"Nowy stan baku: {fuel:.2f} L")

            logging.info(
                "Tankowanie OK | input='%s' | liters=%.4f | cost=%.2f | new_fuel=%.4f",
                raw, liters, cost, fuel
            )

        finally:
            print("Operacja zakończona.")
            logging.info("Operacja zakończona dla input='%s'.", raw)


if __name__ == "__main__":
    main()
