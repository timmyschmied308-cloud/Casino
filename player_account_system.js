class Player {
    constructor(name) {
        this.name = name;
        this.balance = 0; // in currency
        this.chips = 0; // in chips
        this.gameStats = {
            gamesPlayed: 0,
            gamesWon: 0,
            gamesLost: 0,
        };
    }

    // Method to deposit money
    deposit(amount) {
        this.balance += amount;
    }

    // Method to withdraw money
    withdraw(amount) {
        if (amount <= this.balance) {
            this.balance -= amount;
        } else {
            throw new Error('Insufficient balance');
        }
    }

    // Method to add chips
    buyChips(amount) {
        this.chips += amount;
    }

    // Method to play a game
    playGame(result) {
        this.gameStats.gamesPlayed++;
        if (result === 'win') {
            this.gameStats.gamesWon++;
        } else if (result === 'loss') {
            this.gameStats.gamesLost++;
        }
    }

    // Method to get player stats
    getStats() {
        return this.gameStats;
    }
} 

// Example usage:
// const player = new Player('Alice');
// player.deposit(100);
// player.buyChips(10);
// player.playGame('win');
console.log(player.getStats());
