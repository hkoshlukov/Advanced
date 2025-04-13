from functools import reduce


def operate(*nums):
    operator = nums[0]
    result = 0
    if operator == '+':
        result = reduce(lambda x, y: x + y, nums[1:])
        return result

    elif operator == '-':
        result = reduce(lambda x, y: x - y, nums[1:])
        return result

    elif operator == '*':
        result = reduce(lambda x, y: x * y, nums[1:])
        return result

    elif operator == '/':
        result = reduce(lambda x, y: x / y, nums[1:])
        return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
