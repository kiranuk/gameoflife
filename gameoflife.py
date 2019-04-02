
import time


def alive(cell):
    return cell == 1


def neibhours(theboard, row, col):
    board_size = len(theboard) - 1
    alive_members = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            next_row = row + i
            next_col = col + j
            if next_row == row and next_col == col:
                continue
            if next_row < 0 or next_col < 0 or next_row > board_size or next_col > board_size:
                continue
            if theboard[next_row][next_col] == 1:
                alive_members += 1
    return alive_members


def rules(theboard):
    new_board = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]
    rows = len(theboard)
    cols = len(theboard)
    for row in range(rows):
        for col in range(cols):
            if neibhours(theboard, row, col) in [2,3] and theboard[row][col] == 1:
                new_board[row][col] = 1
            elif neibhours(theboard, row, col) == 3 and theboard[row][col] == 0:
                new_board[row][col] = 1
            else:
                new_board[row][col] = 0
    return new_board


def display(theboard):
    size = len(theboard)
    rows = []
    for i in range(size):
        cols = []
        for j in range(size):
            if theboard[i][j] == 1:
                cols.append(u"\u25B2")
            else:
                cols.append(u"\u25E6")
        rows.append(" ".join(cols))
    return "\n\n".join(rows)


def main(theboard):
    row = len(theboard)
    col = len(theboard)
    for i in range(0, 10):
        print("{} generation".format(i))
        print(display(theboard))
        theboard = rules(theboard)
        time.sleep(0.5)


if __name__ == "__main__":
    theboard = [[0, 0, 0],
                [1, 1, 1],
                [0, 0, 0]]

    main(theboard)
