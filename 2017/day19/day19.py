import os
from enum import Enum
class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

def main():
    seen = ""
    ws = os.path.dirname(__file__)
    with open(os.path.join(ws, "day19.txt"), 'r') as f:
        lines = [x.rstrip("\r\n") for x in list(f)]
    grid = []
    for line in lines:
        grid.append([x for x in line])
    row = 0
    col = grid[0].index("|")
    current_symbol = grid[row][col]
    direction = Direction.DOWN
    i = 1

    while True:
        i += 1
        # print(current_symbol, row, col)
        if direction == Direction.DOWN:
            row += 1
        elif direction == Direction.UP:
            row -= 1
        elif direction == Direction.LEFT:
            col -= 1
        elif direction == Direction.RIGHT:
            col += 1
        current_symbol = grid[row][col]
        if current_symbol == "+":
            left = grid[row][col - 1] if direction != Direction.RIGHT else None
            right = grid[row][col + 1] if direction != Direction.LEFT else None
            up = grid[row - 1][col] if direction != Direction.DOWN else None
            down = grid[row + 1][col] if direction != Direction.UP else None
            directions = [up, right, down, left]
            directions = [1 if x is not None and x != ' ' else 0 for x in directions]
            try:
                direction = Direction(directions.index(1))
            except ValueError as e:
                print(seen)
                break
        elif current_symbol.isalpha():
            seen += current_symbol
            left = grid[row][col - 1] if direction != Direction.RIGHT else None
            right = grid[row][col + 1] if direction != Direction.LEFT else None
            up = grid[row - 1][col] if direction != Direction.DOWN else None
            down = grid[row + 1][col] if direction != Direction.UP else None
            directions = [up, right, down, left]
            directions = [1 if x is not None and x != ' ' else 0 for x in directions]
            try:
                direction = Direction(directions.index(1))
            except ValueError as e:
                print(seen, i)
                break
    

if __name__ == '__main__':
    main()