import pytest

from src.decoder import decode
from src.encoder import encode


def test_decode_empty():
    assert decode([]) == ""


def test_decode_literals_only():
    assert decode([(0, 0, "a"), (0, 0, "b"), (0, 0, "c")]) == "abc"


def test_decode_with_back_reference():
    tokens = [(0, 0, "a"), (0, 0, "b"), (0, 0, "c"), (3, 3, "x")]
    assert decode(tokens) == "abcabcx"


def test_decode_overlapping_match():
    # offset 1, length 3 -> copies 'a' three times (self-overlap)
    assert decode([(0, 0, "a"), (1, 3, "b")]) == "aaaab"


def test_decode_returns_string():
    assert isinstance(decode([(0, 0, "a")]), str)


def test_decode_invalid_offset_too_large():
    with pytest.raises(ValueError):
        decode([(0, 0, "a"), (5, 2, "b")])


def test_decode_invalid_zero_offset_with_length():
    with pytest.raises(ValueError):
        decode([(0, 0, "a"), (0, 2, "b")])


@pytest.mark.parametrize("text", [
    "",
    "a",
    "abc",
    "aaaaa",
    "abcabcabc",
    "abracadabra abracadabra",
    "the quick brown fox jumps over the lazy dog the quick brown fox",
    "اللغة العربية اللغة العربية",
])
@pytest.mark.parametrize("window,lookahead", [(10, 5), (4, 3), (32, 8)])
def test_round_trip(text, window, lookahead):
    assert decode(encode(text, window, lookahead)) == text
