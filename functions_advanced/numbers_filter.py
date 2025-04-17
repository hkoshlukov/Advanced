def even_odd_filter(**nums):
    if 'odd' in nums:
        nums['odd'] = [n for n in nums['odd'] if int(n) % 2 == 1]
    if 'even' in nums:
        nums['even'] = list(filter(lambda x: x % 2 == 0, nums['even'])
)
    return dict(sorted(nums.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
