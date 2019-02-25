

def alive(cell):
    return cell == 1


def neibhors(theboard):
    n = len(theboard)
    neibhors_count = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(theboard)):
        for j in range(len(theboard[0])):
            
            if i == 0:
                if j == 0:
                    result = (theboard[0][1], theboard[1][0], theboard[1][1]).count(1)
                    neibhors_count[0][0] = result
                    continue
                if j == 1:
                    result = (theboard[0][0], theboard[1][0], theboard[1][1], theboard[1][2], theboard[0][2]).count(1)
                    neibhors_count[0][1] = result
                    continue
                if j == 2:
                    result = (theboard[0][1], theboard[1][1], theboard[1][2]).count(1)
                    neibhors_count[0][2] = result
                    continue


            
            if i == 1:
                if j == 0:
                    result = (theboard[0][0], theboard[0][1], theboard[1][1], theboard[2][1], theboard[2][0]).count(1)
                    neibhors_count[1][0] = result
                    continue
                if j == 1:
                    result = (theboard[0][0], theboard[0][1], theboard[0][2], theboard[1][0], theboard[1][2], theboard[2][0],theboard[2][1], theboard[2][2]).count(1)
                    neibhors_count[1][1] = result
                    continue
                if j == 2:
                    result = (theboard[0][2], theboard[0][1], theboard[1][1], theboard[2][1], theboard[2][2]).count(1)
                    neibhors_count[1][2] = result
                    continue

            
            if i == 2:
                if j == 0:
                    result = (theboard[1][0], theboard[1][1], theboard[2][1]).count(1)
                    neibhors_count[2][0] = result
                    continue
                if j == 2:
                    result = (theboard[1][2], theboard[1][1], theboard[2][1]).count(1)
                    neibhors_count[2][2] = result
                    continue
                if j ==1:
                    result = (theboard[2][0], theboard[1][0], theboard[1][1], theboard[1][2], theboard[2][2]).count(1)
                    neibhors_count[2][1] = result
                    continue
    return neibhors_count

def rules(theboard,neibhors):
    rows = len(theboard)
    cols = len(theboard[0])
    for i in range(rows):
        for j in range(cols):
            
            if alive(theboard[i][j]):
                
                if neibhors[i][j] < 2:
                    theboard[i][j] = 0
                
                if neibhors[i][j] in range(2,4):
                    theboard[i][j] = 1
                
                if neibhors[i][j] > 3:
                    theboard[i][j] = 0
                
                if neibhors[i][j] == 3:
                    theboard[i][j] = 1
    return theboard
def display(theboard):
    s = " "
    for i in range(len(theboard)):
        for j in range(len(theboard)):
            if alive(theboard[i][j]) == 1:
                s = s + " o "
            else:
                s = s + " . "
    return s



def main():
    theboard = [[1,0,0],[0,1,0],[0,0,1]]
    a = rules(theboard, neibhors(theboard))
    display(theboard)
    return a


if __name__ == '__main__':
    main()

