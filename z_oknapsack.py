# 0/1 Knapsack Problem
# Bottom-Up and Top-Down Approaches


# Bottom Up Approach (Tabulation or Iteration)

def knapsack_bottom_up(weights, profits, W):

    n = len(weights)

    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):

        for w in range(1, W + 1):

            if weights[i - 1] <= w:

                take = profits[i - 1] + dp[i - 1][w - weights[i - 1]]
                not_take = dp[i - 1][w]

                dp[i][w] = max(take, not_take)

            else:

                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


# Top Down Approach 

def knapsack_top_down(weights, profits, W):

    n = len(weights)

    dp = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]

    def solve(i, w):

        if i == 0 or w == 0:
            return 0

        if dp[i][w] != -1:
            return dp[i][w]

        if weights[i - 1] > w:

            dp[i][w] = solve(i - 1, w)

        else:

            take = profits[i - 1] + solve(i - 1, w - weights[i - 1])
            not_take = solve(i - 1, w)

            dp[i][w] = max(take, not_take)

        return dp[i][w]

    return solve(n, W)


# Main Program 

n = int(input("Enter number of items: "))
W = int(input("Enter capacity: "))

profits = list(map(int, input("Enter profits: ").split()))
weights = list(map(int, input("Enter weights: ").split()))

result1 = knapsack_bottom_up(weights, profits, W)
result2 = knapsack_top_down(weights, profits, W)

print("Maximum profit using Bottom-Up:", result1)
print("Maximum profit using Top-Down:", result2)