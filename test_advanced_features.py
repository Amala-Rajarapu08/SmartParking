from advanced_features import (
    ParkingSlotIterator,
    available_slot_generator,
    first_item,
    apply_discount,
    ten_percent_discount,
    occupied_slots,
    performance_timer,
)


def test_iterator():
    iterator = ParkingSlotIterator([1, 2, 3])
    assert list(iterator) == [1, 2, 3]


def test_generator():
    slots = {1: "AP1234", 2: None, 3: "TS5678", 4: None}
    assert list(available_slot_generator(slots)) == [2, 4]


def test_generic_function():
    assert first_item(["AP1234", "TS5678"]) == "AP1234"


def test_generic_function_empty_list():
    assert first_item([]) is None


def test_higher_order_function():
    result = apply_discount(100, ten_percent_discount)
    assert result == 90.0


def test_occupied_slots():
    slots = {1: "AP1234", 2: None, 3: "TS5678"}
    assert occupied_slots(slots) == [1, 3]


def test_performance_timer(capsys):
    with performance_timer():
        sum(range(100))

    output = capsys.readouterr().out
    assert "Execution time:" in output
