def even_matrix():
    lines = int(input())
    matrix = []
    for _ in range(lines):
        numbers = [int(n) for n in input().split(', ') if int(n) % 2 == 0]
        matrix.append(numbers)

    return matrix


print(even_matrix())
