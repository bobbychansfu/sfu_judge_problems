correct_username = "bobby"
correct_password = "BEST54"

attempts_left = 3  # Maximum attempts

while attempts_left > 0:
    # Read the username and password from the user.
    username, password = input("Enter username and password separated by space: ").split()

    if username == correct_username and password == correct_password:
        print("Access Granted")
        break  # Exit the loop as the correct credentials are entered.
    else:
        attempts_left -= 1  # Decrease the attempts left by 1 for every incorrect attempt.
        if attempts_left == 0:
            print("Account Locked")
        else:
            print(f"Incorrect credentials. You have {attempts_left} {'attempts' if attempts_left > 1 else 'attempt'} left.")
