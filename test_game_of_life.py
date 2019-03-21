import gameoflife

def test_alive():
    theboard = [[1,0,0],
                [0,1,0],
                [0,0,1]]
    result = [[True,False,False],
              [False,True,False],
              [False,False,True]]
    assert (gameoflife.alive(theboard[0][0]) == result[0][0])
    assert (gameoflife.alive(theboard[1][0]) == result[1][0])
    assert (gameoflife.alive(theboard[2][0]) == result[2][0])
    assert (gameoflife.alive(theboard[1][1]) == result[1][1])
    assert (gameoflife.alive(theboard[2][1]) == result[2][1])



def test_neibhours():
    theboard = [[0, 0, 0],
                [1, 1, 1],
                [0, 0, 0]]
    result = 0
    assert (gameoflife.neibhours(theboard, 3, 3) == result)

def test_rules():
    theboard = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
    result = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    assert (gameoflife.rules(theboard) == result) 

