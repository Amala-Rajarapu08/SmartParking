from datetime import datetime


class ParkingSystem:
    def __init__(self):
        self.slots = {1: None, 2: None, 3: None, 4: None, 5: None}
        self.entry_times = {}
        self.hourly_rate = 20

    def view_slots(self):
        print("\n--- Parking Slots ---")
        for slot, vehicle in self.slots.items():
            status = vehicle if vehicle else "Available"
            print(f"Slot {slot}: {status}")

    def park_vehicle(self, vehicle):
        vehicle = vehicle.strip().upper()

        if not vehicle:
            print("Vehicle number cannot be empty.")
            return

        if vehicle in self.entry_times:
            print("Vehicle is already parked.")
            return

        for slot, parked_vehicle in self.slots.items():
            if parked_vehicle is None:
                self.slots[slot] = vehicle
                self.entry_times[vehicle] = datetime.now()
                print(f"\nSuccess! Vehicle {vehicle} parked in Slot {slot}.")
                return

        print("Sorry, parking is full.")

    def remove_vehicle(self, vehicle):
        vehicle = vehicle.strip().upper()

        if vehicle not in self.entry_times:
            print("Vehicle not found.")
            return

        duration = datetime.now() - self.entry_times[vehicle]
        hours = max(1, int(duration.total_seconds() // 3600) + 1)
        fee = hours * self.hourly_rate

        for slot, parked_vehicle in self.slots.items():
            if parked_vehicle == vehicle:
                self.slots[slot] = None
                break

        del self.entry_times[vehicle]
        print(f"\nVehicle: {vehicle}")
        print(f"Parking duration: {hours} hour(s)")
        print(f"Parking fee: Rs. {fee}")

    def summary(self):
        occupied = sum(v is not None for v in self.slots.values())
        print("\n--- Parking Summary ---")
        print(f"Total slots: {len(self.slots)}")
        print(f"Occupied slots: {occupied}")
        print(f"Available slots: {len(self.slots) - occupied}")

    def run(self):
        while True:
            print("\n===== SMART PARKING MANAGEMENT SYSTEM =====")
            print("1. View parking slots")
            print("2. Park vehicle")
            print("3. Remove vehicle")
            print("4. Parking summary")
            print("5. Exit")

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
            else:
                print("Invalid choice. Please enter 1 to 5.")


if __name__ == "__main__":
    parking = ParkingSystem()
    parking.run()
