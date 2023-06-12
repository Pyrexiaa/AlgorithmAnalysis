fractional_items = [
    ("A sack of corn for the chicken at the barn", 12),
    ("A hoe for the greenhouse", 5),
    ("An oil tank filled with fuel for the boat at the lake", 10),
    ("Tire for the car in the garage", 4),
    ("Tire for the car in the garage", 4),
    ("Tire for the car in the garage", 4),
    ("Tire for the car in the garage", 4)
]

def generate_combinations(items):
    combinations = [[]]

    for item in items:
        new_combinations = []
        for combination in combinations:
            new_combinations.append(combination)
            new_combinations.append(combination + [item])
        combinations = new_combinations

    return combinations

def calculate_value(combination):
    return sum(item[1] for item in combination)

def knapsack_trolley(capacity, items):
    combinations = generate_combinations(items)
    max_value = 0
    selected_items = []

    for combination in combinations:
        combination_weight = sum(item[1] for item in combination)

        if combination_weight <= capacity:
            combination_value = calculate_value(combination)

            if combination_value > max_value:
                max_value = combination_value
                selected_items = [item[0] for item in combination]

    return selected_items, max_value

# Example usage
capacity = 30
selected_items, max_value = knapsack_trolley(capacity, fractional_items)

print("The maximum number of items carried on the trolley is:", len(selected_items))
print("The selected items carried on the trolley are:")
for item in selected_items:
    print("-", item)
print("Total value:", max_value)
