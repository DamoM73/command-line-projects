import random


def get_bet():
    print(f"You have ${money} how much do you wish to bet?")
    while True:
        bet = input("> ")
        if bet.isdigit():
            bet = int(bet)
            if bet <= money:
                return bet
            else:
                print("You don't have that much money")
        else:
            print("Please enter a number")

            
def get_choice():
    while True:
        print("Choose: CHO (even) or HAN (odd)")
        response = input("> ").upper()
        if response in ("CHO", "HAN"):
            return response
        

def get_continue():
    while True:
        print("\nDo you wish to continue?")
        response = input("Yes or No > ").upper()
        if response in ("YES","NO"):
            return response

# ----- MAIN PROGRAM ----- #
print("""Cho-Han
In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number\n""")

# --- Game Values --- #
JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

money = 5000
running = True

# --- Main Loop --- #
while running:
    bet = get_bet()
    
    # roll dice
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    
    print("\nThe dealer swirls the cup and you hear the rattle of dice.")
    print("The dealer slams the cup on the floor, still covering the") 
    print("dice and asks for your choice.\n")
    
    choice = get_choice()
    
    # reveal dice
    print("\nThe dealer lifts thee cup to reveal")
    print(f"{JAPANESE_NUMBERS[dice_1]} and {JAPANESE_NUMBERS[dice_2]}")
    print(f"{dice_1} and {dice_2}")
    
    # determine win
    if (dice_1 + dice_2) % 2 == 0:
        correct_bet = "CHO"
    else:
        correct_bet = "HAN"
    
    print(f"\nCorrect choice was {correct_bet}")
        
    if choice == correct_bet:
        house_fee = bet // 10
        print("\nYou win!")
        print(f"Your recieve {bet - house_fee}")
        print(f"House collects {house_fee}")
        money += bet - house_fee
    else:
        print("\nYou loose")
        money -= bet
        
    if money <= 0:
        print("\nYou're borke.")
        running = False
    elif get_continue() == "NO":
        running = False
    
print("\nThanks for playing")