def remove_item(item_list, item_to_remove):
    """Remove an item from the list and return the updated list."""
    if item_to_remove in item_list:
        item_list.remove(item_to_remove)
    return item_list

def main():
    # Get the initial list of items from the user, separated by commas.
    items = input("Enter all your grocery items separated by a comma:\n")
    
    # Split the items into a list and strip whitespace
    item_list = [item.strip() for item in items.split(',')]
    
    # Process the shopping list until all items are found
    while item_list:
        # Show the current list of items
        print("Current list:", ', '.join(item_list))
        
        # Get the found item from the user
        found_item = input("Enter found item: ").strip()
        
        # Remove the found item from the list
        item_list = remove_item(item_list, found_item)
        
        # Check if all items have been found
        if not item_list:
            print("All items have been found. Go to the check out.")
            break

if __name__ == "__main__":
    main()

