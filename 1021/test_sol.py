from sol import solve


def test_solve():
    assert solve("(()())(())") == "()()()"


def test_solve_2():
    assert solve("(()())(())(()(()))") == "()()()()(())"


def test_solve_3():
    assert solve("()()") == ""
