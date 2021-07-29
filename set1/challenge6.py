def main():
    keysize_range: list = list(range(2, 41))
    text: bytes = get_text()
    keysize = find_keysize(keysize_range)
    key = generate_key(keysize)
    output = translate_text(key)
    print(output)


def find_keysize(keysize_range: list) -> int:
    # returns the keysize with the lowest avarage hamming distance on the text
    possible_keysizes = get_avg_dist_list(keysize_range)
    return sorted(possible_keysizes, key=lambda x: x["avg_dist"])[0]["keysize"]


def get_avg_dist_list(keysize_range: list) -> list:
    possible_keysizes = []
    for keysize in keysize_range:
        blocks = break_text(keysize)
        distance_list = get_keysize_hamming_dist_list(blocks)
        possible_keysizes.append(
            {
                "avg_dist": (sum(distance_list) / keysize) / len(distance_list),
                "keysize": keysize,
            }
        )
    return possible_keysizes


def get_best_keysize(possible_keysizes: list) -> int:
    sorted(possible_keysizes, key=lambda x: x["avg_dist"])[0]["keysize"]


def generate_key(keysize: int) -> bytes:
    # Finds the key from transposed text single character xor
    from set1.challenge3 import find_xor_key

    transposed_blocks = transpose_blocks(keysize)

    # generates the key from each transposed block
    key = b""
    for block in transposed_blocks:
        key += bytes([ord(find_xor_key(block)["char"])])
    return key


def translate_text(key: str):
    text = get_text()
    # translates text by repeating key xor with the key found
    while len(text) > len(key):
        key += key
    output = ""
    for i in range(len(text)):
        output += chr(text[i] ^ key[i])
    return output


def transpose_blocks(keysize: int) -> list:
    blocks = break_text(keysize)
    return [bytes([block[i] for block in blocks]) for i in range(keysize)]


def break_text(keysize: int) -> list:
    text = get_text()
    blocks = [text[i : i + keysize] for i in range(0, len(text), keysize)]
    return treat_blocks_size(blocks, keysize)


def treat_blocks_size(blocks: list, keysize: int) -> list:
    # Treatment to not raise index out of bounds later on
    if len(blocks) % 2 != 0:
        blocks.append(bytes(range(2 * keysize)))
    if len(blocks[-1]) < keysize:
        blocks[-1] += bytes(keysize - len(blocks[-1]))
    return blocks


def hamming_dist(byte_str: bytes, byte_str_1: bytes) -> int:
    # Xors two byte strings against eachother and counts the bit difference
    return sum(
        [bin(byte_str[i] ^ byte_str_1[i]).count("1") for i in range(len(byte_str))]
    )


def get_keysize_hamming_dist_list(blocks: list) -> list:
    return [
        hamming_dist(blocks[block], blocks[block + 1])
        for block in range(0, len(blocks), 2)
    ]


def get_text() -> bytes:
    import base64

    return base64.b64decode(open("set1/ch6.txt").read())


if __name__ == "__main__":
    main()
