import numpy as np

def alive(cell):
    if cell == 1:
        return True
    else:
        return False


def neibhors(theboard):
    neibhors_count = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(theboard)):
        for j in range(len(theboard[0])):
            
            if i == 0:
                if j == 0:
                    result = (theboard[i-1][j], theboard[i][j-1], theboard[i][j]).count(1)
                    neibhors_count[i-1][j-1] = result
                    continue
                if j == 2:
                    result = (theboard[i-1][j], theboard[i][j], theboard[i][j+1]).count(1)
                    neibhors_count[i-1][j+1] = result
                    continue
                if j == 1:
                    result = (theboard[i-1][j-1], theboard[i][j-1], theboard[i][j], theboard[i][j+1], theboard[i-1][j+1]).count(1)
                    neibhors_count[i-1][j] = result
                    continue
            
            if i == 1:
                if j == 0:
                    result = (theboard[i-1][j-1], theboard[i-1][j], theboard[i][j], theboard[i+1][j], theboard[i+1][j-1]).count(1)
                    neibhors_count[i][j-1] = result
                    continue
                if j == 2:
                    result = (theboard[i-1][j+1], theboard[i-1][j], theboard[i][j], theboard[i+1][j], theboard[i+1][j+1]).count(1)
                    neibhors_count[i][j+1] = result
                    continue
                if j == 1:
                    result = (theboard[i-1][j-1], theboard[i-1][j], theboard[i-1][j+1], theboard[i][j-1], theboard[i][j+1], theboard[i+1][j-1],theboard[i+1][j], theboard[i+1][j+1]).count(1)
                    neibhors_count[i][j] = result
                    continue
            
            if i == n:
                if j == 0:
                    result = (theboard[i][j-1], theboard[i][j], theboard[i+1][j]).count(1)
                    neibhors_count[i+1][j-1] = result
                    continue
                if j ==2:
                    result = (theboard[i][j+1], theboard[i][j], theboard[i+1][j]).count(1)
                    neibhors_count[i+1][j+1] = result
                    continue
                if j ==1:
                    result = (theboard[i+1][j-1], theboard[i][j-1], theboard[i][j], theboard[i][j+1], theboard[i+1][j+1]).count(1)
                    neibhors_count[i+1][j+1] = result
                    continue
    return neibhors_count

def rules(theboard, neibhors):
    for i in range(len(theboard)):
        for j in range(len(theboard[0])):
            if alive(theboard[i][j]):
                if neibhors[i][j] < 2:
                    theboard[i][j] = 0
                if neibhors[i][j] in range(2,4):
                    theboard[i][j] = 1
                if neibhors[i][j] > 3:
                    theboard[i][j] = 0
            else:
                if neibhors[i][j] == 3:
                    theboard[i][j] = 1

def display(theboard):
    for i in range(len(theboard)):
        for j in range(len(theboard[0])):
            if alive(theboard[i][j]) == 1:
                print(" o ")
            else:
                print(" . ")        



def main():
    theboard = [[1,0,0],[0,1,0],[0,0,1]]
    display(theboard)
    a = rules(theboard, neibhors(theboard))
    return a


if __name__ == '__main__':
    main()

