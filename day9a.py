def main():
    tally = 0
    grid = []
    while True:
        row = input()
        if not row:
            break
        grid.append([int(i) for i in row])
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            neighbours = []
            if r > 0:
                neighbours.append(grid[r - 1][c])
            if r < len(grid) - 1:
                neighbours.append(grid[r + 1][c])
            if c > 0:
                neighbours.append(grid[r][c - 1])
            if c < len(grid[0]) - 1:
                neighbours.append(grid[r][c + 1])
            if grid[r][c] < min(neighbours):
                tally += grid[r][c] + 1
                print("{},{}".format(r,c))



    print(tally)

    

    
            
if __name__ == "__main__":
    main()