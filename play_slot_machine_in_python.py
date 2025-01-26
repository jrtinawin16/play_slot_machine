import random
import colorama
colorama.init()
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
        print(colorama.Fore.WHITE + f"Current balance: ₱{balance}")
        bet = input("Place your bet amount: ₱")
        print (colorama.Fore.WHITE + (bet))
        if not bet.isdigit():
            print(colorama.Fore.LIGHTRED_EX + "Invalid amount, please try again.")
            continue

        bet = int(bet)
        if bet > balance:
            print("Insufficient money to bet.")
            continue
        if bet <= 0:
            print("Bet must be greater than 0.")
            continue
        # Asks user how many spins to play
        num_spins = input(colorama.Fore.WHITE + "How many spins would you like to play? " + colorama.Style.RESET_ALL)
        if not num_spins.isdigit():
            num_spins = 1
        else:
            num_spins = int(num_spins)
        # Loop if user wants multiple spins
        for spin in range(num_spins):
            if balance < bet:
                print(colorama.Fore.RED + "Insufficient balance to continue spin")
                break
            print(f"\n{colorama.Fore.LIGHTYELLOW_EX}Spin # {spin + 1}/{num_spins}...")
        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(colorama.Fore.GREEN + f"Congratulations, you won ₱{payout}!") # added colorama to color winning message
        else:
            print(colorama.Fore.RED + "Better luck next time!") # added colorama to losing message
        balance += payout
        
        ask_play_again = input('Do you want to spin again? (y/n): ').lower()
       
        if ask_play_again != "y":
            break
    print(colorama.Fore.WHITE + "-------------------------------------------")
    print(colorama.Fore.WHITE + f"Game over! Your final balance is ₱{balance}")
    print(colorama.Fore.WHITE + "-------------------------------------------")
if __name__ == '__main__':
    main()