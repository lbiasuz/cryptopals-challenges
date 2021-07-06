from Crypto.Cipher import AES

def get_text(): return open('set1/ch8.txt').read().split('\n')

def count_equal_blocks(cyphertext):
    blocks = [cyphertext[i:i+16] for i in range(0,len(cyphertext), 16)]
    ocurrances = [(block, blocks.count(block)-1) for block in blocks]
    return sorted(ocurrances, key=lambda x:x[1], reverse=True)[0]

def main():
    result = [(count_equal_blocks(bytes.fromhex(get_text()[i])), i) for i in range(len(get_text()))]
    print(sorted(result, key=lambda x:x[0][1], reverse=True)[0])

if __name__ == "__main__":
    main()