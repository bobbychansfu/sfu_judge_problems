def calculate_score(cards, n):
    # Count the number of aces
    aces = cards.count(1)
    
    # Calculate the initial score without considering aces
    score = sum(cards)
    
    # Add aces to the score, considering them as 11 if beneficial
    for _ in range(aces):
        if score + 10 <= 7 * n:
            score += 10
    
    return score

def main():
    # Get the number of cards
    n = int(input("Number of cards (n): "))
    
    # Get card values from the user
    cards = []
    for i in range(n):
        card = int(input(f"Card {i + 1} (between 1 and 13): "))
        while card < 1 or card > 13:
            print("Invalid card value. Please enter a value between 1 and 13.")
            card = int(input(f"Card {i + 1} (between 1 and 13): "))
        if card > 10:  # Convert face cards to 10 points
            card = 10
        cards.append(card)
    
    # Calculate the score
    score = calculate_score(cards, n)
    
    # Print the result
    if score > 7 * n:
        print("Busted")
    elif score == 7 * n:
        print("Blackjack")
    else:
        print(score)

if __name__ == "__main__":
    main()
