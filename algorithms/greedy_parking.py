def find_first_available_slot(parking_slots):
    """
    Greedy algorithm for parking slot allocation.

    Selects the first available parking slot.
    """

    for slot, vehicle in parking_slots.items():

        if vehicle is None:
            return slot

    return None


if __name__ == "__main__":

    parking_slots = {1: "AP39AB1234", 2: None, 3: "AP39CD5678", 4: None, 5: None}

    slot = find_first_available_slot(parking_slots)

    if slot is not None:
        print("First available slot:", slot)
    else:
        print("No parking slot available")
