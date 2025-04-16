def func_executor(*nums):
    result = []
    for function, res in nums:
        result.append(f"{function.__name__} - {function(*res)}")

    return f'\n'.join(result)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
