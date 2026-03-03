from collections import defaultdict
from typing import Iterable, Iterator


def source_lines() -> Iterator[str]:
    """Źródło danych: generator linii (tu sztuczne, w realu może być plik/socket/API)."""
    yield "2026-03-03T10:00:00|u1|view|0"
    yield "2026-03-03T10:00:02|u2|purchase|120"
    yield "2026-03-03T10:00:03|u1|purchase|30"
    yield "2026-03-03T10:00:05|u3|purchase|200"
    yield "2026-03-03T10:00:06|u2|view|0"
    yield "2026-03-03T10:00:07|u2|purchase|50"
    yield "2026-03-03T10:00:08|BAD|LINE"
    yield "2026-03-03T10:00:09|u1|purchase|70"


def parse(lines: Iterable[str]) -> Iterator[dict]:
    """Krok 1: parsowanie. Pomijamy błędne linie."""
    for line in lines:
        parts = line.strip().split("|")
        if len(parts) != 4:
            continue  # zła linia, lecimy dalej
        ts, user_id, event, value_str = parts
        try:
            value = float(value_str)
        except ValueError:
            continue

        yield {"ts": ts, "user_id": user_id, "event": event, "value": value}


def only_event(records: Iterable[dict], event_name: str) -> Iterator[dict]:
    """Krok 2: filtr tylko dla wybranego eventu."""
    for r in records:
        if r["event"] == event_name:
            yield r


def with_tax(records: Iterable[dict], vat_rate: float = 0.23) -> Iterator[dict]:
    """Krok 3: mapowanie. Dodajemy wartość brutto."""
    for r in records:
        gross = r["value"] * (1 + vat_rate)
        yield {**r, "gross": gross}


def sum_gross_by_user(records: Iterable[dict]) -> dict:
    """Krok 4: agregacja (tu kończymy strumień i robimy wynik)."""
    totals = defaultdict(float)
    for r in records:
        totals[r["user_id"]] += r["gross"]
    return dict(totals)


def pipe(data: Iterable, *steps):
    """Prosty pipeline: kolejne kroki dostają iterable i zwracają iterable."""
    out = data
    for step in steps:
        out = step(out)
    return out


if __name__ == "__main__":
    stream = pipe(
        source_lines(),
        parse,
        lambda it: only_event(it, "purchase"),
        lambda it: with_tax(it, vat_rate=0.23),
    )

    totals = sum_gross_by_user(stream)

    # TOP 3 userów po wartości brutto
    top = sorted(totals.items(), key=lambda x: x[1], reverse=True)[:3]
    print("TOP users:", top)
