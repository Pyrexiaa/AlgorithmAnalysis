items = [
    ("A sack of corn for the chicken at the barn", 12),
    ("A hoe for the greenhouse", 5),
    ("An oil tank filled with fuel for the boat at the lake", 10),
    ("Four pieces of tires for the car in the garage", 16)
]

fractional_items = [
    ("A sack of corn for the chicken at the barn", 12),
    ("A hoe for the greenhouse", 5),
    ("An oil tank filled with fuel for the boat at the lake", 10),
    ("Tire for the car in the garage", 4),
    ("Tire for the car in the garage", 4),
    ("Tire for the car in the garage", 4),
    ("Tire for the car in the garage", 4)
]

def knapsack_trolley(capacity, items):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight = items[i - 1][1]
        value = weight  # Assuming weight is the value in this case

        for j in range(1, capacity + 1):
            if weight > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

    selected_items = []
    total_weight = capacity
    total_value = dp[n][capacity]

    # Backtracking to find the selected items
    for i in range(n, 0, -1):
        if dp[i][total_weight] != dp[i - 1][total_weight]:
            selected_items.append(items[i - 1][0])
            total_weight -= items[i - 1][1]

    return selected_items, total_value

# Example usage
capacity = 30
selected_items, max_value = knapsack_trolley(capacity, fractional_items)

print("The maximum number of items carried on the trolley is:", len(selected_items))
print("The selected items carried on the trolley are:")
for item in selected_items:
    print("-", item)
print("Total value:", max_value)

