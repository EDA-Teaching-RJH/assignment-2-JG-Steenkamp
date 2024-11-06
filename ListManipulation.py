import random

# Define card ranks and point rules
CARD_RANKS = list(range(1, 14))  # Ace (1) to King (13)
POINTS = 0  # Initial score

# Helper function to convert card rank to name
def card_name(rank):
    match rank:
        case 1:
            return "Ace"
        case 11:
            return "Jack"
        case 12:
            return "Queen"
        case 13:
            return "King"
        case _:
            return str(rank)

# Draw a random card rank
def draw_card():
    return random.choice(CARD_RANKS)

# Main game function
def play_game():
    global POINTS
    current_card = draw_card()  # Starting card
    print(f"Starting card: {card_name(current_card)}")

    while True:
        # Player's guess
        guess = input("Will the next card be (h)igher or (l)ower? Type 'q' to quit: ").lower()

        if guess == 'q':
            print("Game over! Final score:", POINTS)
            break

        # Draw the next card
        next_card = draw_card()
        print(f"Next card: {card_name(next_card)}")

        # Determine if card is even or odd for double points
        is_even = next_card % 2 == 0  # True if card rank is even

        # Evaluate guess with match statement
        match guess:
            case 'h':
                if next_card > current_card:
                    POINTS += 2 if is_even else 1  # Double points if next_card is even
                    print("Correct! You gained", 2 if is_even else 1, "point(s).")
                else:
                    POINTS -= 2 if is_even else 1  # Lose double points if next_card is even
                    print("Incorrect. You lost", 2 if is_even else 1, "point(s).")
            case 'l':
                if next_card < current_card:
                    POINTS += 2 if is_even else 1  # Double points if next_card is even
                    print("Correct! You gained", 2 if is_even else 1, "point(s).")
                else:
                    POINTS -= 2 if is_even else 1  # Lose double points if next_card is even
                    print("Incorrect. You lost", 2 if is_even else 1, "point(s).")
            case _:
                print("Invalid input. Please type 'h' for higher, 'l' for lower, or 'q' to quit.")
                continue

        # Update current card and display score
        current_card = next_card
        print("Current score:", POINTS)
        print("-" * 20)

# Run the game
if __name__ == "__main__":
    print("Welcome to Higher or Lower!")
    play_game()
