import random

def game():
    choices = ['snake', 'water', 'gun']
    user_score = 0
    computer_score = 0
    rounds = int(input("How many rounds you want to play? "))

    for i in range(rounds):
        print(f"\nRound {i+1}")
        user = input("Choose snake, water or gun: ").lower()
        computer = random.choice(choices)
        
        print(f"You chose: {user}")
        print(f"Computer chose: {computer}")
        
        if user == computer:
            print("It's a tie!")
        elif (user == 'snake' and computer == 'water') or \
             (user == 'water' and computer == 'gun') or \
             (user == 'gun' and computer == 'snake'):
            print("You win this round!")
            user_score += 1
        elif user in choices:
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("Invalid input! Round skipped.")

    print("\n--- Game Over ---")
    print(f"Your score: {user_score}")
    print(f"Computer score: {computer_score}")

    if user_score > computer_score:
        print(" You won the game!")
    elif user_score < computer_score:
        print("Computer won the game!")
    else:
        print("It's a draw!")


game()
