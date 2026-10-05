from algorithms.divide_conquer_search import binary_search


def test_binary_search_found():
    slots = [1, 2, 3, 4, 5]

    result = binary_search(slots, 4)

    assert result == 3


def test_binary_search_not_found():
    slots = [1, 2, 3, 4, 5]

    result = binary_search(slots, 6)

    assert result == -1
