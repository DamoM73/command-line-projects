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

# Set up the constants:
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

BACKSIDE = "backside"

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
        print(f"Current funds: {money}")
        bet = get_bet(money)
        
        # deal cards
        player_hand = []
        dealer_hand = []
        deck = get_deck()
        for _ in range(2):
            player_hand.append(deck.pop())
            dealer_hand.append(deck.pop())
            
        print(player_hand)
        print(dealer_hand)