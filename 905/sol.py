from collections import deque


class Solution(object):
    def sortArrayByParity(self, A):
        result_even = []
        result_odd = []

        for item in A:
            if item % 2 == 0:
                result_even.append(item)
            else:
                result_odd.append(item)

        return result_even + result_odd


class Solution2(object):
    def sortArrayByParity(self, A):
        result_even = [item for item in A if item % 2 == 0]
        result_odd = [item for item in A if item % 2 != 0]

        return result_even + result_odd


class Solution3(object):
    def sortArrayByParity(self, A):
        result_even = []
        result_odd = []

        [result_even.append(item) for item in A if item % 2 == 0]
        [result_odd.append(item) for item in A if item % 2 != 0]

        return result_even + result_odd


class Solution4(object):
    def sortArrayByParity(self, A):
        result_even = []
        result_odd = []

        [result_even.append(item) if item % 2 == 0 else result_odd.append(item) for item in A]

        return result_even + result_odd


class Solution5(object):
    def sortArrayByParity(self, A):
        result = deque()

        [result.appendleft(item) if item % 2 == 0 else result.append(item) for item in A]

        return list(result)
