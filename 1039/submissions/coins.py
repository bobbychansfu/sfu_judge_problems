cents = input("Please enter the number of cents: ")

if not (cents.isdigit()):
    print("not possible")
else:
    cents = int(cents)

    t = cents // 200
    cents = cents % 200

    l = cents // 100
    cents = cents % 100

    h = cents // 50
    cents = cents % 50

    q = cents // 25
    cents = cents % 25

    d = cents // 10
    cents = cents % 10

    p = cents // 5
    cents = cents % 5

    print (t+l+h+q+d+p+cents)