import random

# set up constraints
OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['Queensland', 'New South Walse', 'Victoria', 'South Australian', 'Tasmania',
           'Western Australian', 'Nothern Territory', 'ACT']
NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
          'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado',
          'Plastic Straw','Serial Killer', 'Telephone Psychic']
PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
           'Workplace', 'Donut Shop', 'Apocalypse Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']

def get_num_headlines():
    while True:
        response = input("How many headlines to generate? > ")
        try:
            response = int(response)
        except:
            print("Please enter a number\n")
        else:
            return response
        

def gen_are_millenials():
    noun = random.choice(NOUNS)
    return f"Are Millennials Killing the {noun} Industry?"  


def gen_dont_know():
    noun = random.choice(NOUNS)
    plural_noun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return f"Without This {noun}, {plural_noun} Could Kill You {when}!"


def gen_big_company():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun_1 = random.choice(NOUNS)
    noun_2 = random.choice(NOUNS)
    return f"Big Companies Hate {pronoun}! See How This {state} {noun_1} Invented a Cheaper {noun_2}"


def gen_wont_believe():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSESIVE_PRONOUNS)
    place = random.choice(PLACES)
    return f"You Won't Believe What This {state} {noun} Found in {pronoun} {place}."


def gen_dont_want_you():
    plural_noun1 = random.choice(NOUNS) + 's'
    plural_noun2 = random.choice(NOUNS) + 's'
    return f"What {plural_noun1} Don't Want You To Know About {plural_noun2}"


def gen_gift_idea():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return f"{number} Gift Ideas to Give Your {noun} From {state}"


def gen_reasons_why():
    number_1 = random.randint(3, 19)
    pluralNoun = random.choice(NOUNS) + 's'
    # number_2 should be no larger than number_1:
    number_2 = random.randint(1, number_1)
    return f"{number_1} Reasons Why {pluralNoun} Are More Interesting Than You Think (Number {number_2} Will Surprise You!)"


def gen_job_automate():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    index = random.randint(0, 2)
    pronoun_1 = POSSESIVE_PRONOUNS[index]
    pronoun_2 = PERSONAL_PRONOUNS[index]
    if pronoun_1 == 'Their':
        return f"This {state} {noun} Didn't Think Robots Would Take {pronoun_1} Job. {pronoun_2} Were Wrong."
    else:
        return f"This {state} {noun} Didn't Think Robots Would Take {pronoun_1} Job. {pronoun_2} Was Wrong."


# ---- MAIN PROGRAM ---- #
print("Clickbait Generator") 
num_headlines = get_num_headlines()

for _ in range(num_headlines):
    clickbait_type = random.randint(1,7)
    
    if clickbait_type == 1:
        print(gen_are_millenials())
    elif clickbait_type == 2:
        print(gen_dont_know())
    elif clickbait_type == 3:
        print(gen_big_company())
    elif clickbait_type == 4:
        print(gen_wont_believe())
    elif clickbait_type == 5:
        print(gen_dont_want_you())
    elif clickbait_type == 6:
        print(gen_gift_idea())
    elif clickbait_type == 7:
        print(gen_reasons_why())
    elif clickbait_type == 8:
        print(gen_job_automate())
        
    
        
        
    
    