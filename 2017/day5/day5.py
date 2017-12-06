import os

def main():
    ws = os.path.dirname(__file__)
    with open(os.path.join(ws, "day5.txt"), 'r') as f:
        quotients = []
        lines = [int(x.strip()) for x in list(f)]
        pointer = 0
        counter = 0
        while pointer < len(lines):
            pointer = visit(pointer, lines)
            counter += 1

    print counter


def visit(pointer, lines):
    jmp = lines[pointer]
    if jmp >= 3:
        lines[pointer] -= 1
    else:
        lines[pointer] += 1
    pointer += jmp
    return pointer

if __name__ == '__main__':
    main()