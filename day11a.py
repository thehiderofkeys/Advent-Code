def ingest() -> list[list[int]]:
    grid = []
    line = input()
    while line:
        grid.append([int(char) for char in line])
        line = input()
    return grid

def print_grid(grid: list[list[int]]):
    for row in grid:
        print("".join([str(char) for char in row]))

def flash(r, c, grid):
    for n_r, n_c in [(r+1,c-1), (r+1,c), (r+1,c+1), (r,c+1), (r-1,c+1), (r-1,c), (r-1,c-1), (r,c-1)]:
        if 0 <= n_r <= 9 and  0 <= n_c <= 9:
            grid[n_r][n_c] += 1
            if grid[n_r][n_c] == 10:
                flash(n_r, n_c, grid)

def main(grid: list[list[int]]):
    flashes = 0
    for iter in range(100):
        for r in range(10):
            for c in range(10):
                grid[r][c] += 1
                if grid[r][c] == 10:
                    flash(r, c, grid)
                    
        for r in range(10):
            for c in range(10):
                if grid[r][c] > 9:
                    flashes += 1
                    grid[r][c] = 0
        continue
    print(flashes)
    return

if __name__ == "__main__":
    main(ingest())