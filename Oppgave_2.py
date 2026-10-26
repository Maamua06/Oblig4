import random

def generate_random_card():
    cards_value = [{"cards_value": 2},
                   {"cards_value": 3},
                   {"cards_value": 4},
                   {"cards_value": 5},
                   {"cards_value": 6},
                   {"cards_value": 7},
                   {"cards_value": 8},
                   {"cards_value": 9},
                   {"cards_value": 10},
                   {"cards_value": "J"},
                   {"cards_value": "Q"},
                   {"cards_value": "K"},
                   {"cards_value": "A"}]

    rand_value_for_card = random.randrange(0,13)
    actual_card_value = cards_value[rand_value_for_card]["cards_value"]

    return actual_card_value

def generate_random_card_type():
    card_type = ["Hearts", "Diamonds", "Spades", "Clubs"]
    rand_value_for_card_type = random.randrange(0,4)

    return card_type[rand_value_for_card_type]

def track_card_from_deck(card_type, card_value):
    list_of_played_cards = [{"card_value": card_value, "card_type": card_type}]

    list_of_remaining_cards = [
    # Spades
    "2 of Spades", "3 of Spades", "4 of Spades", "5 of Spades", "6 of Spades",
    "7 of Spades", "8 of Spades", "9 of Spades", "10 of Spades", "J of Spades",
    "Q of Spades", "K of Spades", "A of Spades",

    # Hearts
    "2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts", "6 of Hearts",
    "7 of Hearts", "8 of Hearts", "9 of Hearts", "10 of Hearts", "J of Hearts",
    "Q of Hearts", "K of Hearts", "A of Hearts",

    # Diamonds
    "2 of Diamonds", "3 of Diamonds", "4 of Diamonds", "5 of Diamonds", "6 of Diamonds",
    "7 of Diamonds", "8 of Diamonds", "9 of Diamonds", "10 of Diamonds", "J of Diamonds",
    "Q of Diamonds", "K of Diamonds", "A of Diamonds",

    # Clubs
    "2 of Clubs", "3 of Clubs", "4 of Clubs", "5 of Clubs", "6 of Clubs",
    "7 of Clubs", "8 of Clubs", "9 of Clubs", "10 of Clubs", "J of Clubs",
    "Q of Clubs", "K of Clubs", "A of Clubs"
]

    for cards in list_of_played_cards:
        try:
            remove_card = f"{cards["card_value"]} of {cards["card_type"]}"
            list_of_remaining_cards.remove(remove_card)
        except ValueError:
            return True

    return False


#Legg til if statement som sjekker om track_card_from_deck returner True hvis den gjør det
# kjør generering av kort en gang til til det blir returnert false og fortsett program
