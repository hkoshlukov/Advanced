def even_odd(*nums):
    command = nums[-1]
    if command == 'even':
        result = [int(el) for el in nums[:-1] if el % 2 == 0]
        return result
    else:
        result = [int(el) for el in nums[:-1] if el % 2 != 0]
        return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
