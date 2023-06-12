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
    # Sort items based on value-to-weight ratio in descending order
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)

    selected_items = []
    total_weight = 0
    total_value = 0

    for item in sorted_items:
        item_weight = item[1]
        item_value = item[1]  # Assuming weight is the value in this case

        if total_weight + item_weight <= capacity:
            selected_items.append(item[0])
            total_weight += item_weight
            total_value += item_value

    return selected_items, total_value

# Example usage
capacity = 30
selected_items, max_value = knapsack_trolley(capacity, fractional_items)

print("The maximum number of items carried on the trolley is:", len(selected_items))
print("The selected items carried on the trolley are:")
for item in selected_items:
    print("-", item)
print("Total value:", max_value)
