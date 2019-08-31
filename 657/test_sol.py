import sol


def test_total():
    assert sol.Solution2a().judgeCircle("UD") is True
    assert sol.Solution2a().judgeCircle("LL") is False
