def ask_question(question):
    while True:
        answer = input(question).strip().lower()
        if answer in ['yes', 'no']:
            return answer
        else:
            print("Invalid input. Please respond with 'yes' or 'no'.")

def main():
    taboos = [
        "Do you usually go out during midnight (yes/no): ",
        "Do you take photos as you like at night (yes/no): ",
        "Do you usually whistle at night (yes/no): ",
        "Do you dry your clothes outside at night (yes/no): ",
        "Do you usually go near water during ghost month (yes/no): ",
        "Do you pat people on the shoulder (yes/no): "
    ]
    
    for taboo in taboos:
        response = ask_question(taboo)
        if response == 'yes':
            print('Uh oh! Ghosts are coming for you!')
            return
    print('You are the taboo master!')

if __name__ == "__main__":
    main()
