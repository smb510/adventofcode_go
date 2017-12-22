import os

def main():
    padding = 200
    dimension = 25
    row = (dimension + padding * 2) // 2
    col = (dimension + padding * 2) // 2
    direction = 0
    infections = 0
    grid = []
    for i in range(padding):
        grid.append([x for x in '.' * (dimension + padding * 2)])
    ws = os.path.dirname(__file__)
    with open(os.path.join(ws, "day22.txt"), 'r') as f:
        for line in f.readlines():
            grid.append([x for x in '.' * padding] + [x for x in line.strip()] + [x for x in '.' * padding])
    for i in range(padding):
        grid.append([x for x in '.' * (dimension + padding * 2)])
    for i in range(10000000):
        curr = grid[row][col]
        if curr == '#':
            direction += 1
            direction %= 4
            grid[row][col] = 'F'
        elif curr == '.':
            print("Weakened")
            direction += 3
            direction %= 4
            grid[row][col] = 'W'
        elif curr == 'F':
            grid[row][col] = '.'
            direction += 2
            direction %= 4
        elif curr == 'W':
            grid[row][col] = '#'
            infections += 1

        if direction == 0: # up
            row -= 1
        elif direction == 1: #left
            col += 1
        elif direction == 2: #down
            row += 1
        elif direction == 3: # right
            col -= 1
    print(infections)




    
if __name__ == '__main__':
    main()