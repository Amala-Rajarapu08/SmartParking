from datetime import datetime
from functools import wraps
from threading import Thread, Lock
from time import perf_counter
from typing import Callable, Iterator, Optional


# Pure function: calculates parking fee
def calculate_fee(duration_hours: float, hourly_rate: int) -> int:
    hours = max(1, int(duration_hours) + 1)
    return hours * hourly_rate


# Decorator: measures execution time
def measure_time(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - start
        print(f"[Execution time: {elapsed:.6f} seconds]")
        return result

    return wrapper


class ParkingSystem:
    def __init__(self) -> None:
        self.slots: dict[int, Optional[str]] = {i: None for i in range(1, 6)}
        self.entry_times: dict[str, datetime] = {}
        self.hourly_rate: int = 20
        self.lock = Lock()

    # Generator: yields available slots
    def available_slots(self) -> Iterator[int]:
        for slot, vehicle in self.slots.items():
            if vehicle is None:
                yield slot

    def view_slots(self) -> None:
        print("\n--- Parking Slots ---")
        statuses = {
            slot: vehicle if vehicle else "Available"
            for slot, vehicle in self.slots.items()
        }

        for slot, status in statuses.items():
            print(f"Slot {slot}: {status}")

    @measure_time
    def park_vehicle(self, vehicle: str) -> None:
        vehicle = vehicle.strip().upper()

        if not vehicle:
            print("Vehicle number cannot be empty.")
            return

        with self.lock:
            if vehicle in self.entry_times:
                print("Vehicle is already parked.")
                return

            slot = next(self.available_slots(), None)

            if slot is None:
                print("Sorry, parking is full.")
                return

            self.slots[slot] = vehicle
            self.entry_times[vehicle] = datetime.now()
            print(f"\nSuccess! Vehicle {vehicle} parked in Slot {slot}.")

    @measure_time
    def remove_vehicle(self, vehicle: str) -> None:
        vehicle = vehicle.strip().upper()

        with self.lock:
            if vehicle not in self.entry_times:
                print("Vehicle not found.")
                return

            duration = datetime.now() - self.entry_times[vehicle]
            hours = max(1, int(duration.total_seconds() // 3600) + 1)
            fee = calculate_fee(hours - 1, self.hourly_rate)

            for slot, parked_vehicle in self.slots.items():
                if parked_vehicle == vehicle:
                    self.slots[slot] = None
                    break

            del self.entry_times[vehicle]

        print(f"\nVehicle: {vehicle}")
        print(f"Parking duration: {hours} hour(s)")
        print(f"Parking fee: Rs. {fee}")

    def summary(self) -> None:
        with self.lock:
            occupied = sum(vehicle is not None for vehicle in self.slots.values())
            total = len(self.slots)

        print("\n--- Parking Summary ---")
        print(f"Total slots: {total}")
        print(f"Occupied slots: {occupied}")
        print(f"Available slots: {total - occupied}")

    # Threading example
    def background_report(self) -> None:
        report_thread = Thread(target=self.summary)
        report_thread.start()
        report_thread.join()

    # Performance evaluation
    def performance_test(self) -> None:
        iterations = 1000
        start = perf_counter()

        for _ in range(iterations):
            next(self.available_slots(), None)

        end = perf_counter()
        total_time = end - start
        average_time = total_time / iterations

        print("\n--- Performance Evaluation ---")
        print(f"Operations: {iterations}")
        print(f"Total time: {total_time:.6f} seconds")
        print(f"Average time: {average_time:.8f} seconds")
        print("Algorithm: Available-slot search")
        print("Time complexity: O(n), where n is the number of slots")

    def run(self) -> None:
        while True:
            print("\n===== SMART PARKING MANAGEMENT SYSTEM =====")
            print("1. View parking slots")
            print("2. Park vehicle")
            print("3. Remove vehicle")
            print("4. Parking summary")
            print("5. Exit")
            print("6. Background summary report")
            print("7. Performance evaluation")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.view_slots()
            elif choice == "2":
                vehicle = input("Enter vehicle number: ")
                self.park_vehicle(vehicle)
            elif choice == "3":
                vehicle = input("Enter vehicle number to remove: ")
                self.remove_vehicle(vehicle)
            elif choice == "4":
                self.summary()
            elif choice == "5":
                print("Thank you for using Smart Parking Management System!")
                break
            elif choice == "6":
                self.background_report()
            elif choice == "7":
                self.performance_test()
            else:
                print("Invalid choice. Please enter 1 to 7.")


if __name__ == "__main__":
    parking = ParkingSystem()
    parking.run()
