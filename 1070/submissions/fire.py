def ask_question(question):
    response = input(question).strip()
    
    while response not in ['1', '2']:
        print("Invalid response.")
        response = input(question).strip()
    return response

def main():
    questions = [
        "(1) Take many things or (2) Take nothing? ",
        "(1) Stay in the room or (2) Leave the room? ",
        "(1) Walk or (2) Crawl? ",
        "(1) Take the elevator or (2) Take the stairs? "
    ]
    
    attempts_left = 4
    
    while attempts_left > 0:
        success = True
        for question in questions:
            response = ask_question(question)
            if response == '1':
                print("You did not survive. Try again.")
                success = False
                break
                
        if success:
            print("Congratulations! You have successfully escaped the fire!")
            break
        else:
            attempts_left -= 1
            if attempts_left == 0:
                print("You've run out of attempts. The program is now ending.")
            else:
                print(f"You have {attempts_left} {'attempts' if attempts_left > 1 else 'attempt'} left.")
                
if __name__ == "__main__":
    main()
