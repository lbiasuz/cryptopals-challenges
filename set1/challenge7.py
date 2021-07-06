# %% 
from Crypto.Cipher import AES
from base64 import b64decode


key = b'YELLOW SUBMARINE'

def get_text():
    return b64decode(open('set1/ch7.txt').read())

def decode_AES(text:bytes, key:bytes):
    aes = AES.new(key, AES.MODE_ECB)
    return aes.decrypt(text)

def main():
    cypher_text = get_text()
    text = decode_AES(cypher_text, key)
    print(text.decode('utf-8'))

if __name__ == "__main__":
    main()