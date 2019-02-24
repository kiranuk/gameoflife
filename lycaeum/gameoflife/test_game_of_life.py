import gameoflife


def test_neibhors():
    theboard = [[True,False,False], [False,True,False], [False,False,True]]
    result = [[1, 2, 1], [2, 2, 2], [1, 2, 1]]
    assert (gameoflife.neibhors(theboard) == result)
def test_rules():
    actual = [1,2,1]
    result = [2,2,2]
    assert (gameoflife.rules(theboard,actual) == result for _ in range(3)) 

