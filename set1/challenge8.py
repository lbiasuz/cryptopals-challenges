from Crypto.Cipher import AES

def get_text():
    return open("set1/ch8.txt").read().split("\n")


def break_text(cypher_text):
    return [cypher_text[i : i + 16] for i in range(0, len(cypher_text), 16)]


def count_ocurrances(blocks):
    return [(block, blocks.count(block) - 1) for block in blocks]


def count_equal_blocks(cypher_text):
    return sorted(
        count_ocurrances(break_text(cypher_text)), key=lambda x: x[1], reverse=True
    )[0]

def get_best_resulted_line(result):
    return sorted(result, key=lambda x: x[0][1], reverse=True)[0]


def find_ECB_line():
    result = [
        (count_equal_blocks(bytes.fromhex(get_text()[i])), i)
        for i in range(len(get_text()))
    ]
    return get_best_resulted_line(result)


if __name__ == "__main__":
    print(find_ECB_line())
