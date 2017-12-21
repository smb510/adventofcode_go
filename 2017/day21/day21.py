import os
from math import sqrt

def main():
    rules = {}
    start = (".#.", "..#", "###")
    ws = os.path.dirname(__file__)
    lines = []
    with open(os.path.join(ws, "day21.txt"), 'r') as f:
        lines = [x.strip() for x in list(f)]
    for line in lines:
        parse(line, rules)

    for i in range(18):
        start = subdivide(start)
        next_block = [get_expansion(block, rules) for block in start]
        start = fuse(next_block)
        if i == 4:
            print("Part 1:", sum([len([i for i in x if i == '#']) for x in start]))


    print("Part 2:", sum([len([i for i in x if i == '#']) for x in start]))


def rotate(block):
    return tuple([''.join(y) for y in list(list(x)[::-1] for x in zip(*block))])


def flipx(block):
    return tuple([x[::-1] for x in block])


def parse(line, rules):
    splits = [x.strip() for x in line.split("=>")]
    inputs = splits[0].split("/")
    outputs = splits[1].split("/")
    rules[tuple(inputs)] = tuple(outputs)


def fuse(block):
    size = int(sqrt(len(block)))
    fused = ''
    for i in range(len(block) // size):
        row = block[i * size:i * size + size]
        for j in zip(*row):
            fused += ''.join(j)
    side = int(sqrt(len(fused)))
    sliced = []
    for i in range(side):
        sliced.append(fused[side * i: side * i + side])
    return tuple(sliced)


def get_expansion(block, rules):
    for i in range(4):
        if block in rules:
            return rules[block]
        elif flipx(block) in rules:
            return rules[flipx(block)]
        else:
            block = rotate(block)
            i += 1


def subdivide(block):
    blocks = 1
    s = 1
    if len(block) % 2 == 0:
        blocks = len(block) // 2
        s = 2
    else:
        blocks = len(block) // 3
        s = 3
    if blocks == 1:
        return [block]
    divisions = []
    for row in range(blocks):
        for col in range(blocks):
            divisions.append([x[col * s:col * s + s]
                              for x in block[row * s:row * s + s]])
    return [tuple(t) for t in divisions]


if __name__ == '__main__':
    main()
