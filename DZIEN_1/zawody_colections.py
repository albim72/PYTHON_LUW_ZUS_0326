from collections import defaultdict, Counter

nb = [5,3,6,9,35,9,36,90] #lista
tpnb = (73,78,244,2,56) #krotka
drzewa = {"dąb","sosna","buk","jodła"} #zbiór
slownik = {"imię":"Leon","nazwisko":"Kot","wiek":45}

#dane z punktów kontrolnych zawodów biegowych -> (numer_startowy, punkt, czas_minuty)

checkpoints = [
    (101,"Start",0),
    (102,"Start",0),
    (103,"Start",0),
    (104,"Start",0),
    (101,"Kościeliska",56),
    (102,"Kościeliska",67),
    (103,"Kościeliska",69),
    (104,"Kościeliska",23),
    (101,"Ornak",230),
    (102,"Ornak",267),
    (103,"Ornak",366),
    (104,"Ornak",88),
    (101,"Meta",428),
    (102,"Meta",546),
    (104,"Meta",145),
]

#grupowanie danych
runners = defaultdict(list)
for bib, point, time in checkpoints:
    runners[bib].append((point, time))

print(runners)

print("_"*70)
print("czas końcowy")

final_times = {
    bib: data[-1][1]
    for bib, data in runners.items()
}

#ranking
ranking = sorted(final_times.items(), key=lambda x: x[1])
print(ranking)

#analiza unikalnych punktów
points = {point for _, point, _ in checkpoints}
print(points)

#kto ile razy był notowany
bib_counts = Counter(bib for bib, _, _ in checkpoints)
print(bib_counts)

#wykrywanie zbyt szybkiego tempa...

# for bib, data in runners.items():
#     times = [t for _, t in data]
#     # print(f"bib: {bib} - {times}")
#     if len(times) > 1:
#         avg_time_point = times[-1] / (len(times) - 1)
#         if avg_time_point < 60:
#             print(f"podejrzany wynik: {bib}")

DIST_KM = 45
SUSP_KMH = 15

for bib, data in runners.items():
    data_sorted = sorted(data, key=lambda x: x[1])

    start_times = [t for point, t in data_sorted if point == "Start"]
    meta_times = [t for point, t in data_sorted if point == "Meta"]

    if not start_times or not meta_times:
        continue

    start_time = start_times[0]
    meta_time = meta_times[-1]

    total_min = meta_time - start_time

    if total_min <= 0:
        continue

    total_h = total_min / 60.0
    avg_kmh = DIST_KM/total_h

    if avg_kmh > SUSP_KMH:
        print(f"podejrzany wynik: {bib} | {avg_kmh:.2f}km/h "
              f"| {total_min}min | {total_h:.2f}h")
