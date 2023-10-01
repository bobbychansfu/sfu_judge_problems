
def main():
    
    step_count = 0
    
    while True:
        move = input("Enter your move ('step', 'dig', or 'rest'): ").lower()
        
        if move not in ['step', 'dig', 'rest']:
            print("Invalid move! Please enter 'step', 'dig', or 'rest'.")
            continue
        
        if move == 'step':
            step_count += 1
        
        if move == 'dig':
            if 4 < step_count < 10 and step_count % 2 != 0:
                print("Congratulations! You found the treasure and won the game!")
                break
            else:
                print("Oh no! You have been captured by pirates! You lose!")
                break
        
        if step_count > 10:
            print("Oh no! You fell off a cliff! You lose!")
            break
        
        if move == 'rest':
            print("You decided to rest. Be cautious and make your next move wisely.")
            
if __name__ == "__main__":
    main()

