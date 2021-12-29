class Card:
    suit = None
    value = None

    suit_names = ['spade', 'heart', 'club', 'diamond']
    value_names = ['zero index', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, value, suit):
        if value < 1 or value > 13:
            raise ValueError("Value must be between 1 and 13")
        else:
            self.value = value

        if suit < 0 or suit > 3:
            raise ValueError("Suit must be between 0 and 3")
        else:
            self.suit = suit

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

    def to_string(self):
        return f'{self.value_names[self.value]} of {self.suit_names[self.suit]}'
