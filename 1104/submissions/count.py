import ast

def count_total_people(seating_chart):
    # Initialize a counter for the people
    total_people = 0
    
    # Iterate over each row in the seating chart
    for row in seating_chart:
        # Iterate over each seat in the row
        for seat in row:
            # If the seat is not empty (empty string), increment the counter
            if seat:  # This checks for a non-empty string
                total_people += 1
    
    # Return the total count of people
    return total_people

def main():
    input_string = input()
    parsed_list = ast.literal_eval(input_string)
    print(count_total_people(parsed_list))  

if __name__ == "__main__":
    main()
