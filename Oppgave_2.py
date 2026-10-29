import random

starting_chips = 100
chip_counter = starting_chips
deck = []

# Denne funskjonen lager kortstokken som skal brukes i blackjack
def create_deck():
    card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    card_types = ["hearts", "diamonds", "spades", "clubs"]

    card_deck = []
    for types in card_types:
        for val in card_values:
            card_tuple = (val, f"{val} of {types}")
            card_deck.append(card_tuple)

    random.shuffle(card_deck)
    return card_deck

# Funskjon som trekker kort fra kortstokken og fjerner det etter at det har blitt trukket
def draw_card():
    #Global blir brukt for at python skal referere til listen deck utenfor funskjonen
    # og ikke bare lage en lokal variabel i funksjonen
    global deck
    if len(deck) == 0:
        deck = create_deck()
    # deck.pop() returnere verdien som blir fjernet fra listen som
    # er det kortet spilleren eller dealeren får
    return deck.pop()


def get_card_value(card_val):
    if card_val in ["K", "Q", "J"]:
        return 10
    elif card_val == "A":
        return 11
    return card_val

#Funskjon som regner ut verdien på kortene og bestemmer verdien
# utifra om totale verdien overstiger 21
def calculate_hand_value(hand_values):
    total = 0
    ace_count = 0

    for card in hand_values:
        total += get_card_value(card)
        if card == "A":
            ace_count += 1

    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1

    return total

#Funskjon som spør spilleren hvor mange chips de ønsker å spille for
def take_bet(chips):
    while True:
        try:
            bet = int(input(f"You currently have {chips} chips. How many do you bet?: "))
            if bet <= 0:
                print("The bet must be higher than 0.")
            elif bet > chips:
                print("The bet cannot be higher than the amount of chips you have.")
            else:
                print(f"\nYou bet {bet} chips out of your {chips} total.")
                return bet
        except ValueError:
            print("Please enter a whole number.")

# Funskjon som sjekker om spilleren har black jack
def black_jack(hand_val, bet_val):
    global chip_counter
    if hand_val == 21:
        winnings = bet_val * 2
        chip_counter += winnings
        print(f"\nCongratulation you got Blackjack. You won {winnings}")
        print(f"Your total amount is now {chip_counter}.")
        return True
    return False

#logikk som håndtere hit og stand under spilling
def hit_stand_logic(hand_val, player_hand_list_vals, player_hand_strs_list, dealer_vis_hand_val):
    while hand_val < 21:
        choice = input("\nDo you wish to hit or stand?\n1 - Hit\n2 - Stand\nAnswer: ").strip()

        if choice in ["1", "hit", "h"]:
            print("\nYou chose to Hit.")
            new_val, new_str = draw_card()
            player_hand_list_vals.append(new_val)
            player_hand_strs_list.append(new_str)
            hand_val = calculate_hand_value(player_hand_list_vals)

            print(f"You have been dealt one card ({new_val}). You have these cards in your hand now:")
            for card in player_hand_strs_list:
                print(f"- {card}")
            print(f"\nThe total value of your hand is now {hand_val}, and the dealers' is {dealer_vis_hand_val}.")
        elif choice in ["2", "stand", "s"]:
            print("\nYou chose to Stand.")
            break
        else:
            print("Please choose 1 (Hit) or 2 (Stand).")

    return hand_val


#Spør spilleren om de ønsker å spille på nytt
def ask_play_again():
    while True:
        choice = input("\nDo you wish to play again?\ny - Yes\nn - No\nAnswer: ").strip().lower()
        if choice in ["y", "yes"]:
            return True
        elif choice in ["n", "no"]:
            return False
        print("Please enter 'y' or 'n'.")

#funskjon som starter runden og deler ut kort og tar og bruker de andre funskjone
#og setter de sammen sånn at spillet skal fungere
def play_round():
    global chip_counter

    bet = take_bet(chip_counter)

    p_val1, p_str1 = draw_card()
    p_val2, p_str2 = draw_card()
    player_hand_vals = [p_val1, p_val2]
    player_hand_strs = [p_str1, p_str2]
    player_total = calculate_hand_value(player_hand_vals)

    d_val1, d_str1 = draw_card()
    d_val2, d_str2 = draw_card()
    dealer_hand_vals = [d_val1, d_val2]
    dealer_hand_strs = [d_str1, d_str2]
    dealer_visible_val = calculate_hand_value([d_val1])

    print(f"\nThe cards have been dealt. You have a {p_str1} and a {p_str2}, with a total value of {player_total}.")
    print(f"\nThe dealers visible card is a {d_str1}, with a value of {dealer_visible_val}.")

    if black_jack(player_total, bet):
        return

    player_total = hit_stand_logic(player_total, player_hand_vals, player_hand_strs, dealer_visible_val)

    if player_total > 21:
        chip_counter -= bet
        print(f"\nYou bust with {player_total}! Dealer wins. You lose {bet} chips.")
        print(f"Your total amount remains {chip_counter}.")
        return

    print("\nThe dealer draws cards until their hand value is greater than 17. The dealers cards are the following:")
    dealer_total = calculate_hand_value(dealer_hand_vals)

    while dealer_total <= 17:
        new_val, new_str = draw_card()
        dealer_hand_vals.append(new_val)
        dealer_hand_strs.append(new_str)
        dealer_total = calculate_hand_value(dealer_hand_vals)

    for card in dealer_hand_strs:
        print(f"- {card}")

    print(f"\nThe total value of the dealers hand is {dealer_total} compared to your hand's value; {player_total}.")

    if dealer_total > 21:
        chip_counter += bet
        print(f"\nDealer busts! You win {bet} chips, and your total amount is {chip_counter}.")
    elif player_total > dealer_total:
        chip_counter += bet
        print(f"\nYou win! You earn {bet} chips, and your total amount is {chip_counter}.")
    elif player_total < dealer_total:
        chip_counter -= bet
        print(f"\nDealer wins. You lose {bet} chips, and your total amount is {chip_counter}.")
    else:
        print(f"\nNo one wins. You keep your chips, and your total amount remains {chip_counter}.")


#Hovedfunskjonen som kjører koden og sjekker om du har mer enn 0 chips
# og spør om du har lyst til å spille igjen
def game():
    global chip_counter, deck
    deck = create_deck()

    while chip_counter > 0:
        play_round()

        if chip_counter <= 0:
            print("\nYou have run out of chips! Game over.")
            break

        if not ask_play_again():
            print("\nSee you next time! :)\n")
            break


game()