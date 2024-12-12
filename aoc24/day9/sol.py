def parse(path: str) -> list[str]:
    with open(path) as f:
        seq = f.readline().strip()
        ret = []
        for i in range(len(seq)):
            if i % 2 == 0:
                ret.extend(list([str(i // 2)] * int(seq[i])))
            else:
                ret += list("." * int(seq[i]))
        return ret


def swap(blocks: str) -> list[str]:
    i, j = 0, len(blocks) - 1

    while i < j:
        if blocks[i] != ".":
            i += 1
        elif blocks[j] == ".":
            j -= 1
        else:
            blocks[i], blocks[j] = blocks[j], blocks[i]
            i += 1
            j -= 1

    return blocks


def solve(path: str) -> int:
    blocks = parse(path)
    partitioned_blocks = swap(blocks)
    return sum(
        [i * int(partitioned_blocks[i]) for i in range(partitioned_blocks.index("."))]
    )
