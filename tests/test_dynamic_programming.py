from algorithms.dynamic_programming import maximum_parking_revenue


def test_maximum_parking_revenue():
    revenues = [20, 30, 40, 50]

    result = maximum_parking_revenue(revenues, 70)

    assert result == 70


def test_zero_capacity():
    revenues = [20, 30, 40]

    result = maximum_parking_revenue(revenues, 0)

    assert result == 0
