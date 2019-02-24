import numpy as np

def alive(theboard, row, col):
    for row in range(len(theboard)):
        for col in range(len(theboard[0])):
            if theboard[row][col] == 1:
                return True
            else:
                return False


def neibhors(theboard,n=3):
    neibhors_count = np.zeros(n*n,dtype=int).reshape(n,n)
    for i in range(len(theboard)):
        for j in range(len(theboard[0])):
            
            if i == 0:
                if j == 0:
                    result = (theboard[i-1][j], theboard[i][j-1], theboard[i][j]).count(1)
                    neibhors_count[i-1][j-1] = result
                    continue
                if j == n:
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
                if j == n:
                    result = (theboard[i-1][j+1], theboard[i-1][j], theboard[i][j], theboard[i+1][j], theboard[i+1][j+1]).count(1)
                    neibhors_count[i][j+1] = result
                    continue
                else:
                    result = (theboard[i-1][j-1], theboard[i-1][j], theboard[i-1][j+1], theboard[i][j-1], theboard[i][j+1], theboard[i][j-1],theboard[i+1][j], theboard[i+1][j+1]).count(1)
                    neibhors_count[i][j] = result
                    continue
            
            if i == n:
                if j == 0:
                    result = (theboard[i][j-1], theboard[i][j], theboard[i+1][j]).count(1)
                    neibhors_count[i+1][j-1] = result
                    continue
                if j ==n:
                    result = (theboard[i][j+1], theboard[i][j], theboard[i+1][j]).count(1)
                    neibhors_count[i+1][j+1] = result
                    continue
                else:
                    result = (theboard[i+1][j-1], theboard[i][j-1], theboard[i][j], theboard[i][j+1], theboard[i+1][j+1]).count(1)
                    neibhors_count[i+1][j+1] = result
                    continue
        return neibhors_count

def rules(theboard, neibhors_count, cell):
    for i in range(len(neibhors_count)):
        for j in range(len(neibhors_count[0])):
            if neibhors_count[i][j] < 2:
                theboard[i][j] = 0

            if neibhors_count[i][j] in range(2,4):
                theboard[i][j] = 1

            if neibhors_count[i][j] > 3:
                theboard[i][j] = 0

            if neibhors_count[i][j] == 3:
                theboard[i][j] = 1

def display(theboard):
    if theboard[i][j] == 1:
        print('o',end='')
    else:
        print('.',end='')



def main():
    theboard = np.random.randint(2,size=(3, 3))
    print(theboard)
    print(neibhors(theboard))
    display(theboard)
    rules(theboard, neibhors_count, cell)


if __name__ == '__main__':
    main()

