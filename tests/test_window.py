from src.window import find_longest_match
from src.windo import find_longest_match as legacy_find_longest_match


def test_find_longest_match_returns_zero_when_no_match():
    assert find_longest_match("abcde", 3, 3, 3) == (0, 0)
    assert legacy_find_longest_match("abcde", 3, 3, 3) == (0, 0)


def test_find_longest_match_finds_longest_match_in_window():
    data = "abcabcx"
    assert find_longest_match(data, 3, 10, 4) == (3, 3)


def test_find_longest_match_allows_self_overlap():
    data = "aaaaa"
    assert find_longest_match(data, 2, 10, 3) == (1, 3)
