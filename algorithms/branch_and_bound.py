def best_parking_revenue(revenues, capacity):
    """
    Branch and Bound algorithm.

    Finds the maximum possible parking revenue
    without exceeding the given capacity.
    """

    best = 0

    def branch(index, current_revenue):

        nonlocal best

        # If current revenue is better, update best
        if current_revenue > best:
            best = current_revenue

        # No more choices
        if index == len(revenues):
            return

        # Include current revenue
        if current_revenue + revenues[index] <= capacity:
            branch(index + 1, current_revenue + revenues[index])

        # Exclude current revenue
        branch(index + 1, current_revenue)

    branch(0, 0)

    return best


if __name__ == "__main__":

    parking_revenues = [20, 30, 40, 50]

    capacity = 70

    result = best_parking_revenue(parking_revenues, capacity)

    print("Best parking revenue:", result)
