def find_parking_arrangement(slots, vehicles):
    """
    Backtracking algorithm.

    Tries to assign vehicles to parking slots.
    If a choice does not work, it goes back
    and tries another choice.
    """

    arrangement = {}

    def backtrack(vehicle_index):

        if vehicle_index == len(vehicles):
            return True

        vehicle = vehicles[vehicle_index]

        for slot in slots:

            if slot not in arrangement:

                arrangement[slot] = vehicle

                if backtrack(vehicle_index + 1):
                    return True

                # Undo the choice
                del arrangement[slot]

        return False

    if backtrack(0):
        return arrangement

    return None


if __name__ == "__main__":

    parking_slots = [1, 2, 3]
    vehicles = ["AP39AB1234", "AP39CD5678"]

    result = find_parking_arrangement(parking_slots, vehicles)

    print("Parking arrangement:", result)
