from card import Card

POKER_HAND_SIZE = 5


class Hand:
    def __init__(self, cards):
        valid_cards = [isinstance(x, Card) for x in cards]
        unique_cards = set(cards)
        validity_requirements = (
            all(valid_cards),
            any(valid_cards),
            len(unique_cards) == POKER_HAND_SIZE,
        )
        if not (all(validity_requirements)):
            raise ValueError()
