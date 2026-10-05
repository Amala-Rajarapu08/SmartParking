from algorithms.branch_and_bound import best_parking_revenue


def test_best_parking_revenue():
    revenues = [20, 30, 40, 50]

    result = best_parking_revenue(revenues, 70)

    assert result == 70


def test_zero_capacity():
    revenues = [20, 30, 40]

    result = best_parking_revenue(revenues, 0)

    assert result == 0
