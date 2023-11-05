import calendar

def printCalendar(y, m):
    
    first_day,num_days = calendar.monthrange(y,m)
    day_of_week = calendar.weekday(y, m, 1)  
    day_of_week = (first_day + 1) % 7

    print(" " * (2 * (day_of_week)) + " "*(day_of_week), end="")  # Two spaces for each day

    for day in range(1, num_days + 1):
        print(f"{day:2}", end=" ")  
        if (day + day_of_week) % 7 == 0:
            print()

    if (num_days + day_of_week) % 7 != 0:
        print()

def main():
    y,m = map(int,(input().split()))
    printCalendar(y,m)

if __name__ == "__main__":
    main()
