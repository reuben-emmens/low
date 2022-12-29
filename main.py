import random
from deck import DECK

if __name__ == "__main__":
    print("Welcome to Low!")

    print("So far, all we have is the deck!")

    deck = DECK
    hand = []

    while True:
        last_user_input = input('Do you want another card?: Y/N ')
        if last_user_input == 'Y':
            card = deck.pop(random.randrange(len(deck)))
            hand.append(card)
            print(f"Your hand: {hand}")
        elif last_user_input == 'N':
            print(f"Dealing no more cards, your final hand: {hand}")
            break
        elif len(deck) == 0:
            print("No more cards in deck.")
            break