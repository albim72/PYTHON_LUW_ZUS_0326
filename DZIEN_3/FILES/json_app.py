import json

studentX = {
    "name":"Olaf",
    "surname":"Kot",
    "points":45,
    "city":"Kraków"
}

try:
    with open("student.json", "r", encoding="utf-8") as f:
        stds = json.load(f)
    stds.append(studentX)
    with open("student.json", "w", encoding="utf-8") as f:
        json.dump(stds, f, indent=4, ensure_ascii=False)
    print("student dodany")


except IOError as e:
    print(e)
