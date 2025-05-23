size = int(input())

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

matrix = []
alice_pos = []
tea_bags = 0

for row in range(size):
    matrix.append(input().split())

    if 'A' in matrix[row]:
        alice_pos = [row, matrix[row].index('A')]
        matrix[row][alice_pos[1]] = '*'

while tea_bags < 10:
    direction = input()

    row = alice_pos[0] + directions[direction][0]
    col = alice_pos[1] + directions[direction][1]

    if not (0 <= row < size and 0 <= col < size):
        break

    position = matrix[row][col]
    alice_pos = [row, col]
    matrix[row][col] = '*'

    if position =='R':
        break

    if position.isdigit():
        tea_bags += int(position)

if tea_bags == 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
print(*[' '.join(row) for row in matrix], sep= '\n')