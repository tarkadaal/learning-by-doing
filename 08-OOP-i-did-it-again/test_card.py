import pytest
from card import Card


def test_card_properties():
    result = Card("3", "H")
    assert result.rank == "3"
    assert result.suit == "H"


@pytest.mark.parametrize(
    "rank,suit",
    [
        (None, None),
        (None, "H"),
        ("3", None),
        (3, "C"),
    ],
)
def test_card_invalid_types(rank, suit):
    with pytest.raises(TypeError):
        Card(rank, suit)


@pytest.mark.parametrize(
    "rank,suit",
    [
        ("1", "H"),
        ("11", "H"),
        ("d", "H"),
        ("k", "H"),
        ("-2", "H"),
        ("five", "H"),
        ("3", "h"),
        ("4", "X"),
        ("8", "Clubs"),
    ],
)
def test_card_invalid_values(rank, suit):
    with pytest.raises(ValueError):
        Card(rank, suit)


@pytest.mark.parametrize(
    "left,right,expected",
    [
        (Card("3", "H"), Card("5", "C"), True),
        (Card("A", "H"), Card("5", "C"), True),
        (Card("4", "H"), Card("5", "C"), True),
        (Card("5", "H"), Card("5", "C"), False),
        (Card("6", "H"), Card("5", "C"), False),
        (Card("K", "H"), Card("5", "C"), False),
    ],
)
def test_card_less_than(left, right, expected):
    assert (left < right) == expected


@pytest.mark.parametrize("other", [(None), (2), ("KH")])
def test_card_less_than_invalid_type(other):
    with pytest.raises(TypeError):
        Card("5", "C") < other


@pytest.mark.parametrize(
    "left,right,expected",
    [
        (Card("3", "H"), Card("5", "C"), False),
        (Card("A", "H"), Card("5", "C"), False),
        (Card("4", "H"), Card("5", "C"), False),
        (Card("5", "H"), Card("5", "C"), False),
        (Card("6", "H"), Card("5", "C"), True),
        (Card("K", "H"), Card("5", "C"), True),
    ],
)
def test_card_greater_than(left, right, expected):
    assert (left > right) == expected


@pytest.mark.parametrize("other", [(None), (2), ("KH")])
def test_card_greater_than_invalid_type(other):
    with pytest.raises(TypeError):
        Card("5", "C") > other


@pytest.mark.parametrize(
    "left,right,expected",
    [
        (Card("3", "H"), Card("5", "C"), False),
        (Card("A", "H"), Card("5", "C"), False),
        (Card("4", "H"), Card("5", "C"), False),
        (Card("5", "H"), Card("5", "C"), False),
        (Card("6", "H"), Card("5", "C"), False),
        (Card("K", "H"), Card("5", "C"), False),
        (Card("5", "H"), Card("5", "H"), True),
    ],
)
def test_card_equal_to(left, right, expected):
    assert (left == right) == expected


@pytest.mark.parametrize("other", [(None), (2), ("KH")])
def test_card_greater_than_invalid_type(other):
    with pytest.raises(TypeError):
        Card("5", "C") == other


@pytest.mark.parametrize(
    "card,expected",
    [
        (Card("A", "S"), "Ace of Spades"),
        (Card("2", "D"), "Two of Diamonds"),
        (Card("3", "H"), "Three of Hearts"),
        (Card("4", "S"), "Four of Spades"),
        (Card("5", "C"), "Five of Clubs"),
        (Card("6", "C"), "Six of Clubs"),
        (Card("7", "D"), "Seven of Diamonds"),
        (Card("8", "D"), "Eight of Diamonds"),
        (Card("9", "H"), "Nine of Hearts"),
        (Card("10", "C"), "Ten of Clubs"),
        (Card("J", "D"), "Jack of Diamonds"),
        (Card("Q", "C"), "Queen of Clubs"),
        (Card("K", "H"), "King of Hearts"),
    ],
)
def test_card_string_method(card, expected):
    assert str(card) == expected
