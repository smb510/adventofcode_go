import os

def main():
    score = 0
    group_counter = 0
    in_garbage = False
    garbage_count = 0
    ws = os.path.dirname(__file__)
    with open(os.path.join(ws, "day9.txt"), 'r') as f:
        inp = f.read()
        i = 0
        while i < len(inp):
            curr = inp[i]
            if curr == '{':
                if not in_garbage:
                    group_counter += 1
                else:
                    garbage_count += 1
            elif curr == '}':
                if not in_garbage:
                    score += group_counter
                    group_counter -= 1
                else:
                    garbage_count += 1
            elif curr == '<':
                if in_garbage:
                    garbage_count += 1
                else:
                    in_garbage = True
            elif curr == '>':
                in_garbage = False
            elif curr == '!':
                i += 1
            else:
                if in_garbage:
                    garbage_count += 1
            i += 1
    print("Part 1:", score)
    print("Part 2:", garbage_count)

if __name__ == '__main__':
    main()