import calendar

def printCalendar(y, m):
    # Function to check if a given year is a leap year
    def is_leap_year(y):
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            return True
        else:
            return False

    # List of number of days in each month (0-based indexing)
    days_in_month = [31, 29 if is_leap_year(y) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Calculate the day of the week for the first day of the given month and year
    day_of_week = calendar.weekday(y, m, 1)  # Monday is 0 and Sunday is 6
    day_of_week = (day_of_week + 1) % 7
    # Print the calendar
    # Print initial spaces based on the day of the week
    print(" " * (2 * (day_of_week)) + " "*(day_of_week), end="")  # Two spaces for each day

    # Print all the days for the month
    for day in range(1, days_in_month[m - 1] + 1):
        print(f"{day:2}", end=" ")  # Right-aligned (width 2) day

        # If the current day is Saturday, print a new line
        if (day + day_of_week) % 7 == 0:
            print()

    # If the last day wasn't Saturday, print a final new line
    if (days_in_month[m - 1] + day_of_week) % 7 != 0:
        print()

def main():
    y,m = map(int,(input().split()))
    printCalendar(y,m)

if __name__ == "__main__":
    main()
