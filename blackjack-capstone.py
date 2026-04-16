# Set up the deck and basic mechanics
# DECLARE deck as LIST of 52 card values (2-10, J, Q, K, A)
# importing random
import random
# define deck
deck = [
    11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
] * 4
# function for the shuffle deck
def shuffle_deck(deck):
    random.shuffle(deck)
# function for the deal card
def deal_card(deck):
    if not deck:
        return None
    shuffle_deck(deck)
    return deck.pop()
# function for handling total and ace_count
def hand_total(hand):
    total = 0
    ace_count = 0
    for card in hand:
        if card == 11:
            ace_count += 1

    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1
    return total
# function for player turn with parameter of deck and player hand:
# player_turn(deck, player_hand):
def player_turn(deck, player_hand):
    # WHILE calculate_total(player_hand) < 21:
    while calculate_total(player_hand) < 21:
        print(f"Your hand: {deck} (Total: {hand_total(player_hand)})")
        user_input = input("Hit or stand? ").lower()

# FUNCTION dealer_turn(deck, player_hand):
def dealer_turn(deck, player_hand):
    # Dealer logic: must hit until 17 or higher
    # WHILE calculate_total(player_hand) < 17:
    while calculate_total(player_hand) < 17:
        # APPEND deal_card(deck) TO player_hand
        player_hand.append(deal_card(deck))
    return calculate_total(player_hand)
        # RETURN
        # calculate_total(player_hand)
def evaluate_winner(player_hand, dealer):
    if player_hand > 21:
        return "Player Busts! Dealer wins."
    elif dealer > 21:
        return "Dealer Busts! Player wins."
    elif player_hand > dealer:
        return "Player Wins!"
    elif dealer > player_hand:
        return "Dealer Wins!"
    return "It's a Push!"

def main():
    while True:
        current_deck = shuffle_deck(deck)
        player_hand = [deal_card(current_deck), deal_card(current_deck)]
        dealer_hand = [deal_card(current_deck), deal_card(current_deck)]
        player_score = player_turn(current_deck, player_hand)

        if player_score <= 21:
            dealer_score = dealer_turn(current_deck, player_hand)
        else:
            dealer_score = calculate_total(dealer_hand)


# The main execution block
# FUNCTION main():
    # WHILE TRUE:
    # SET current_deck = shuffle_deck(NEW deck)
    # SET player_hand = [deal_card(current_deck), deal_card(current_deck)]
    # SET dealer_hand = [deal_card(current_deck), deal_card(current_deck)]
    # Execution
    # player_score = player_turn(current_deck, player_hand)
    # IF player_score <= 21:
        # dealer_score = dealer_turn(current_deck, dealer_hand)
    # ELSE:
        # dealer_score = calculate_total(dealer_hand)  # For display only
    # Final Result
    # PRINT evaluate_winner(player_score, dealer_score)
    # IF input("Play again? (y/n)")
    # IS NOT "y":
        # PRINT "Thanks for playing!"
    # BREAK
        # loop
    # Standard Python entry trigger
    # IF __name__ == "__main__":
    # main()