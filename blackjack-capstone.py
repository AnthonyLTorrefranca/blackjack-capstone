# # Set up the deck and basic mechanics
# DECLARE deck as LIST of 52 card values (2-10, J, Q, K, A)
import random

decks = [
            11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
        ] * 4
def shuffle_deck(decks):
    random.shuffle(decks)

def deal_card(decks):
    if not decks:
        shuffle_deck(decks)
    shuffle_deck(decks)
    return decks.pop()


# FUNCTION shuffle_deck(deck):
#     USE random module to REARRANGE deck in place
#
# FUNCTION deal_card(deck):
#     IF deck is not empty:
#         RETURN and REMOVE last card from deck



# # The scoring engine
# FUNCTION calculate_total(hand):
#     SET total = 0
#     SET ace_count = 0
#
#     FOR EACH card IN hand:
#         IF card is "A":
#             total += 11
#             ace_count += 1
#         ELSE IF card is in ["J", "Q", "K"]:
#             total += 10
#         ELSE:
#             total += integer_value(card)
#
#     # Adjust for Aces if busting
#     WHILE total > 21 AND ace_count > 0:
#         total -= 10
#         ace_count -= 1
#
#     RETURN total
# # Participant behaviors and win conditions
# FUNCTION
# player_turn(deck, player_hand):
# WHILE
# calculate_total(player_hand) < 21:
# PRINT
# "Your hand: [cards] (Total: [score])"
# GET
# user_input("hit" or "stand")
#
# IF
# user_input
# IS
# "hit":
# APPEND
# deal_card(deck)
# TO
# player_hand
# ELSE:
# BREAK
# loop
# RETURN
# calculate_total(player_hand)
#
# FUNCTION
# dealer_turn(deck, dealer_hand):
# # Dealer logic: must hit until 17 or higher
# WHILE
# calculate_total(dealer_hand) < 17:
# APPEND
# deal_card(deck)
# TO
# dealer_hand
# RETURN
# calculate_total(dealer_hand)
#
# FUNCTION
# evaluate_winner(p_score, d_score):
# IF
# p_score > 21:
# RETURN
# "Player Busts! Dealer Wins."
# IF
# d_score > 21:
# RETURN
# "Dealer Busts! Player Wins."
# IF
# p_score > d_score:
# RETURN
# "Player Wins!"
# IF
# d_score > p_score:
# RETURN
# "Dealer Wins."
# RETURN
# "It's a Push!"
# # The main execution block
# FUNCTION
# main():
# WHILE
# TRUE:
# SET
# current_deck = shuffle_deck(NEW
# deck)
# SET
# player_hand = [deal_card(current_deck), deal_card(current_deck)]
# SET
# dealer_hand = [deal_card(current_deck), deal_card(current_deck)]
#
# # Execution
# player_score = player_turn(current_deck, player_hand)
#
# IF
# player_score <= 21:
# dealer_score = dealer_turn(current_deck, dealer_hand)
# ELSE:
# dealer_score = calculate_total(dealer_hand)  # For display only
#
# # Final Result
# PRINT
# evaluate_winner(player_score, dealer_score)
#
# IF
# input("Play again? (y/n)")
# IS
# NOT
# "y":
# PRINT
# "Thanks for playing!"
# BREAK
# loop
#
# # Standard Python entry trigger
# IF
# __name__ == "__main__":
# main()