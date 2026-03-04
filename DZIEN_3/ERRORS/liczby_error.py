try:
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    result = a / b

except ZeroDivisionError:
    print("Błąd: Nie dziel przez zero!")

except ValueError:
    print("Podałeś coś co nie jest liczbą...")

else:
    print(result)
finally:
    print("co dalej?")

