import os
from collections import deque
letters = list("abcdefghijklmnop")

def main():
    global letters
    ws = os.path.dirname(__file__)
    with open(os.path.join(ws, "day16.txt"), 'r') as f:
        insns = f.read().split(",")
        insn_parsed = get_insns(insns)
        results = []
        results.append(''.join(letters))
        for i in range(50):
            for insn in insn_parsed:
                insn_type = insn[0]
                if insn_type == 's':
                    letters = spin(insn[1])
                elif insn_type == 'x':
                    exchange(insn[1], insn[2])
                elif insn_type == 'p':
                    partner(insn[1], insn[2])
            res = ''.join(letters)
            if res in results:
                break
            else:
                results.append(res)
    print(results[1])
    print(results[1000000000 % len(results)])
    
def get_insns(insns):
    insn_parsed = []
    for insn in insns:
        name = insn[0]
        if name == 's':
            insn_parsed.append((name, int(insn[1:])))
        elif name == 'x':
            positions = [int(x) for x in insn[1:].split("/")]
            insn_parsed.append((name, positions[0], positions[1]))
        elif name == 'p':
            names = insn[1:].split("/")
            insn_parsed.append((name, names[0], names[1]))
    return insn_parsed

def spin(by):
    global letters
    return letters[-by:] + letters[:-by]

def exchange(a, b):
    global letters
    x = letters[a]
    letters[a] = letters[b]
    letters[b] = x

def partner(a, b):
    global letters
    x = letters.index(a)
    y = letters.index(b)
    exchange(x, y)

if __name__ == '__main__':
    main()