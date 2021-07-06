import sys

hex_decode_str = '0123456789abcdef'
etaoin_shrdlu = {
    'e': 13,
    't': 12,
    'a': 11,
    'o': 10,
    'i': 9,
    'n': 8,
    ' ': 7,
    's': 6,
    'h': 5,
    'r': 4,
    'd': 3,
    'l': 2,
    'u': 1,
} 
""" 
    Note: The numbers I chose were completely arbitrary;
    I don't know, but this method of scoring text looks really naive;
    But it works, so I'm sticking with it this time;
"""
def find_xor_key(input_bytes):
    possible_strings = []
    # loops the ascii table size;
    for i in range(128):
        # xors the bytes from byte_string against a single characher;
        byte_string = xor_bytes(input_bytes, i)
        # scores the string with etaoin;
        score = score_string(byte_string)
        # appends string, score and character of possible xored texts;
        possible_strings.append({'string': byte_string, 'char': chr(i), 'score': score})
    # returns the string with the best score
    return sorted(possible_strings, key=lambda x: x['score'], reverse=True)[0]


def xor_bytes(inputbytes, xor_char):
    result = b''
    for byte in inputbytes:
        result += bytes([byte ^ xor_char])
    return result


def score_string(bytes_string):
    # returns the sum of arbitrary values to score how close character frequency is to english;
    return sum([etaoin_shrdlu.get(chr(i), 0) for i in bytes_string.lower()])


if __name__ == "__main__":
    print(find_xor_key(bytes.fromhex(sys.argv[1])))
