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

#ex2 - funkcja jako argument
#system punktacji

def score_by_time(time):
    return max(0,500-time)

def score_by_consistancy(time):
    return 1000/(1+time)

def evaluate(time, scoring_strategy):
    return scoring_strategy(time)

print(evaluate(100, score_by_time))
print(evaluate(300, score_by_consistancy))
