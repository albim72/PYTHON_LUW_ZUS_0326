from typing import get_type_hints
from functools import wraps


class RequireRunMeta(type):
    def __new__(cls, name, bases, attrs):
        if "run" not in attrs:
            raise TypeError("Class must have a run() method")

        run_method = attrs["run"]
        annotations = get_type_hints(run_method)

        # Walidacja deklaracji typu (statyczna)
        if "return" not in annotations:
            raise TypeError("run() method must declare return type")
        if annotations["return"] not in (int, float):
            raise TypeError("run() method must return int or float")

        # Walidacja wartości zwracanej (runtime)
        @wraps(run_method)
        def wrapped_run(self, *args, **kwargs):
            result = run_method(self, *args, **kwargs)
            if not isinstance(result, (int, float)):
                raise TypeError(
                    f"run() returned {type(result).__name__}, expected int or float"
                )
            return result

        attrs["run"] = wrapped_run
        return super().__new__(cls, name, bases, attrs)


class Worker(metaclass=RequireRunMeta):
    def run(self) -> float:
        print("Running worker")
        return 2.0


w = Worker()
print(w.run())
