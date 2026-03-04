import random

def blackjack():
    print("Welcome to Blackjack!")
    # Implement Blackjack game logic here

def roulette():
    print("Welcome to Roulette!")
    # Implement Roulette game logic here

def slots():
    print("Welcome to Slots!")
    # Implement Slots game logic here

def poker():
    print("Welcome to Poker!")
    # Implement Poker game logic here

def dice():
    print("Welcome to Dice Games!")
    # Implement Dice game logic here

def main_menu():
    while True:
        print("\n--- Casino Main Menu ---")
        print("1. Blackjack")
        print("2. Roulette")
        print("3. Slots")
        print("4. Poker")
        print("5. Dice Games")
        print("6. Exit")

        choice = input("Choose a game (1-6): ")

        if choice == '1':
            blackjack()
        elif choice == '2':
            roulette()
        elif choice == '3':
            slots()
        elif choice == '4':
            poker()
        elif choice == '5':
            dice()
        elif choice == '6':
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == '__main__':
    main_menu()