#strumień zdarzeń z zawodów
from collections import namedtuple, defaultdict,Counter,deque
events = [
    (5,101,"overtake"),
    (7,102,"overtake"),
    (9,101,"gel"),
    (12,101,"overtake"),
    (14,102,"gel"),
    (16,101,"overtake"),
    (18,101,"overtake"),
    (21,102,"gel"),
]

"""
1 - policz kto najczęsciej wyprzedza
2 - śledź ostatnie 3 akcje każdego zawodnika
3 - zbuduj strukturę zawodnika (nametuple)
4 - wykryj agresywną fazę - 3 wyprzedzenia w krótkim czasie
"""

Runner = namedtuple("Runner",["bib","actions"])

#liczenie akcji
action_counter = Counter()
#historia ostatnich 3 akcji
recent_actions = defaultdict(lambda : deque(maxlen=3))

#przechowywanie wszytkich akcji
all_actions = defaultdict(list)

for minute, bib, action in events:
    action_counter[(bib,action)] += 1
    recent_actions[bib].append((minute,action))
    all_actions[bib].append((minute,action))

#kto najczęsciej wyprzedza
overtake_counts = {
    bib: count
    for (bib,action),count in action_counter.items()
    if action == "overtake"
}

print("Wyprzedzanie",overtake_counts)
