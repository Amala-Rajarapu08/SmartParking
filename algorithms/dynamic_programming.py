def maximum_parking_revenue(revenues, capacity):
    """
    Dynamic Programming algorithm.

    Finds the maximum revenue that can be obtained
    without exceeding the given parking capacity.
    """

    dp = [0] * (capacity + 1)

    for revenue in revenues:

        for current_capacity in range(capacity, 0, -1):

            if revenue <= current_capacity:
                dp[current_capacity] = max(
                    dp[current_capacity], dp[current_capacity - revenue] + revenue
                )

    return dp[capacity]


if __name__ == "__main__":

    parking_revenues = [20, 30, 40, 50]

    capacity = 70

    result = maximum_parking_revenue(parking_revenues, capacity)

    print("Maximum parking revenue:", result)
