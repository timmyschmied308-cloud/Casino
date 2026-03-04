# Slots Machine Game

## Description
This is a simple slots machine game implemented in Python. The game features spinning reels and winning combinations. When the player presses 'Enter', the reels will spin and display a combination. If the combination matches a winning combination, the player wins!

## Code
```python
import random

class SlotsMachine:
    def __init__(self):
        self.reels = ['🍒', '🍋', '🍊', '🍉', '🍇', '🔔', '💰']  # Symbols in the slots
        self.winning_combinations = [
            ['🍒', '🍒', '🍒'],
            ['🍋', '🍋', '🍋'],
            ['🍊', '🍊', '🍊'],
            ['🍉', '🍉', '🍉'],
            ['🍇', '🍇', '🍇'],
            ['🔔', '🔔', '🔔'],
            ['💰', '💰', '💰']
        ]

    def spin_reels(self):
        return [random.choice(self.reels) for _ in range(3)]

    def check_win(self, combination):
        return combination in self.winning_combinations

    def play(self):
        print("Welcome to the Slots Machine!")
        input("Press 'Enter' to spin...")
        result = self.spin_reels()
        print(f"Reels: {result}")
        if self.check_win(result):
            print("Congratulations! You win!")
        else:
            print("Sorry, you lose. Try again!")

if __name__ == '__main__':
    game = SlotsMachine()
    game.play()
```

## How to Run
1. Install Python on your machine.
2. Save this code in a file named `slots_machine.py`.
3. Run the game with the command: `python slots_machine.py`.

## Features
- Simple and colorful UI
- Randomly generated results
- Easy to play

## Author
Timmy Schmid