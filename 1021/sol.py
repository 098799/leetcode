def solve(string):
    stack = []
    result = []

    beginning = 0

    for index, character in enumerate(string):
        if character == "(":
            stack.append(character)
        else:
            stack.pop()
        if not stack:
            result.append(string[beginning + 1:index])
            beginning = index + 1

    return ''.join(result)
