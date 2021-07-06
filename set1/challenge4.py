import sys
from set1 import challenge3

hex_decode_str = '0123456789abcdef'

def find_encrypted_hex():
    """ Iterates through a file of hex encoded strings, xors them against every
        ascii char, scores every xored string and returns the best scored one; """
    file = open('set1/ch4.txt')
    xoredlist = [challenge3.find_xor_key(bytes.fromhex(h)) for h in file]
    return sorted(xoredlist, key=lambda x: x['score'], reverse=True)[0]

if __name__ == "__main__":
    print(find_encrypted_hex())