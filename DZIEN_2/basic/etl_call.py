from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Callable, Iterable, Iterator, List, Dict
import time


Step = Callable[[Iterable[Any]], Iterable[Any]]


@dataclass
class StreamPipeline:
    """
    Pipeline do przetwarzania strumieniowego.
    - instancja jest wywoływalna dzięki __call__
    - trzyma kroki transformacji
    - zbiera statystyki (ile elementów weszło/wyszło, czas)
    """

    steps: List[Step] = field(default_factory=list)
    stats: Dict[str, Any] = field(default_factory=lambda: {
        "runs": 0,
        "last_time_s": 0.0,
        "last_in": 0,
        "last_out": 0,
    })

    def add(self, step: Step) -> "StreamPipeline":
        """Dodaj krok i zwróć self, żeby dało się łańcuchować."""
        self.steps.append(step)
        return self

    def __call__(self, data: Iterable[Any]) -> Iterator[Any]:
        """
        Uruchamia pipeline na wejściu data i zwraca iterator wyników.
        Klucz: nie materializujemy wyników (strumień).
        """
        self.stats["runs"] += 1
        start = time.perf_counter()

        # Liczymy wejście "w locie" (bez robienia listy)
        def count_in(it: Iterable[Any]) -> Iterator[Any]:
            n = 0
            for x in it:
                n += 1
                yield x
            self.stats["last_in"] = n

        # Liczymy wyjście "w locie"
        def count_out(it: Iterable[Any]) -> Iterator[Any]:
            n = 0
            for x in it:
                n += 1
                yield x
            self.stats["last_out"] = n

        stream: Iterable[Any] = count_in(data)

        # Przepuszczamy przez kolejne kroki
        for step in self.steps:
            stream = step(stream)

        # Ostatni krok: policz ile wyszło
        stream = count_out(stream)

        # Aktualizujemy czas po pełnym skonsumowaniu strumienia:
        # UWAGA: czas zaktualizuje się dopiero, gdy ktoś przeiteruje wyniki.
        def finalize(it: Iterable[Any]) -> Iterator[Any]:
            yield from it
            self.stats["last_time_s"] = time.perf_counter() - start

        return finalize(stream)


# --- Kroki pipeline ---
def parse_int(lines: Iterable[str]) -> Iterator[int]:
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            yield int(line)
        except ValueError:
            continue


def only_even(nums: Iterable[int]) -> Iterator[int]:
    for n in nums:
        if n % 2 == 0:
            yield n


def scale(factor: int) -> Step:
    """Fabryka kroku: domknięcie."""
    def step(nums: Iterable[int]) -> Iterator[int]:
        for n in nums:
            yield n * factor
    return step


# --- Demo ---
if __name__ == "__main__":
    raw = ["1", "2", "x", "4", "", "10", "11", "12"]

    pipe = (
        StreamPipeline()
        .add(parse_int)
        .add(only_even)
        .add(scale(10))
    )

    # __call__ => obiekt zachowuje się jak funkcja
    out = list(pipe(raw))
    print("OUTPUT:", out)            # [20, 40, 100, 120]
    print("STATS:", pipe.stats)      # runs, last_in, last_out, last_time_s
