def calculate_revenue(egg_weights):
    # Define the prices for each full tray based on egg size
    prices = {11: 8.50, 12: 10.25, 'large': 12.55}
    
    # Initialize the count for each category
    count = {0: 0, 11: 0, 12: 0, 'large': 0}
    
    # Count the eggs in each category
    for weight in egg_weights:
        if weight == 0:
            count[0] += 1
        elif weight == 11:
            count[11] += 1
        elif weight == 12:
            count[12] += 1
        elif weight > 12:
            count['large'] += 1
    
    # Calculate the revenue for each category
    revenue = 0
    for size, number_of_eggs in count.items():
        if size != 0:  # Damaged eggs have no revenue
            full_trays = number_of_eggs // 6  # Integer division to find out full trays
            revenue += full_trays * prices[size]
    
    return revenue

n = int(input().strip())
egg_weights = list(map(int, input().strip().split()))
print(f"{calculate_revenue(egg_weights):.2f}")
