def enter_names():
    names = set()  # Using a set to avoid duplicates

    while True:  # Start an infinite loop to get names
        name = input("Enter a student's name or 'n' to stop: ")
        if name == 'n':  # Break the loop if 'n' is entered
            break
        names.add(name)  # Add the name to the set

    # Sort the names and print them separated by commas
    sorted_names = sorted(names)
    print("List without duplicates, sorted alphabetically:", ", ".join(sorted_names))

# Run the function
enter_names()
