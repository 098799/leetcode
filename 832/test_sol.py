from sol import solution
from sol import flip_horizontally
from sol import invert


def test_flip():
    assert flip_horizontally([[1, 0, 0], [0, 1, 1]]) == [[0, 0, 1], [1, 1, 0]]


def test_invert():
    assert invert([[1, 0, 0], [0, 1, 1]]) == [[0, 1, 1], [1, 0, 0]]


def test_solution():
    assert solution([[1,1,0],[1,0,1],[0,0,0]]) == [[1,0,0],[0,1,0],[1,1,1]]
