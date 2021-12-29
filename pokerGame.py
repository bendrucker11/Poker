import deck
import handEvaluator as hE
import handRank as hR
from player import *


class PokerGame:
    d = None
    player1 = None
    player2 = None
    cards_dealt = 0  # the number of cards shown during the game (5 total by the end of the game)
                     # first 3 = flop, 4th = turn, 5th = river
    community_cards = []    # holds the community cards

    def __init__(self):
        d = deck.Deck()
        player1 = Player(money=500)
        player1.hand = d.deal(num_cards=2)
        player1.hand += self.community_cards
        player2 = Player(money=500)
        player2.hand = d.deal(num_cards=2)
        player2.hand += self.community_cards

    def deal_cards(self):
        if self.cards_dealt == 0:
            self.community_cards[0] = self.d.deal(num_cards=1)
            self.community_cards[1] = self.d.deal(num_cards=1)
            self.community_cards[2] = self.d.deal(num_cards=1)
            self.cards_dealt += 3
        elif self.cards_dealt == 3:
            self.community_cards[3] = self.d.deal(num_cards=1)
            self.cards_dealt += 1
        elif self.cards_dealt == 4:
            self.community_cards[4] = self.d.deal(num_cards=1)

    def hand_check(self):
        # have to work from best hand rank to worst so that it keeps the best rank
        # first checks player1's hand
        if hE.HandEvaluator.has_straight_flush(self.player1.hand):
            self.player1.hand_rank = 8
        elif hE.HandEvaluator.has_four_of_a_kind(self.player1.hand):
            self.player1.hand_rank = 7
        elif hE.HandEvaluator.has_full_house(self.player1.hand):
            self.player1.hand_rank = 6
        elif hE.HandEvaluator.has_flush(self.player1.hand):
            self.player1.hand_rank = 5
        elif hE.HandEvaluator.has_straight(self.player1.hand):
            self.player1.hand_rank = 4
        elif hE.HandEvaluator.has_three_of_a_kind(self.player1.hand):
            self.player1.hand_rank = 3
        elif hE.HandEvaluator.has_two_pair(self.player1.hand):
            self.player1.hand_rank = 2
        elif hE.HandEvaluator.has_pair(self.player1.hand):
            self.player1.hand_rank = 1
        else:
            self.player1.hand_rank = 0

        # now checks player2's hand
        if hE.HandEvaluator.has_straight_flush(self.player2.hand):
            self.player2.hand_rank = 8
        elif hE.HandEvaluator.has_four_of_a_kind(self.player2.hand):
            self.player2.hand_rank = 7
        elif hE.HandEvaluator.has_full_house(self.player2.hand):
            self.player2.hand_rank = 6
        elif hE.HandEvaluator.has_flush(self.player2.hand):
            self.player2.hand_rank = 5
        elif hE.HandEvaluator.has_straight(self.player2.hand):
            self.player2.hand_rank = 4
        elif hE.HandEvaluator.has_three_of_a_kind(self.player2.hand):
            self.player2.hand_rank = 3
        elif hE.HandEvaluator.has_two_pair(self.player2.hand):
            self.player2.hand_rank = 2
        elif hE.HandEvaluator.has_pair(self.player2.hand):
            self.player2.hand_rank = 1
        else:
            self.player2.hand_rank = 0

    def determine_winner(self):
        if self.player1.hand_rank > self.player2.hand_rank:
            return self.player1
        elif self.player2.hand_rank > self.player1.hand_rank:
            return self.player2
        else:
            if 1 in self.player1.hand:
                player1_high = 1
            else:
                player1_high = max(self.player1.hand)

            if 1 in self.player2.hand:
                player2_high = 1
            else:
                player2_high = max(self.player2.hand)
            if player1_high > player2_high:
                return self.player1
            else:
                return self.player2

