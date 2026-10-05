from typing import Iterator, Callable, TypeVar, Optional
from contextlib import contextmanager
from time import perf_counter

T = TypeVar("T")


# 1. Iterator example
class ParkingSlotIterator:
    def __init__(self, slots: list[int]) -> None:
        self.slots = slots
        self.index = 0

    def __iter__(self) -> "ParkingSlotIterator":
        return self

    def __next__(self) -> int:
        if self.index >= len(self.slots):
            raise StopIteration

        slot = self.slots[self.index]
        self.index += 1
        return slot


# 2. Generator example
def available_slot_generator(slots: dict[int, Optional[str]]) -> Iterator[int]:
    for slot, vehicle in slots.items():
        if vehicle is None:
            yield slot


# 3. Generic function example
def first_item(items: list[T]) -> Optional[T]:
    return items[0] if items else None


# 4. Higher-order function example
def apply_discount(price: float, discount_function: Callable[[float], float]) -> float:
    return discount_function(price)


def ten_percent_discount(price: float) -> float:
    return price * 0.90


# 5. Context manager example
@contextmanager
def performance_timer():
    start = perf_counter()
    try:
        yield
    finally:
        elapsed = perf_counter() - start
        print(f"Execution time: {elapsed:.6f} seconds")


# 6. List comprehension example
def occupied_slots(slots: dict[int, Optional[str]]) -> list[int]:
    return [slot for slot, vehicle in slots.items() if vehicle is not None]


# Demonstration
if __name__ == "__main__":
    print("--- Advanced Python Features ---")

    slots = {1: "AP1234", 2: None, 3: "TS5678", 4: None}

    print("\nIterator:")
    for slot in ParkingSlotIterator([1, 2, 3]):
        print(slot)

    print("\nGenerator:")
    print(list(available_slot_generator(slots)))

    print("\nGeneric function:")
    print(first_item(["AP1234", "TS5678"]))

    print("\nHigher-order function:")
    print(apply_discount(100, ten_percent_discount))

    print("\nList comprehension:")
    print(occupied_slots(slots))

    print("\nContext manager:")
    with performance_timer():
        sum(range(10000))
