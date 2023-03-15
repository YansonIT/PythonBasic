from abc import ABC, abstractmethod


class BaseCounter(ABC):
    def __init__(self, start: int = 0, min_val: int = 0, max_val: int = 0):
        self._value = start
        self._min_val = min_val
        self._max_val = max_val

class Counter(BaseCounter):
    def __init__(self, start: int = 0, min_val: int = 0, max_val: int = 0):
        if start < min_val:
            start = min_val
        if start > max_val:
            start = max_val
        super().__init__(start, min_val, max_val)

    def set_min_value(self, min_val: int):
        self._min_val = min_val

    def set_max_value(self, max_val: int):
        self._max_val = max_val

    def set_start_value(self, start: int):
        self._value = start

    def increment(self):
        if self._value == self._max_val:
            self._value = self._min_val
        else:
            self._value += 1

    def current(self) -> int:
        return self._value

    def get_current_value(self):
        return self.current()

erste = Counter(3, 0, 10)
print(erste.current())
erste.increment()
print(erste.current())
erste.set_start_value(90)
print(erste.current())
print(erste.get_current_value())
