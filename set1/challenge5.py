import sys

hex_decode_str = '0123456789abcdef'

def xor_string(string, key):
    while len(string) > len(key):
        key += key
    output = b''
    for c in range(len(string)):
        output += bytes([ord(string[c]) ^ ord(key[c])])
    return output

if __name__ == "__main__":
    arg1 = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    arg2 = "ICE"
    print(bytes.hex(xor_string(arg1, arg2)))
    """
    The actual input has \n in it, and i apparently the terminal swallows it before executing
    the code, I could not find any way to get around this, so I'm sticking to hard code the input
    in this exercice
    """