def main():
    draw = [int(call) for call in input().split(',')]
    max_index = None
    winner_score = None
    try:
        while True:
            input()
            score, index = bingo_board(draw)
            if max_index is None or index > max_index:
                max_index = index
                winner_score = score
    except:
        last_number = draw[max_index]
        print(winner_score)
        print(last_number)


def bingo_board(draw):
    board = [0] * len(draw)
    last_index_rows = [0] * 5
    last_index_cols = [0] * 5
    for row_index in range(5):
        row = [int(call) for call in input().split(' ') if call]
        for col_index in range(5):
            number = row[col_index]
            index = draw.index(number)
            board[index] = number
            if last_index_rows[row_index] < index:
                last_index_rows[row_index] = index
            if last_index_cols[col_index] < index:
                last_index_cols[col_index] = index
    win_index = min(min(last_index_rows), min(last_index_cols))
    score = sum(board) - sum(board[:win_index + 1])
    return score, win_index


if __name__ == "__main__":
    main()
