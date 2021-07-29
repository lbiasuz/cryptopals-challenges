def repeated_xor(text:bytes, key:bytes) -> bytes:
    key = resize_key(key, len(text))
    output = b""
    for c in range(len(text)):
        output += bytes([text[c] ^ key[c]])
    return output


def resize_key(key: bytes, size:int) -> str:
    while size > len(key):
        key += key
    return key


if __name__ == "__main__":
    text = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = b"ICE"
    expected_output = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    output = bytes.hex(repeated_xor(text, key))
    assert output == expected_output
    print(output)

    """
    The actual input has \n in it, and i apparently the terminal swallows it before executing
    the code, I could not find any way to get around this, so I'm sticking to hard code the input
    in this exercice
    """
