import pytest
from hand import Hand
from card import Card


def _str_to_cards(text):
    return [Card(x[:-1], x[-1]) for x in text.split()]


def test_hand():
    assert Hand(_str_to_cards("AH 4C 8D 8H 4D"))


@pytest.mark.parametrize(
    "cards",
    [
        tuple(),
        list(),
        _str_to_cards("8D"),
        _str_to_cards("3H 6H 7C 8C 6H"),
        _str_to_cards("3H 6H 7C 8C"),
    ],
)
def test_invalid_hands(cards):
    with pytest.raises(ValueError):
        Hand(cards)
