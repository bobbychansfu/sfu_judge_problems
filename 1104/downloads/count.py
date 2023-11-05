import ast

def count_total_people(seating_chart):
    # your code here

def main():
    input_string = input()
    parsed_list = ast.literal_eval(input_string)
    print(count_total_people(parsed_list))  

if __name__ == "__main__":
    main()
