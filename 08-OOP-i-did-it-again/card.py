class Card:
    def __init__(self, rank, suit):
        if not (isinstance(rank, str) and isinstance(suit, str)):
            raise TypeError()

        if not (rank in _RANKS and suit in _SUITS):
            raise ValueError()

        self.rank = rank
        self.suit = suit

    def __lt__(self, other):
        if not isinstance(other, Card):
            raise TypeError()
        ordered_ranks = list(_RANKS)
        return ordered_ranks.index(self.rank) < ordered_ranks.index(other.rank)

    def __eq__(self, other):
        if not isinstance(other, Card):
            raise TypeError()
        return self.rank == other.rank and self.suit == other.suit

    def __str__(self):
        rank = _RANKS[self.rank] if self.rank in _RANKS else self.rank
        return f"{rank} of {_SUITS[self.suit]}"


# The order of these entries is important; when getting a list of keys
# from a dict, Python defaults to using insertion order. Change the order
# of these entries, and card sorting will break.
_RANKS = {
    "A": "Ace",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "10": "Ten",
    "J": "Jack",
    "Q": "Queen",
    "K": "King",
}
_SUITS = {"C": "Clubs", "D": "Diamonds", "H": "Hearts", "S": "Spades"}
