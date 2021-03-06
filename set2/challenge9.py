# PKCS#7
def pad_text(text: str, block_size: int): 
    byteArr = bytes(text, 'utf-8')
    blockDif = block_size - len(byteArr)
    byteArr += bytes([blockDif for i in range(blockDif)])
    return byteArr


if __name__ == "__main__":
    import sys
    print(pad_text(sys.argv[1], int(sys.argv[2])))