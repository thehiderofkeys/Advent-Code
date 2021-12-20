import numpy as np


def ingest() -> np.ndarray:
    line = input()
    points = []
    dim_x, dim_y = 0, 0
    while line:
        x, y = [int(num) for num in line.split(",")]
        dim_x = max(x, dim_x)
        dim_y = max(y, dim_y)
        points.append((x, y))
        line = input()
    paper = np.zeros((dim_y + 1, dim_x + 1))
    for x, y in points:
        paper[y, x] = 1
    return paper


def main(paper: np.ndarray):
    line = input()
    direction, pivot = line.split("=")
    pivot = int(pivot)
    if direction.endswith("y"):
        top = paper[:pivot, :]
        bottom = np.flipud(paper[pivot + 1:, :])
        row = np.zeros((1, bottom.shape[1]))
        if top.shape[0] < bottom.shape[0]:
            top = np.vstack((row, top))
        if top.shape[0] > bottom.shape[0]:
            bottom = np.vstack((row,  bottom))
        paper = top + bottom
    if direction.endswith("x"):
        left = paper[:, :pivot]
        right = np.fliplr(paper[:, pivot + 1:])
        col = np.zeros((left.shape[0], 1))
        if left.shape[1] < right.shape[1]:
            left = np.hstack((col, left))
        if left.shape[1] > right.shape[1]:
            right = np.hstack((col, right))
        paper = left + right
    dim_y, dim_x = paper.shape
    count = 0
    for y in range(dim_y):
        for x in range(dim_x):
            count += 1 if paper[y, x] > 0 else 0
    print(count)


if __name__ == "__main__":
    main(ingest())
