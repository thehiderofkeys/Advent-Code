import heapq


def ingest() -> list[list[int]]:
    line = input()
    grid = []
    while line:
        row = []
        for char in line:
            row.append(int(char))
        grid.append(row)
        line = input()
    return grid


def main(grid: list[list[int]]):
    heap = []
    heapq.heappush(heap, (0, 0, 0))
    h = len(grid)
    w = len(grid[0])
    goal = (h - 1, w - 1)
    visited = [[0]*w for _ in range(h)]
    while True:
        d, r, c = heapq.heappop(heap)
        if (r, c) == goal:
            print(d)
            return
        visited[r][c] = 1
        if r > 0 and visited[r - 1][c] == 0:
            new_d = d + grid[r - 1][c]
            heapq.heappush(heap, (new_d, r - 1, c))
        if r < h - 1 and visited[r + 1][c] == 0:
            new_d = d + grid[r + 1][c]
            heapq.heappush(heap, (new_d, r + 1, c))
        if c > 0 and visited[r][c - 1] == 0:
            new_d = d + grid[r][c - 1]
            heapq.heappush(heap, (new_d, r, c - 1))
        if c < w - 1 and visited[r][c + 1] == 0:
            new_d = d + grid[r][c + 1]
            heapq.heappush(heap, (new_d, r, c + 1))


if __name__ == "__main__":
    main(ingest())
