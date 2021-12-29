import random
from card import Card


class Deck:
    cards = []  # initialize deck to size 52

    def __init__(self):
        for c in range(52):
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
        return len(self.cards)

    def shuffle(self):
        temp = self.cards
        shuffled = []

        for i in range(52):
            shuffled[i] = random.choice(temp)
            temp.remove(shuffled[i])
        self.cards = shuffled

    def deal(self, num_cards):
        dealt = []
        for i in range(num_cards):
            dealt[i] = self.cards[i]
            self.cards.remove(dealt[i])
        return dealt
