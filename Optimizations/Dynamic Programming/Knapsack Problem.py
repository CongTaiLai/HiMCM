def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])  # max of up and
            else:
                dp[i][w] = dp[i - 1][w]  # up

    return dp[n][capacity]


weights = [2, 2, 3, 5, 1]
values = [5, 20, 20, 15, 5]
capacity = 10
result = knapsack(weights, values, capacity)
print("Maximum value:", result)
