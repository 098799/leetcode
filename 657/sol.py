from collections import Counter


class Solution(object):
    def judgeCircle(self, moves):

        px = 0
        py = 0

        def make_move(move, position_x, position_y):
            if move == "U":
                position_x += 1
            elif move == "D":
                position_x -= 1
            elif move == "L":
                position_y -= 1
            else:
                position_y += 1

            return position_x, position_y

        for move in moves:
            px, py = make_move(move, px, py)

        if px == py == 0:
            return True

        return False


class Solution2(object):
    def judgeCircle(self, moves):

        px = 0
        py = 0

        for move in moves:
            if move == "U":
                px += 1
            elif move == "D":
                px -= 1
            elif move == "L":
                py -= 1
            else:
                py += 1

        if px == py == 0:
            return True

        return False


class Solution2a(object):
    def judgeCircle(self, moves):

        px = py = 0

        for move in moves:
            if move == "U":
                px += 1
            elif move == "D":
                px -= 1
            elif move == "L":
                py -= 1
            else:
                py += 1

        return px == py == 0


class Solution3(object):
    def judgeCircle(self, moves):
        counter = Counter(moves)

        if counter["U"] == counter["D"] and counter["L"] == counter["R"]:
            return True

        return False


class Solution4(object):
    def judgeCircle(self, moves):
        counter = {"U": 0, "L": 0}

        for move in moves:
            if move in counter:
                counter[move] += 1
            elif move == "D":
                counter["U"] -= 1
            elif move == "R":
                counter["L"] -= 1

        if counter["U"] == counter["L"] == 0:
            return True

        return False
