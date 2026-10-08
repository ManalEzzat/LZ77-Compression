def decode(tokens):
    """Rebuild the original string from a list of (offset, length, next_char) tokens."""
    output = []

    for offset, length, next_char in tokens:
        if offset < 0 or length < 0:
            raise ValueError(f"Invalid token: {(offset, length, next_char)}")

        if length > 0:
            if offset == 0 or offset > len(output):
                raise ValueError(
                    f"Offset {offset} is out of range (output size: {len(output)})"
                )
            start = len(output) - offset
            # Copy one char at a time so overlapping matches (length > offset) work.
            for i in range(length):
                output.append(output[start + i])

        output.append(next_char)

    return "".join(output)
