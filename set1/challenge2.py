hex_decode_str = '0123456789abcdef'

def xor_hex_strings(hex_input_string, hex_xor_input_string):
    # iterates through hex_input_string, generates a list of bits and joins them on bit_string;
    bit_string = ''.join(
        [
            bin(hex_decode_str.index(hex_input_string[i]))[2:].zfill(4)
            for i in range(0, len(hex_input_string))
        ]
    )
    # iterates through hex_xor_input_string, generates a list of bits and joins them on bit_xor_string;
    bit_xor_string = ''.join(
        [
            bin(hex_decode_str.index(hex_xor_input_string[i]))[2:].zfill(4)
            for i in range(0, len(hex_xor_input_string))
        ]
    )
    # iterates through bit_string, xoring each bit, for the equivalent index in bit_xor_string,
    # generates a list of bits and joins them on bit_xored_string;
    bit_xored_string = ''.join(
        [
            '0' if bit_string[i] == bit_xor_string[i] else '1'
            for i in range(len(bit_string))
        ]
    )
    # iterates through bit_xored_string, generates a list of converted hex characters and joins them on hex_output_string;
    hex_output_string = ''.join(
        [
            hex_decode_str[int(bit_xored_string[i : i + 4], 2)]
            for i in range(0, len(bit_xored_string), 4)
        ]
    )
    return hex_output_string

if __name__ == "__main__":
    import sys
    print(xor_hex_strings(sys.argv[1], sys.argv[2]))

