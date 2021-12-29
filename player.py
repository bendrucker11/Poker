class Player:
    money = None
    hand = []
    hand_rank = None

    def __init__(self, money):
        self.money = money

    def bet(self, amount):
        self.money -= amount


