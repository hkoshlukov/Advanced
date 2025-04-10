from math import floor
lines = int(input())
odd_set = set()
even_set = set()
sum_func = 0
result = 0
iteration = 1
for i in range(lines):
    name = input()

    for l in name:
        sum_func += ord(l)
    result = floor(sum_func / iteration)
    if result % 2 == 0:
        even_set.add(result)
    elif result % 2 != 0:
        odd_set.add(result)

    sum_func = 0
    iteration += 1

if sum(even_set) == sum(odd_set):
    intersection = odd_set | even_set
    print(f"{', '.join(str(n) for n in intersection)}")
elif sum(even_set) > sum(odd_set):
    sym_difference = even_set ^ odd_set
    print(f"{', '.join(str(n) for n in sym_difference)}")
else:
    difference = odd_set - even_set
    print(f"{', '.join(str(n) for n in difference)}")
