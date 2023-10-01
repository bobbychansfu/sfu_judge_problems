def main():
    
        # Getting the number of days until D-Day
        days_left = int(input("Enter the number of days left until D-Day: "))

        # Getting the number of mock exams needed to pass
        required_exams = int(input("Enter the number of mock exams needed to pass: "))
        
        # Validate required_exams
        if required_exams < 0:
            raise ValueError("Number of mock exams should be non-negative.")
        
        total_completed = 0  
        
        # Loop through the number of days left and get user input for each day
        for day in range(1, days_left + 1):
            daily_completed = int(input(f"How many mock exams did you complete on day {day}? "))
           
            
            total_completed += daily_completed  # Update the total number of mock exams completed
        
        # Check if the user has completed the required number of mock exams
        if total_completed >= required_exams:
            print("D-Day! Your exam will go as planned.")
        else:
            print("D-Day! Still, hope for the best.")
            

if __name__ == "__main__":
    main()
