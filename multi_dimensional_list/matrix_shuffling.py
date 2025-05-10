def check_valid_index(indeces):
    if set(indeces[:2]).issubset(valid_rows) and set(indeces[2:]).issubset(valid_cols):
        return True

    return False


def swap_command(command, indeces):
    if check_valid_index(indeces) and command == 'swap' and len(indeces) == 4:
        row1, col1, row2, col2 = indeces

        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        print(*[' '.join((matrix[r])) for r in range(rows)], sep='\n')
    else:
        print("Invalid input!")


rows, cols = [int(n) for n in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_cols = range(cols)

while True:
    command_type, *info = [int(x) if x.isdigit() else x for x in input().split()]

    if command_type == "END":
        break

    swap_command(command_type, info)
