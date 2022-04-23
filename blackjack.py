import random, sys

def get_bet(max_bet):
    while True:
        bet = input("How much do you want to bet? > ").strip()
        if bet.isdecimal():
            bet = int(bet)
            if bet <= max_bet:
                return bet
            
        print(f"Please enter a value between 1 and {max_bet}\n")


def get_deck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2,11):
            deck.append((str(rank), suit))
        for rank in ("J", "Q", "K", "A"):
            deck.append((str(rank), suit))
    random.shuffle(deck)
    return deck


def get_hand_value(hand):
    value = 0
    num_aces = 0
    
    # add the face values of non-ace cards
    for card in hand:
        rank = card[0]
        if rank == "A":
            num_aces += 1
        elif rank in ("K", "Q", "J"):
            value += 10
        else:
            value += int(rank)
    
    # add value of aces as 1s
    value += num_aces
    
    # if another 10 can be added for each ace
    for _ in range(num_aces):
        if value <= 11:
            value += 10
    
    return value
    
    
def display_cards(hand):
    # card display has 5 rows
    rows = ["","","","",""]
    
    # build card
    for card in hand:
        rows[0] += f" {chr(8212)}{chr(8212)}{chr(8212)} "
        if card == "backside":
            # Print card back
            rows[1] += "|## |"
            rows[2] += "| # |"
            rows[3] += "| ##|"
        else:
            # Print card front
            rank, suit = card
            rows[1] += f"|{rank.ljust(2)} |"
            rows[2] += f"| {suit} |"
            rows[3] += f"| {rank.rjust(2)}|"
        rows[4] += f" {chr(8212)}{chr(8212)}{chr(8212)} "
        
    # display card
    for row in rows:
        print(row)
    print("")

def display_hands(player_hand, dealer_hand, player_turn):    
    # show dealer's hand
    if not player_turn:
        print(f"Dealer: {get_hand_value(dealer_hand)}")
        display_cards(dealer_hand)
    else:
        print("Dealer: ???")
        display_cards(["backside"] + dealer_hand[1:])
        
    # show player's hand
    print(f"Player: {get_hand_value(player_hand)}")
    display_cards(player_hand)
    

def get_move(hand, bet, money):
    while True:
        # build options
        moves = ["(H)it", "(S)tand"]
        
        if len(hand) == 2 and money - bet > 0:
            moves.append("(D)ouble down")
            
        # display options
        move_prompt = ", ".join(moves) + ": "
        move = input(move_prompt).upper()
        if move in ("H", "S"):
            return move
        elif move == "D" and "(D)ouble down" in moves:
            return move
        

def get_continue():
    while True:
        print("Do you wish to continue?")
        response = input("(Y)es or (N)o")
        if response in ("Y","N"):
            return response

# Set up the constants:
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

print("Blackjack")
print("=========")

print("""
Rules:
    Try to get as close to 21 without going over.
    Kings, Queens, and Jacks are worth 10 points. 
    Aces are worth 1 or 11 points.
    Cards 2 through 10 are worth their face value.
    
    (H)it to take another card.
    (S)tand to stop taking cards.
    
    On your first play, you can (D)ouble down to increase your bet
    but must hit exactly one more time before standing.
    
    In case of a tie, the bet is returned to the player.
    
    The dealer stops hitting at 17.
    """)

# ----- MAIN PROGRAM ----- #

# --- Game Variables --- #
money = 5000
running = True

# --- Main Loop --- #
while running:
    # check if player has run out of money
    if money <= 0:
        print("You're broke!")
        print("Good thing you weren't playing for real money")
        running = False
    else:
        # ask player for bet
        print(f"Current funds: ${money}")
        bet = get_bet(money)
        
        # deal cards
        player_hand = []
        dealer_hand = []
        deck = get_deck()
        for _ in range(2):
            player_hand.append(deck.pop())
            dealer_hand.append(deck.pop())
            
        # player's turn
        player_turn = True
        while player_turn:
            
            # show hands
            display_hands(player_hand, dealer_hand, player_turn)
            
            # get player's move
            move = get_move(player_hand, bet, money)
            
            if move == "D":
                additional_bet = get_bet(min(bet, money-bet))
                bet += additional_bet
                print(f"Bet increased to {bet}.")
            
            if move in ("H", "D"):
                player_hand.append(deck.pop())
                
                if get_hand_value(player_hand) > 21:
                    player_turn = False
            
            if move in ("S", "D"):
                player_turn = False
                
        # dealer turn
        if get_hand_value(player_hand) <= 21:
            while get_hand_value(dealer_hand) < 17:
                # show hands
                display_hands(player_hand, dealer_hand, player_turn)
                
                # the dealer hits
                print("The dealer hits...")
                dealer_hand.append(deck.pop())
                
        # check winner
        display_hands(player_hand, dealer_hand, player_turn)
        
        player_value = get_hand_value(player_hand)
        dealer_value = get_hand_value(dealer_hand)
        
        if dealer_value > 21:
            print(f"Dealer busts! You win ${bet}")
            money += bet
        elif player_value > 21 or player_value < dealer_value:
            print(f"You lose ${bet}")
            money -= bet
        elif player_value > dealer_value:
            print(f"You win ${bet}")
            money += bet
        elif player_value == dealer_value:
            print("It's a tie, bet it returned to you.")
            
    if get_continue == "N":
        running = False
        
print(f"You started with $5000, you are leaving with ${money}.")