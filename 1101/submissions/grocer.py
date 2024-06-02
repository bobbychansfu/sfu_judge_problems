def remove_item(item_list, item_to_remove):
    """Remove an item from the list and return the updated list."""
    if item_to_remove in item_list:
        item_list.remove(item_to_remove)
    return item_list

def main():

    items = input("Enter all your grocery items separated by a comma:\n")

    item_list = [item.strip() for item in items.split(',')]

    while item_list:

        print("Current list:", ', '.join(item_list))

        found_item = input("Enter found item: ").strip()
        #print(found_item)
        item_list = remove_item(item_list, found_item)
        if not item_list:
            print("All items have been found. Go to the check out.")
            break

if __name__ == "__main__":
    main()

