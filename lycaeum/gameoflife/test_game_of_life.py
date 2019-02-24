import gameoflife

def test_alive():
    theboard = [[1,0,0],[0,1,0],[0,0,1]]
    result = [[True,False,False],[False,True,False],[False],[False],[True]]

    assert (gameoflife.alive(theboard) == result for _ in range(len(theboard)))
def test_neibhors():
    theboard = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    result = [[1, 2, 1], [2, 2, 2], [1, 2, 1]]
    assert (gameoflife.neibhors(theboard, 3) == result for _ in range(len(theboard)))
def test_rules():
    theboard = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    actual = [[1, 2, 1], [2, 2, 2], [1, 2, 1]]
    result = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    assert (gameoflife.rules(theboard,actual) == result for _ in range(len(theboard))) 

