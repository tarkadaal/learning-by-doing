import pytest
from user_input import UserInput
from hand import Hand


def test_user_input_exists():
    UserInput("5H 6H 7C AC 2D")


@pytest.mark.parametrize(
    "input_text,expected",
    [
        (None, TypeError),
        (12, TypeError),
        ([], TypeError),
        ("AH", ValueError),
        ("AH 2C 4H 3C", ValueError),
        ("Cabbages", ValueError),
        ("bill and teds excellent adventure", ValueError),
        ("AH AH AH AH AH", ValueError),
    ],
)
def test_invalid_user_input(input_text, expected):
    with pytest.raises(expected):
        UserInput(input_text)


def test_user_input_creates_hand():
    result = UserInput("6H 7H 8D 2D QC")
    assert isinstance(result.hand, Hand)
