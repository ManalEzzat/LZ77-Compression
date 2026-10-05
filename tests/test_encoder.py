from src.encoder import create_token, encode


def test_create_token():
    assert create_token(3, 2, "A") == (3, 2, "A")


def test_encode_no_match():
    result = encode("abc", window_size=10, lookahead_size=3)

    assert result == [
        (0, 0, "a"),
        (0, 0, "b"),
        (0, 0, "c")
    ]


def test_encode_returns_list():
    result = encode("abc", window_size=10, lookahead_size=3)

    assert isinstance(result, list)


def test_encode_repetitive():
    result = encode("aaaaa", window_size=10, lookahead_size=3)

    assert len(result) > 0
    assert all(len(token) == 3 for token in result)
