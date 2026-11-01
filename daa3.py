
# DAA: Fractional Knapsack using Greedy Method

def knapsack(weights, values, capacity):

    items = []
    step_count = 0

    # Calculate value/weight ratio
    for i in range(len(weights)):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i], i + 1))

    # Sort items by ratio in descending order
    items.sort(key=lambda x: x[0], reverse=True)

    total_value = 0

    print("\nSelected Items:")

    # Select items according to highest ratio
    for ratio, weight, value, item_id in items:

        if capacity <= 0:
            break

        step_count += 1

        if weight <= capacity:
            capacity -= weight
            total_value += value
            print(f"Item {item_id}: Full item selected")

        else:
            fraction = capacity / weight
            total_value += ratio * capacity
            print(f"Item {item_id}: {fraction:.2%} selected")
            capacity = 0

    print("\nMaximum value in Knapsack:", round(total_value, 2))
    print("Step Count:", step_count)


# Main Program
n = int(input("Enter number of items: "))

if n <= 0:
    print("Enter a positive number of items")

else:
    weights = []
    values = []

    for i in range(n):
        w = float(input(f"Enter weight of item {i+1}: "))
        v = float(input(f"Enter value of item {i+1}: "))

        weights.append(w)
        values.append(v)

    capacity = float(input("Enter knapsack capacity: "))

    if capacity < 0 or any(w <= 0 for w in weights) or any(v < 0 for v in values):
        print("Invalid input!")
    else:
        knapsack(weights, values, capacity)
