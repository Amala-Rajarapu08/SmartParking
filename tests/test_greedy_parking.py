from algorithms.greedy_parking import find_first_available_slot


def test_first_available_slot():
    parking_slots = {1: "AP39AB1234", 2: None, 3: "AP39CD5678", 4: None, 5: None}

    result = find_first_available_slot(parking_slots)

    assert result == 2


def test_no_available_slot():
    parking_slots = {
        1: "AP39AB1234",
        2: "AP39CD5678",
        3: "AP39EF1111",
        4: "AP39GH2222",
        5: "AP39IJ3333",
    }

    result = find_first_available_slot(parking_slots)

    assert result is None
