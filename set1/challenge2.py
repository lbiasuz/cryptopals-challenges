HEX_DECODE_STR = "0123456789abcdef"


def hex_to_bin(hex_in: str) -> str:
    return "".join(
        [
            bin(HEX_DECODE_STR.index(hex_in[i]))[2:].zfill(4)
            for i in range(0, len(hex_in))
        ]
    )


def bin_to_hex(bin_in: str) -> str:
    return "".join(
        [HEX_DECODE_STR[int(bin_in[i : i + 4], 2)] for i in range(0, len(bin_in), 4)]
    )


def xor_bits(bits: str, bits1: str) -> str:
    return "".join(["0" if bits[i] == bits1[i] else "1" for i in range(len(bits))])


def test_algorithm():
    hex_input = "1c0111001f010100061a024b53535009181c"
    hex_input_1 = "686974207468652062756c6c277320657965"
    expected_output = "746865206b696420646f6e277420706c6179"

    assert (
        bin_to_hex(xor_bits(hex_to_bin(hex_input), hex_to_bin(hex_input_1)))
        == expected_output
    )


def main(hex_input: str, hex_input_1: str) -> str:
    bits: str = hex_to_bin(hex_input)
    bits1: str = hex_to_bin(hex_input_1)
    xored_bin: str = xor_bits(bits, bits1)
    return bin_to_hex(xored_bin)


if __name__ == "__main__":
    import sys

    test_algorithm()
    if len(sys.argv) > 2:
        print(main(sys.argv[1], sys.argv[2]))
    else:
        print("It lacks arguments!")
