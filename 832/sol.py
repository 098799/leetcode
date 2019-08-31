def flip_horizontally(matrix):
    return [column[::-1] for column in matrix]


def invert(matrix):
    return [[(number + 1) % 2 for number in column] for column in matrix]


def flip_and_invert(matrix):
    return [[(number + 1) % 2 for number in column][::-1] for column in matrix]


def solution(matrix):
    return invert(flip_horizontally(matrix))
