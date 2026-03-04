import json

try:
    with open("student.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Normalize to a list of student dictionaries
    if isinstance(data, dict):
        students = [data]
    elif isinstance(data, list):
        students = data
    else:
        raise ValueError("Niepoprawna struktura JSON: oczekiwano obiektu lub listy obiektów.")

    print("Lista studentów:\n")
    for i, s in enumerate(students, start=1):
        if not isinstance(s, dict):
            raise ValueError(f"Element #{i} nie jest obiektem JSON.")

        required_keys = ("name", "surname", "points")
        missing = [k for k in required_keys if k not in s]
        if missing:
            raise ValueError(f"Brakuje pól {missing} w elemencie #{i}.")

        name = s["name"]
        surname = s["surname"]
        points = s["points"]
        print(f"Student: {name} {surname} -> punkty: {points}")

except FileNotFoundError:
    print("Nie znaleziono pliku")
except json.JSONDecodeError:
    print("Niepoprawny format pliku JSON")
except ValueError as e:
    print(f"Błąd danych: {e}")
