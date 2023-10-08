def main():

    # Ask for the number of courses
    num_courses = int(input("How many courses did you take? "))

    # Initialize a variable to store the total grades
    total_grade = 0

    # Loop through each course and ask for the grade
    for i in range(1, num_courses + 1):
        grade = float(input(f"Course {i} final grade: "))
        total_grade += grade

    # Calculate the average grade
    average_grade = total_grade / num_courses
    average_grade = round(average_grade,2)
    # Print the result
    print(f"Average grade: {average_grade}")

if __name__ == "__main__":
    main()
