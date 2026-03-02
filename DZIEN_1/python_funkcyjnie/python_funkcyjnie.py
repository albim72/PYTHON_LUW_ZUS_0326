#programowanie funkcyjne
#ex1 - funkcja jako obiekt
#tryby silnika samochodu

def eco_mode(speed):
    return speed * 0.8

def sport_mode(speed):
    return speed * 1.2

mode = eco_mode

print(mode(100))
print(type(mode))

mode = sport_mode
print(mode(100))
print(type(mode))
