import random

class Dealer:
    def __init__(self):
        self.card_old = 0
        self.card_new = 0

    def draw_card(self):
        card = random.randint(1, 13)
        self.card_old = self.card_new
        self.card_new = card

    def determine(self):
        if self.card_new > self.card_old:
            result = 'h'
        elif self.card_new < self.card_old:
            result = 'l'
        elif self.card_new == self.card_old:
            result = 'n'
        return result
