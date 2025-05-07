def move(direction, steps):
    r = my_position[0] + (directions[direction][0] * steps)
    c = my_position[1] + (directions[direction][1] * steps)

    if not (0 <= r < rows and 0 <= c < cols):
        return my_position
    if field[r][c] == 'x':
        return my_position

    return [r, c]


def shoot(direction):
    r = my_position[0] + directions[direction][0]
    c = my_position[1] + directions[direction][1]
    while 0 <= r < rows and 0 <= c < cols:
        if field[r][c] == 'x':
            field[r][c] = '.'
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]


rows, cols = 5, 5

field = []
my_position = None
targets = 0
targets_hit = 0
targets_hit_position = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(rows):
    field.append(input().split())
    if 'A' in field[row]:
        my_position = [row, field[row].index('A')]
    if 'x' in field[row]:
        targets += field[row].count('x')

command_num = int(input())

for _ in range(command_num):
    lines = input().split()

    if lines[0] == 'move':
        my_position = move(lines[1], int(lines[2]))
    elif lines[0] == 'shoot':
        targets_down_pos = shoot(lines[1])

        if targets_down_pos:
            targets_hit_position.append(targets_down_pos)
            targets_hit += 1

        if targets_hit == targets:
            print(f'Training completed! All {targets} targets hit.')
            break

if targets_hit < targets:
    print(f'Training not completed! {targets - targets_hit} targets left.')

[print(target_pos) for target_pos in targets_hit_position]
