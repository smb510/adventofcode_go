import os
from collections import defaultdict

def main():
    registers = defaultdict(int)
    sounds = defaultdict(int)
    ws = os.path.dirname(__file__)
    with open(os.path.join(ws, "day18.txt"), 'r') as f:
        insns = [x.strip().split(" ") for x in list(f)]
        x = 0
        while x >= 0 and x < len(insns):
            insn = insns[x]
            typ = insn[0]
            if typ == 'set':
                val = registers[insn[2]] if insn[2].isalpha() else int(insn[2])
                registers[insn[1]] = val
            elif typ == 'add':
                val = registers[insn[2]] if insn[2].isalpha() else int(insn[2])
                registers[insn[1]] += val
            elif typ == 'mul':
                val = registers[insn[2]] if insn[2].isalpha() else int(insn[2])
                registers[insn[1]] *= val
            elif typ == 'mod':
                val = registers[insn[2]] if insn[2].isalpha() else int(insn[2])
                registers[insn[1]] %= val
            elif typ == 'jgz':
                branch = registers[insn[1]] if insn[1].isalpha() else int(insn[1])
                if branch > 0:
                    val = registers[insn[2]] if insn[2].isalpha() else int(insn[2])
                    x += val
                    continue
            elif typ == 'snd':
                sounds[insn[1]] = registers[insn[1]]
            elif typ == 'rcv':
                if registers[insn[1]] != 0 and sounds[insn[1]] != 0:
                    x = 1000
            x += 1


if __name__ == '__main__':
    main()