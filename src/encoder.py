from .window import find_longest_match


def create_token(offset, length, next_char):
    return (offset, length, next_char)


def encode(data, window_size=10, lookahead_size=5):
    tokens = []
    current_position = 0

    while current_position < len(data):

        offset, match_length = find_longest_match(
            data,
            current_position,
            window_size,
            lookahead_size
        )

        if match_length == 0:
            tokens.append(
                create_token(0, 0, data[current_position])
            )
            current_position += 1

        else:
            # Make sure there is a next character for the token
            if current_position + match_length >= len(data):
                match_length = len(data) - current_position - 1

            if match_length == 0:
                tokens.append(
                    create_token(0, 0, data[current_position])
                )
                current_position += 1
                continue

            next_char = data[current_position + match_length]

            tokens.append(
                create_token(offset, match_length, next_char)
            )

            current_position += match_length + 1

    return tokens
