import os
from enum import Enum
class Direction(Enum):
    DONE = -1
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class Maze():

    def __init__(self):
        ws = os.path.dirname(__file__)
        with open(os.path.join(ws, "day19.txt"), 'r') as f:
            lines = [x.rstrip("\r\n") for x in list(f)]
        self.grid = []
        for line in lines:
            self.grid.append([x for x in line])
        self.row = 0
        self.col = self.grid[0].index("|")
        self.update_symbol()
        self.seen = ""
        self.direction = Direction.DOWN
        self.steps = 1

    def move(self):
        if self.direction == Direction.DOWN:
            self.row += 1
        elif self.direction == Direction.UP:
            self.row -= 1
        elif self.direction == Direction.LEFT:
            self.col -= 1
        elif self.direction == Direction.RIGHT:
            self.col += 1
        self.steps += 1

    def update_symbol(self):
        self.current_symbol = self.grid[self.row][self.col]
        if self.current_symbol.isalpha():
            self.seen += self.current_symbol

    def update_direction(self):
        left = self.grid[self.row][self.col - 1] if self.direction != Direction.RIGHT else None
        right = self.grid[self.row][self.col + 1] if self.direction != Direction.LEFT else None
        up = self.grid[self.row - 1][self.col] if self.direction != Direction.DOWN else None
        down = self.grid[self.row + 1][self.col] if self.direction != Direction.UP else None
        directions = [1 if x is not None and x != ' ' else 0 for x in [up, right, down, left]]
        try:
            self.direction = Direction(directions.index(1))
        except ValueError as e:
            self.direction = Direction.DONE

    def zoom(self):
        while self.direction != Direction.DONE:
            self.move()
            self.update_symbol()
            if self.current_symbol == '+' or self.current_symbol.isalpha():
                self.update_direction()
            
        print(self.seen, self.steps)

def main():
    maze = Maze()
    maze.zoom()
    

if __name__ == '__main__':
    main()