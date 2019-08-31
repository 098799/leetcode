import sol


def test_total():
    assert sol.Solution5().sortArrayByParity([3, 1, 2, 4]) == [4, 2, 3, 1]
