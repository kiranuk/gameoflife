import gameoflife

def test_alive():
    theboard = [[1,0,0],[0,1,0],[0,0,1]]
    assert (gameoflife.alive(theboard, 0, 0) == True)
    assert (gameoflife.alive(theboard, 1, 1) == True)
def test_neibhors():
    theboard = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    result = [[1, 2, 1], [2, 2, 2], [1, 2, 1]]
    assert (gameoflife.neibhors(theboard, 3) == result for _ in range(len(theboard)))
def test_rules():
    actual = [1,2,1]
    result = [2,2,2]
    assert (gameoflife.rules(theboard,actual) == result for _ in range(3)) 

