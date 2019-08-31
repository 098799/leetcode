class Solution(object):
    def repeatedNTimes(self, A):
        helper_set = set()

        current_length = 0

        for i in A:
            helper_set.add(i)

            future_length = len(helper_set)

            if future_length == current_length:
                return i

            current_length = future_length


class Solution2(object):
    def repeatedNTimes(self, A):
        helper_dict = {}

        for i in A:
            if helper_dict.get(i):
                return i

            helper_dict[i] = True


class Solution3(object):
    def repeatedNTimes(self, A):
        helper_set = set()

        for i in A:
            if i in helper_set:
                return i

            helper_set.add(i)
