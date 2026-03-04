import random

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def main():
    print("Welcome to the Dice Game!")
    balance = 100  # Starting balance

    while True:
        print(f"Your current balance is: ${balance}")
        bet = input("Enter your bet (or type 'exit' to quit): ")

        if bet.lower() == 'exit':
            print("Thanks for playing! Goodbye!")
            break

        try:
            bet = int(bet)
            if bet > balance:
                print("You can't bet more than your current balance!")
                continue
            elif bet <= 0:
                print("Please enter a valid bet amount.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        prediction = input("Predict the sum of the dice (2-12): ")

        try:
            prediction = int(prediction)
            if prediction < 2 or prediction > 12:
                print("Invalid prediction. The sum of two dice can only be between 2 and 12.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 2 and 12.")
            continue

        dice_sum = roll_dice()
        print(f"You rolled: {dice_sum}")

        if dice_sum == prediction:
            print("Congratulations! You win!")
            balance += bet
        else:
            print("Sorry, you lose.")
            balance -= bet

        if balance <= 0:
            print("You've run out of money! Game over.")
            break

if __name__ == "__main__":
    main()
