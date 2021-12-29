from card import *
from deck import *

import numpy as np


class Player:
    money = None
    hand = np.empty(2, dtype=object)

    def __init__(self, money):
        self.money = money
        hand = Deck.deal(num_cards=2)

    def bet(self, amount):
        self.money -= amount
