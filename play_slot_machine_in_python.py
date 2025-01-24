import random
def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🍀", "🍓", "🔔", "⭐"]
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row [0] == row [1] == row[2]:
        if row[0] == "🍒":
            return bet - 100
        elif row[0] == "🍉":
            return bet + 100
        elif row[0] == "🍋":
            return bet * 2
        elif row[0] == "🍓":
            return bet * 3
        elif row[0] == "🍀":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    return 0

def main():
    balance = 1000
    
    print("*******************************")
    print("Welcome to Reydo's Lucky Slots!")
    print("    🍒 🍉 🍋 🍀 🍓 🔔 ⭐    ")
    print("*******************************")

    while balance > 0: 
        print(f"Current balance: ₱{balance}")
        bet = input("Place your bet amount: ₱")
        if not bet.isdigit():
            print("Invalid amount, please try again.")
            continue

        bet = int(bet)
        if bet > balance:
            print("Insufficient money to bet.")
            continue
        if bet <= 0:
            print("Bet must be greater than 0.")
            continue
        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

if __name__ == '__main__':
    main()