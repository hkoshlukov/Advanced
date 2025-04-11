lines = int(input())
my_set = set()

for n in range(lines):

    for el in input().split():
        my_set.add(el)

print(*my_set, sep='\n')