import random
def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🍀", "🍓", "🔔", "⭐"]
    return [random.choice(symbols) for _ in range(3)]

def print_row():
    pass

def get_payout():
    pass

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
        print(row)

if __name__ == '__main__':
    main()