import time

from greedy_parking import find_first_available_slot
from divide_conquer_search import binary_search
from dynamic_programming import maximum_parking_revenue
from backtracking_parking import find_parking_arrangement
from branch_and_bound import best_parking_revenue


def measure_time(function, *args):
    start = time.perf_counter()

    function(*args)

    end = time.perf_counter()

    return end - start


if __name__ == "__main__":

    # Greedy
    parking_slots = {
        1: "AP39AB1234",
        2: None,
        3: "AP39CD5678",
        4: None,
        5: None,
    }

    greedy_time = measure_time(find_first_available_slot, parking_slots)

    # Divide and Conquer
    slots = list(range(1, 1001))

    divide_time = measure_time(binary_search, slots, 750)

    # Dynamic Programming
    revenues = [20, 30, 40, 50]

    dp_time = measure_time(maximum_parking_revenue, revenues, 70)

    # Backtracking
    backtracking_slots = [1, 2, 3, 4]
    vehicles = ["AP39AB1234", "AP39CD5678"]

    backtracking_time = measure_time(
        find_parking_arrangement, backtracking_slots, vehicles
    )

    # Branch and Bound
    revenues = [20, 30, 40, 50]

    branch_bound_time = measure_time(best_parking_revenue, revenues, 70)

    print("\n===== PERFORMANCE EVALUATION =====")

    print(f"Greedy:              {greedy_time:.8f} seconds")
    print(f"Divide & Conquer:    {divide_time:.8f} seconds")
    print(f"Dynamic Programming: {dp_time:.8f} seconds")
    print(f"Backtracking:        {backtracking_time:.8f} seconds")
    print(f"Branch & Bound:      {branch_bound_time:.8f} seconds")
