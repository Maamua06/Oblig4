import random

starting_chips = 100
chip_counter = starting_chips
deck = []


def create_deck():
    """Lager én kortstokk med 52 kort (4 av hver verdi)."""
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    new_deck = [(rank, f"{rank} of {suit.lower()}") for suit in suits for rank in ranks]
    random.shuffle(new_deck)
    return new_deck


def draw_card():
    """Trekker og fjerner ett kort fra kortstokken."""
    global deck
    if len(deck) == 0:
        deck = create_deck()
    return deck.pop()


def get_card_value(card_val):
    if card_val in ["K", "Q", "J"]:
        return 10
    elif card_val == "A":
        return 11
    return int(card_val)


def calculate_hand_value(hand_values):
    """Beregner verdi og justerer ess til 1 ved behov."""
    total = sum(get_card_value(card) for card in hand_values)
    ace_count = hand_values.count("A")

    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1

    return total


def take_bet(chips):
    while True:
        try:
            bet = int(input(f"You currently have {chips} chips. How many do you bet?: "))
            if bet <= 0:
                print("Innsatsen må være høyere enn 0.")
            elif bet > chips:
                print("Innsatsen kan ikke være høyere enn det totale antallet chips du har.")
            else:
                print(f"\nYou bet {bet} chips out of your {chips} total.")
                return bet
        except ValueError:
            print("Vennligst skriv inn et gyldig heltall.")


def ask_play_again():
    while True:
        choice = input("\nDo you wish to play again?\ny - Yes\nn - No\nAnswer: ").strip().lower()
        if choice in ["y", "yes"]:
            return True
        elif choice in ["n", "no"]:
            return False
        print("Please enter 'y' or 'n'.")


def play_round():
    global chip_counter

    # 1. Spiller oppgir innsats
    bet = take_bet(chip_counter)

    # 2. Spiller og dealer får tildelt 2 kort hver fra kortstokken
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

    # 3. Sjekk Blackjack (21 på initielle to kort)
    if player_total == 21:
        winnings = bet * 2
        chip_counter += winnings
        print(f"\nBlackjack! You automatically win 2 x your bet ({winnings} chips).")
        print(f"Your total amount is now {chip_counter}.")
        return

    # 4. Spillerens tur: Hit eller Stand
    while player_total < 21:
        choice = input("\nDo you wish to hit or stand?\n1 - Hit\n2 - Stand\nAnswer: ").strip()

        if choice in ["1", "hit", "h"]:
            print("\nYou chose to Hit.")
            new_val, new_str = draw_card()
            player_hand_vals.append(new_val)
            player_hand_strs.append(new_str)
            player_total = calculate_hand_value(player_hand_vals)

            print(f"You have been dealt one card ({new_val}). Your hand now consists of the following cards:")
            for card in player_hand_strs:
                print(f"- {card}")
            print(f"\nThe total value of your hand is now {player_total}, and the dealers' is {dealer_visible_val}.")

        elif choice in ["2", "stand", "s"]:
            print("\nYou chose to Stand.")
            break
        else:
            print("Please choose 1 (Hit) or 2 (Stand).")

    # 5. Sjekk om spiller bustet
    if player_total > 21:
        chip_counter -= bet
        print(f"\nYou bust with {player_total}! Dealer wins. You lose {bet} chips.")
        print(f"Your total amount remains {chip_counter}.")
        return

    # 6. Dealerens tur: Trekker helt til hånden er større enn 17 (> 17)
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

    # 7. Avgjør vinner og oppdater chips
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


def main():
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


main()