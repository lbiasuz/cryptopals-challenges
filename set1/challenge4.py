from set1.challenge3 import find_xor_key, get_best_scored_string


def find_encrypted_hex_on_file(file):
    hex_list = [find_xor_key(bytes.fromhex(line)) for line in file]
    return get_best_scored_string(hex_list)


def get_text():
    return open("set1/ch4.txt")


def test_algorithm():
    expected_result = {
        "string": b"Now that the party is jumping\n",
        "char": "5",
        "score": 183,
    }
    assert find_encrypted_hex_on_file(get_text()) == expected_result


if __name__ == "__main__":
    test_algorithm()
    print(find_encrypted_hex_on_file(get_text()))
