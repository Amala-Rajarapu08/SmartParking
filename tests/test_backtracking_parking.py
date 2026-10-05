from algorithms.backtracking_parking import find_parking_arrangement


def test_parking_arrangement():
    slots = [1, 2, 3]
    vehicles = ["AP39AB1234", "AP39CD5678"]

    result = find_parking_arrangement(slots, vehicles)

    assert result is not None
    assert len(result) == 2
    assert result[1] == "AP39AB1234"
    assert result[2] == "AP39CD5678"


def test_not_enough_slots():
    slots = [1]
    vehicles = ["AP39AB1234", "AP39CD5678"]

    result = find_parking_arrangement(slots, vehicles)

    assert result is None
