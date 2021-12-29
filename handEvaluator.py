from card import *
from deck import *


class HandEvaluator:

    @staticmethod
    def has_pair(cards):
        for i in range(cards.size):
            for j in range(cards.size):
                if Deck.get_card_val(cards[i]) == Deck.get_card_val(cards[j]) and i != j:
                    return True
        return False

    @staticmethod
    def has_two_pair(cards):
        count = 0
        first = 0
        second = 0
        if not HandEvaluator.has_pair(cards):
            return False
        for i in range(cards.size):
            for j in range(cards.size):
                if i == j:
                    continue
                if Deck.get_card_val(cards[i]) == Deck.get_card_val(cards[j]) and Deck.get_card_val(cards[i]) != first \
                        and Deck.get_card_val(cards[j]) != second:
                    count += 1
                    if count == 1:
                        first = Deck.get_card_val(cards[i])
                    elif count == 2:
                        second = Deck.get_card_val(cards[i])
        if count == 2:
            return True
        else:
            return False

    @staticmethod
    def has_three_of_a_kind(cards):
        for i in range(cards.size):
            for j in range(cards.size):
                for k in range(cards.size):
                    if i == j or i == k or j == k:
                        continue
                    if Deck.get_card_val(cards[i]) == Deck.get_card_val(cards[j]) and Deck.get_card_val(cards[i]) == Deck.get_card_val(cards[k]) \
                            and Deck.get_card_val(cards[j]) == Deck.get_card_val(cards[k]):
                        return True
        return False

    @staticmethod
    def has_straight(cards):
        for i in range(cards.size):
            for j in range(cards.size):
                for k in range(cards.size):
                    for n in range(cards.size):
                        for m in range(cards.size):
                            if i == j or i == k or i == n or i == m or j == k or j == n or j == m or k == n or k == m or n == m:
                                continue
                            if Deck.get_card_val(cards[i]) == Deck.get_card_val(cards[j]) + 1 and Deck.get_card_val(cards[j]) == Deck.get_card_val(cards[k]) + 1 and Deck.get_card_val(cards[k]) == Deck.get_card_val(cards[n]) + 1 and Deck.get_card_val(cards[n]) == Deck.get_card_val(cards[m]) + 1:
                                return True
        return False

    @staticmethod
    def has_flush(cards):
        for i in range(cards.size):
            for j in range(cards.size):
                for k in range(cards.size):
                    for n in range(cards.size):
                        for m in range(cards.size):
                            if i == j or i == k or i == n or i == m or j == k or j == n or j == m or k == n or k == m or n == m:
                                continue
                            if Deck.get_card_suit(cards[i]) == Deck.get_card_suit(cards[j]) == Deck.get_card_suit(cards[k]) == Deck.get_card_suit(cards[n]) == Deck.get_card_suit(cards[m]):
                                return True
        return False

    @staticmethod
    def has_full_house(cards):
        if HandEvaluator.has_two_pair(cards) and HandEvaluator.has_three_of_a_kind(cards):
            return True
        return False

    @staticmethod
    def has_four_of_a_kind(cards):
        for i in range(cards.size):
            for j in range(cards.size):
                for k in range(cards.size):
                    for m in range(cards.size):
                        if i == j or i == k or i == m or j == k or j == m or k == m:
                            continue
                        if Deck.get_card_val(cards[i]) == Deck.get_card_val(cards[j]) == Deck.get_card_val(cards[k]) == Deck.get_card_val(cards[m]):
                            return True
        return False

    @staticmethod
    def has_straight_flush(cards):
        return HandEvaluator.has_flush(cards) and HandEvaluator.has_straight(cards)

