def get_text() -> bytes:
    import base64

    return base64.b64decode(open('set1/ch6.txt').read())


def break_text(text: bytes, keysize: int) -> list:
    # Iterates through text and returns a list of bytes of KEYSIZE lenght
    blocks = [text[i : i + keysize] for i in range(0, len(text), keysize)]
    # Below is treatment to not raise index out of bounds later on
    if len(blocks) % 2 != 0:
        blocks.append(bytes([0 for i in range(2 * keysize)]))
    if len(blocks[-1]) < keysize:
        blocks[-1] += bytes(keysize - len(blocks[-1]))
    return blocks


def transpose_text(text: bytes, keysize: int) -> list:
    # Iterates through broken text and transposes it
    blocks = break_text(text, keysize)
    return [bytes([block[i] for block in blocks]) for i in range(keysize)]


def hamming_dist(byte_str: bytes, byte_str_1: bytes) -> int:
    # Xors two byte strings against eachother and counts the bit (hammning) difference
    return sum(
        [bin(byte_str[i] ^ byte_str_1[i]).count('1') for i in range(len(byte_str))]
    )


def find_keysize(text: bytes, keysize_range: list) -> int:
    # returns the keysize with the lowest avarage hamming distance on the text
    possible_keysizes: list = []

    for keysize in keysize_range:
        blocks = break_text(text, keysize)

        # appends the distance of each pair of blocks of keysize lenght and normalizes it
        distances = [
            hamming_dist(blocks[i], blocks[i + 1]) / keysize
            for i in range(0, len(blocks), 2)
        ]

        # appends the avarage distance of each keysize
        possible_keysizes.append(
            {
                'avg_dist': sum(distances) / len(distances),
                'keysize': keysize,
            }
        )
    return sorted(possible_keysizes, key=lambda x: x['avg_dist'])[0]['keysize']


def find_key(text: bytes, keysize: int) -> bytes:
    #Finds the key from transposed text single character xor
    from set1.challenge3 import find_xor_key

    transposed_blocks = transpose_text(text, keysize)
    
    #generates the key from each transposed block
    key = b""
    for block in transposed_blocks:
        key += bytes([ord(find_xor_key(block)['char'])])
    return key


def translate_text(text: bytes, key: str):
    #translates text by repeating key xor with the key found
    while len(text) > len(key):
        key += key
    output = ''
    for i in range(len(text)):
        output += chr(text[i] ^ key[i])
    return output


def main():
    keysize_range: list = list(range(2, 41))
    text: bytes = get_text()
    keysize: int = find_keysize(text, keysize_range)
    key = find_key(text, keysize)
    output = translate_text(text, key)
    print(output)

if __name__ == "__main__":
    main()