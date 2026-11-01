# 0/1 Knapsack using Dynamic Programming

def knapsack(weights, values, capacity):
    n = len(weights)

    # Create DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Find selected items
    selected_items = []
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i)
            w -= weights[i - 1]

    selected_items.reverse()

    # Display selected items
    print("\nSelected Items:")
    for item in selected_items:
        print(f"Item {item}: Weight = {weights[item - 1]}, Value = {values[item - 1]}")

    print("\nMaximum value in Knapsack:", dp[n][capacity])


# Main Program
n = int(input("Enter number of items: "))

weights = []
values = []

for i in range(n):
    w = int(input(f"Enter weight of item {i+1}: "))
    v = int(input(f"Enter value of item {i+1}: "))

    weights.append(w)
    values.append(v)

capacity = int(input("Enter knapsack capacity: "))

if n <= 0 or capacity < 0 or any(w <= 0 for w in weights) or any(v < 0 for v in values):
    print("Invalid input!")
else:
    knapsack(weights, values, capacity)