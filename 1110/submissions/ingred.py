def sort_and_total_groceries(n, items):
    # Convert the items into a list of tuples (item, price) and sort by price in descending order
    sorted_items = sorted([(item, int(price)) for item, price in (line.split(' ') for line in items)], key=lambda x: x[1], reverse=True)

    # Calculate the total price
    total_price = sum(price for item, price in sorted_items)

    # Print the sorted items
    for item, price in sorted_items:
        print(f"{item} {price}")

    # Print the total price
    print(f"{total_price}")

# Sample Input
n = int(input())
items = []
for i in range(n):
    items.append(input())

# Running the script with the sample input
sort_and_total_groceries(n, items)
