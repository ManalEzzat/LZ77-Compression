from src.encoder import encode
from src.decoder import decode


def read_positive_int(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Please enter a positive whole number.")


def read_text(prompt):
    while True:
        text = input(prompt)
        if text:
            return text
        print("Text cannot be empty.")


def main():
    window_size = read_positive_int("Enter Search Window Size: ")
    lookahead_size = read_positive_int("Enter Look-ahead Buffer Size: ")
    text = read_text("Enter text: ")

    tokens = encode(text, window_size, lookahead_size)
    decoded = decode(tokens)

    print("\nTokens (offset, length, next_char):")
    for token in tokens:
        print("  ", token)
    print("\nDecoded  :", decoded)
    print("Lossless :", decoded == text)


if __name__ == "__main__":
    main()
