from set1.challenge5 import repeated_xor
from Crypto.Cipher import AES

BLOCK_SIZE = AES.block_size = 16
KEY = "YELLOW SUBMARINE"


def string_to_bytes(text: str):
    return bytes(text, "utf-8")


def get_IV():
    return bytes(BLOCK_SIZE)


def get_text():
    return "The quick brown fox jumps over the lazy dog"


def encrypt_ECB(text: bytes, key: bytes):
    aes = AES.new(key, AES.MODE_ECB)
    return aes.encrypt(text)


def break_text(text: bytes) -> list:
    return [text[i : i + BLOCK_SIZE] for i in range(0, len(text), BLOCK_SIZE)]


def pad_text(blocks: list):
    size_dif = BLOCK_SIZE - len(blocks[-1])
    blocks[-1] += bytes([size_dif for i in range(size_dif)])
    return blocks


def encrypt_CBC(text: str, key: str):
    blocks = pad_text(break_text(string_to_bytes(text)))
    key = bytes(key, "utf-8")
    ouput = b""
    for i in range(len(blocks)):
        if i == 0:
            iv = get_IV()
        iv = encrypt_ECB(repeated_xor(blocks[i], iv), key)
        ouput += iv
    return ouput


def decrypt_CBC(text, key):
    key = bytes(key, "utf-8")
    cbc = AES.new(key, AES.MODE_CBC, iv=get_IV())
    return cbc.decrypt(text)


if __name__ == "__main__":
    output = encrypt_CBC(get_text(), KEY)
    print(decrypt_CBC(output, KEY)==output)
    print(output)
