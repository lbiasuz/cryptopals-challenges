# strings for encode/decode the type to int
hex_decode_str = '0123456789abcdef'
base64_encode_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


def hex_to_base64(hex_input_string):
    #11-16: iterates through hex_input_string, generates a list of bits and joins them on bit_string;
    bit_string = ''.join(
        [
            bin(hex_decode_str.index(hex_input_string[i]))[2:].zfill(4)
            for i in range(0, len(hex_input_string))
        ]
    )
    #18-23: iterates through bit_string, generates a list of characters and joins them on base_output;
    base64_output_string = ''.join(
        [
            base64_encode_str[int(bit_string[i : i + 6], 2)]
            for i in range(0, len(bit_string), 6)
        ]
    )
    return base64_output_string


if __name__ == "__main__":
    import sys
    print(hex_to_base64(sys.argv[1]))
