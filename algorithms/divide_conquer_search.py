def binary_search(slots, target):
    """
    Divide and Conquer algorithm using Binary Search.

    Searches for a target parking slot in a sorted list.
    """

    left = 0
    right = len(slots) - 1

    while left <= right:

        middle = (left + right) // 2

        if slots[middle] == target:
            return middle

        elif slots[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    return -1


if __name__ == "__main__":

    parking_slots = [1, 2, 3, 4, 5]

    target = 4

    result = binary_search(parking_slots, target)

    if result != -1:
        print("Parking slot found:", parking_slots[result])
    else:
        print("Parking slot not found")
