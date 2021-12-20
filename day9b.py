def main():
    grid = []
    flow_grid = []
    basin_coords = []
    while True:
        row = input()
        if not row:
            break
        grid.append([int(i) for i in row])
        flow_grid.append([[] for _ in row])
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            neighbour_values = []
            neighbour_flow = []
            if r > 0:
                neighbour_values.append(grid[r - 1][c])
                neighbour_flow.append(flow_grid[r - 1][c])
            if r < len(grid) - 1:
                neighbour_values.append(grid[r + 1][c])
                neighbour_flow.append(flow_grid[r + 1][c])
            if c > 0:
                neighbour_values.append(grid[r][c - 1])
                neighbour_flow.append(flow_grid[r][c - 1])
            if c < len(grid[0]) - 1:
                neighbour_values.append(grid[r][c + 1])
                neighbour_flow.append(flow_grid[r][c + 1])
            min_neighbour = min(neighbour_values)
            if grid[r][c] < min_neighbour:
                basin_coords.append((r, c))
            elif grid[r][c] != 9:
                min_index = neighbour_values.index(min_neighbour)
                neighbour_flow[min_index].append((r, c))
    print(len(basin_coords))
    basin_sizes = [basin_count(r, c, flow_grid) + 1 for r, c in basin_coords]
    for (r, c), size in zip(basin_coords, basin_sizes):
        print("{},{} size: {}".format(r, c, size))
    basin_sizes.sort()
    print(basin_sizes[-3:])


def basin_count(r, c, flow_map: list[list[tuple]]) -> int:
    total = 0
    for n_r, n_c in flow_map[r][c]:
        total += 1 + basin_count(n_r, n_c, flow_map)
    return total


if __name__ == "__main__":
    main()
