import time

def alive(cell):
    return cell == 1


def neibhors(theboard, row, col):
    size_limit = len(theboard) - 1
    alive_members = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            next_row = row + i
            next_col = col + j
            if next_row == row and next_col == col:
                continue
            if next_row < 0 or next_col < 0 or next_row > size_limit or next_col > size_limit:
                continue
            if alive(theboard[next_row][next_col]):
                alive_members += 1

    return alive_members


def rules(theboard, neibhors):
    rows = len(neibhors)
    cols = len(neibhors[0])
    for row in range(rows):
        for col in range(cols):             
            if neibhors[row][col] not in [2,3]:
                theboard[row][col] = 0
                continue
                
            if neibhors[row][col] == 3:
                theboard[row][col] = 1
                continue
    return theboard


def display(theboard):
    size = len(theboard)
    for i in range(size):
        for j in range(size): 
            if alive(theboard[i][j]):
                print("1", end=' ')
            else:
                print("o",end=' ')
        print("\n")



def main(theboard):
    while True:
        print(display(theboard))
        for i in range(10):
            print ("{} generation".format(i))    
            rules(theboard, neibhors(theboard, row, col))


if __name__ == "__main__":
    theboard = [[0,0,0], 
                [1,1,1], 
                [0,0,0]]
    main(theboard)

