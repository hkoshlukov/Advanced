import sys

rows, cols = [int(n) for n in input().split()]
matrix = [input().split() for _ in range(rows)]

max_sum = -sys.maxsize
biggest_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        first = matrix[row][col:col + 3]
        second = matrix[row + 1][col:col + 3]
        third = matrix[row + 2][col:col + 3]

        current_sum = sum(map(int, first)) + sum(map(int, second)) + sum(map(int, third))

        if current_sum > max_sum:
            max_sum = current_sum
            biggest_matrix = [first, second, third]

print(f"Sum = {max_sum}")
[print(*biggest_matrix[row]) for row in range(3)]
