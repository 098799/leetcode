import sol


def test_total():
    assert sol.Solution().repeatedNTimes([1, 2, 3, 3]) == 3
    assert sol.Solution().repeatedNTimes([2, 1, 2, 5, 3, 2]) == 2
    assert sol.Solution().repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]) == 5
