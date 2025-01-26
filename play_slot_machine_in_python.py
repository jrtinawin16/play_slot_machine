import random
import colorama
colorama.init()

# Leaderboard system
leaderboard = []

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
def update_leaderboard(player_name, final_balance):
    global leaderboard
    leaderboard.append((player_name, final_balance))
    leaderboard.sort(key=lambda x: x[1], reverse= True) # Sorts the balance, highest first
    leaderboard = leaderboard[:5] # Keeps top 5 players

    # Writes the leaderboard to a file
    with open("slot_machine_leaderboard.txt", "w", encoding="utf-8") as file:
        file.write("🏆Leaderboard🏆\n")
        for idx, (name, score) in enumerate(leaderboard, 1):
            file.write(f"{idx}. {name}: ₱{score}\n")

def display_leaderboard():
    print(colorama.Fore.LIGHTCYAN_EX + "\n🏆 Leaderboard 🏆")
    for idx, (name, score) in enumerate(leaderboard, 1):
        print(f"{idx}. {name}: ₱{score}")

def main():
    balance = 1000
    min_bet = 20 # Added minimum and maximum bet
    max_bet = 500
    
    # Get player name for leaderboards
    player_name = input("Please enter your name: ")
    print("*******************************")
    print("Welcome to Reydo's Lucky Slots!")
    print("    🍒 🍉 🍋 🍀 🍓 🔔 ⭐    ")
    print("*******************************")
    print(colorama.Fore.LIGHTCYAN_EX + "Legend:")
    print(colorama.Fore.RED + "🍒🍒🍒: -100, " + colorama.Fore.GREEN + "🍉🍉🍉: +100, " + colorama.Fore.YELLOW + "🍋🍋🍋: 2x Bet")
    print(colorama.Fore.MAGENTA + "🍓🍓🍓: 3x Bet, " + colorama.Fore.GREEN + "🍀🍀🍀: 5x Bet, " +
        colorama.Fore.LIGHTYELLOW_EX + "🔔🔔🔔: 10x Bet, " + colorama.Fore.CYAN + "⭐⭐⭐: 20x Bet") 
    print(f"Bet range: ₱{min_bet} up to ₱{max_bet}")


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
        if bet < min_bet or bet > max_bet:
            print(f"Bet must be between ₱{min_bet} and ₱{max_bet}.")
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
            print(f"\n{colorama.Fore.LIGHTYELLOW_EX}Spin #{spin + 1}/{num_spins}...")
            balance -= bet
            row = spin_row()
            print("Spinning...\n")
            print_row(row)

            payout = get_payout(row, bet)
            if payout > 0:
                print(colorama.Fore.GREEN + f"Congratulations, you won ₱{payout}!") # added colorama to color winning message
            else:
                print(colorama.Fore.RED + "Better luck next time!") # added colorama to losing message
            balance += payout

            # Bonus Round
            if random.randint(1,10) == 1:
                print(colorama.Fore.MAGENTA + "🎁 BONUS ROUND! Choose a box: A, B, or C")
                choice = input ("Your choice: ").upper()
                rewards = {"A": 200, "B": 500, "C": 1000}
                bonus = rewards.get(choice,0)
                print(colorama.Fore.LIGHTMAGENTA_EX + f"You won ₱{bonus} in the bonus round!")
                balance += bonus

            if balance <= 0:
                print(colorama.Fore.RED + "You spent all your money during multiple spins.")
                break
        
        ask_play_again = input(colorama.Fore.WHITE + 'Do you want to spin again? (y/n): ').lower()
       
        if ask_play_again != "y":
            break

    update_leaderboard(player_name, balance)

    print(colorama.Fore.WHITE + "-------------------------------------------")
    print(colorama.Fore.WHITE + f"Game over! Your final balance is ₱{balance}")
    print(colorama.Fore.WHITE + "-------------------------------------------")

    display_leaderboard()

if __name__ == '__main__':
    main()