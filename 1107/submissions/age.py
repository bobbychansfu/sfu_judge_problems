def main():
    # Read the number of students
    n = int(input())
    
    # Initialize variables
    total_age = 0
    max_age = -1
    students = {}

    # Read student data
    for _ in range(n):
        name, age = input().split()
        age = int(age)
        total_age += age
        
        # Update max age and student names
        if age > max_age:
            max_age = age
            students = {name}
        elif age == max_age:
            students.add(name)

    # Calculate average age
    average_age = total_age / n

    # Print average age
    print(f"{average_age:.2f}")

    # Print names of oldest students in lexicographical order
    for name in sorted(students):
        print(name)

if __name__ == "__main__":
    main()
