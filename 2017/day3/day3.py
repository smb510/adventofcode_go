def main():
    grid = [[0 for i in range(11)] for j in range(11)]
    # print grid
    grid[5][5] = 1
    spiral(9, 9, grid)
    for line in grid:
        print line


def get_number_at(x, y, grid):
    middle = 5
    return grid[middle + x][middle + y]


def set_number_at(x, y, grid, val):
    middle = 5
    grid[middle + x][middle + y] = val
    if val > 277678:
        print "Aha!", val


def sum_surrounding(x, y, grid):
    middle = 5
    s = 0
    for i in range(middle + x - 1, middle + x + 2):
        for j in range(middle + y - 1, middle + y + 2):
            s += grid[i][j]
    return s


def spiral(X, Y, grid):
    x = y = 0
    k = 1
    dx = 0
    dy = -1
    for i in range(max(X, Y)**2):
        if (-X / 2 < x <= X / 2) and (-Y / 2 < y <= Y / 2):
            if x != 0 or y != 0:
                set_number_at(x, y, grid, sum_surrounding(x, y, grid))
            
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = (-1 * dy), dx
        x, y = x+dx, y+dy

if __name__ == '__main__':
    main()
