import numpy as np
import random
from card import Card


class Deck:
    cards = np.empty(52)  # initialize deck to size 52

    def __init__(self):
        for c in range(self.cards.size):
            if c < 13:
                self.cards[c] = Card(c + 1, 0)
            elif c < 26:
                self.cards[c] = Card(c + 1 - 13, 1)
            elif c < 39:
                self.cards[c] = Card(c + 1 - 26, 2)
            else:
                self.cards[c] = Card(c + 1 - 39, 3)

    def get_card_at(self, position):
        return self.cards[position]

    @staticmethod
    def get_card_val(card):
        return card.value

    @staticmethod
    def get_card_suit(card):
        return card.suit

    def get_num_cards(self):
        return self.cards.size

    def shuffle(self):
        temp = self.cards
        shuffled = np.empty(52)
        for i in range(52):
            shuffled[i] = random.choice(temp)
            temp.remove(shuffled[i])


    def deal(self, num_cards):
        deal = np.empty(num_cards, dtype=object)
        for c in range(num_cards):
            deal[c] = self.cards[c]
        smaller = np.empty(52 - num_cards)
        for c in range(smaller.size):
            smaller[c] = self.cards[num_cards + c]
        self.cards = smaller
        return deal
