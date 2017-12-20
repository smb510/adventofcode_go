import os
from collections import Counter

def main():
    ws = os.path.dirname(__file__)
    lines = []
    with open(os.path.join(ws, "day20.txt"), 'r') as f:
        lines = [parse_line(x.strip()) for x in list(f)]
    min_index = -1
    print(len(lines))
    for y in range(100): 
        distances = [manhattan(line) for line in lines]
        positions = [position(line) for line in lines]
        c = Counter(positions)
        # print(c)
        new_lines = []
        for j in range(len(positions)):
            if c[positions[j]] == 1:
                new_lines.append(lines[j])
            else:
                print("removing ", positions[j])
        lines = new_lines
        for line in lines:
            update(line) 
        print(len(lines))

        

def parse_line(line):
    parsed = line.split(", ")
    p = [int(x) for x in parsed[0][3:len(parsed[0]) - 1].split(",")]
    v = [int(x) for x in parsed[1][3:len(parsed[1]) - 1].split(",")]
    a = [int(x) for x in parsed[2][3:len(parsed[2]) - 1].split(",")]
    return [list(x) for x in zip(p, v, a)]

def manhattan(particle):
   return sum([abs(y) for y in [x[0] for x in particle]])

def position(particle):
    return tuple([y for y in [x[0] for x in particle]])

def update(particle):
    for part in particle:
        part[1] += part[2]
    # print(particle)
    for part in particle:
        part[0] += part[1]


if __name__ == '__main__':
    main()