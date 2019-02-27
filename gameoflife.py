import time

def alive(cell):
    return cell == 1


def neighbours(theboard):
    n = len(theboard)
    neighbours_count = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # Hardcoding. This will work only for 3x3. It should be written for NxN
    result = (theboard[0][1], theboard[1][0], theboard[1][1]).count(1)
    neighbours_count[0][0] = result
    result = (theboard[0][0], theboard[1][0], theboard[1][1], theboard[1][2], theboard[0][2]).count(1)
    neighbours_count[0][1] = result
    result = (theboard[0][1], theboard[1][1], theboard[1][2]).count(1)
    neighbours_count[0][2] = result
    result = (theboard[0][0], theboard[0][1], theboard[1][1], theboard[2][1], theboard[2][0]).count(1)
    neighbours_count[1][0] = result
    result = (theboard[0][0], theboard[0][1], theboard[0][2], theboard[1][0], theboard[1][2], theboard[2][0],theboard[2][1], theboard[2][2]).count(1)
    neighbours_count[1][1] = result
    result = (theboard[0][2], theboard[0][1], theboard[1][1], theboard[2][1], theboard[2][2]).count(1)
    neighbours_count[1][2] = result
    result = (theboard[1][0], theboard[1][1], theboard[2][1]).count(1)
    neighbours_count[2][0] = result
    result = (theboard[1][2], theboard[1][1], theboard[2][1]).count(1)
    neighbours_count[2][2] = result
    result = (theboard[2][0], theboard[1][0], theboard[1][1], theboard[1][2], theboard[2][2]).count(1)
    neighbours_count[2][1] = result
    return neighbours_count


def rules(theboard, neighbours):
    rows = len(neighbours)
    cols = len(neighbours[0])
    for i in range(rows):
        for j in range(cols):             
            if neighbours[i][j] not in [2,3]:
                theboard[i][j] = 0
                continue
                
            if neighbours[i][j] == 3:
                theboard[i][j] = 1
                continue
    return theboard


def display(theboard):
    rows = []
    for i in range(len(theboard)):
        cols = []
        for j in range(len(theboard)):
            if alive(theboard[i][j]):
                cols.append("o")
            else:
                cols.append(".")
        rows.append("   ".join(cols))
    return "\n\n".join(rows)



def main(theboard):
    for i in range(10):
        print ("{} generation".format(i))
        time.sleep(0.5)
        print(display(theboard))
        rules(theboard, neighbours(theboard))



if __name__ == "__main__":
    theboard = [[0,0,0], 
                [1,1,1], 
                [0,0,0]]
    main(theboard)
    
