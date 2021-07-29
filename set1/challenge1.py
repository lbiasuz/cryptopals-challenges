# strings for encode/decode the type to int
from set1.challenge2 import HEX_DECODE_STR


HEX_DECODE_STR = "0123456789abcdef"
BASE64_ENCODE_STR = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def hex_to_base64(hex_in):
    bits = "".join(
        [
            bin(HEX_DECODE_STR.index(hex_in[i]))[2:].zfill(4)
            for i in range(0, len(hex_in))
        ]
    )
    base64_out = "".join(
        [BASE64_ENCODE_STR[int(bits[i : i + 6], 2)] for i in range(0, len(bits), 6)]
    )
    return base64_out


if __name__ == "__main__":
    import sys

    hex_input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    expected_output = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    assert hex_to_base64(hex_input) == expected_output

    output = hex_to_base64(sys.argv[1])
    print(output)
