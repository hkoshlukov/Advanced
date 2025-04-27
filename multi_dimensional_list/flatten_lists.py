data = input().split('|')
matrix = []
for el in data[::-1]:
    matrix.extend(el.split())

print(*matrix)
