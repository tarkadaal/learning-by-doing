from card import Card
from hand import Hand


class UserInput:
    def __init__(self, input_text):
        if not isinstance(input_text, str):
            raise TypeError()
        tokens = input_text.split()
        if not len(tokens) == 5:
            raise ValueError()

        cards = [Card(x[:-1], x[-1]) for x in tokens]
        self.hand = Hand(cards)
