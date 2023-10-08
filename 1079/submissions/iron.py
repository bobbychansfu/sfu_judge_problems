def plate_combinations(total_weight):
    results = []

    # Calculate the maximum number of 20kg, 10kg, and 5kg plates possible for the given weight
    max_20kg = total_weight // 20
    max_10kg = total_weight // 10
    max_5kg = total_weight // 5

    # Loop through all possible combinations of plates
    for num_20kg in range(max_20kg, -1, -1):
        for num_10kg in range(max_10kg, -1, -1):
            for num_5kg in range(max_5kg, -1, -1):
                if num_20kg * 20 + num_10kg * 10 + num_5kg * 5 == total_weight:
                    results.append(f"20kg: {num_20kg}, 10kg: {num_10kg}, 5kg: {num_5kg}")

    return results

# Input
total_weight = int(input().strip())

# Process and Output
combinations = plate_combinations(total_weight)
for combo in combinations:
    print(combo)
