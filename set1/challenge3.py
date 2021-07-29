import sys

ETAOIN_SHRDLU = {
    "e": 13,
    "t": 12,
    "a": 11,
    "o": 10,
    "i": 9,
    "n": 8,
    " ": 7,
    "s": 6,
    "h": 5,
    "r": 4,
    "d": 3,
    "l": 2,
    "u": 1,
    # Note: The numbers I chose were completely arbitrary;
    # I don't know, but this method of scoring text looks really naive;
    # But it works, so I'm sticking with it this time;
}


def find_xor_key(input_bytes):
    possible_strings = []
    for i in range(128):
        byte_string = xor_bytes(input_bytes, i)
        score = score_string(byte_string)
        possible_strings.append({"string": byte_string, "char": chr(i), "score": score})
    return get_best_scored_string(possible_strings)


def get_best_scored_string(possible_strings: list):
    return sorted(possible_strings, key=lambda x: x["score"], reverse=True)[0]


def score_string(bytes_string: bytes):
    return sum([ETAOIN_SHRDLU.get(chr(i), 0) for i in bytes_string.lower()])


def xor_bytes(in_bytes: bytes, xor_char: int) -> bytes:
    result = b""
    for byte in in_bytes:
        result += bytes([byte ^ xor_char])
    return result


def test_algorithm():
    input_test = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    expected_result = {
        "string": b"Cooking MC's like a pound of bacon",
        "char": "X",
        "score": 181,
    }
    assert find_xor_key(bytes.fromhex(input_test)) == expected_result


if __name__ == "__main__":
    test_algorithm()

    if len(sys.argv) > 1:
        print(find_xor_key(bytes.fromhex(sys.argv[1])))
    else:
        print("It lacks arguments!")
