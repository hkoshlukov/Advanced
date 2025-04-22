rows = int(input())
matrix = [input().split(', ') for _ in range(rows)]
primary = [matrix[p][p] for p in range(rows)]
secondary = [matrix[s][rows - s - 1] for s in range(rows - 1, -1, -1)]
print(f"Primary diagonal: {', '.join(str(n) for n in primary)}. Sum: {sum(map(int, primary))}")
print(f"Secondary diagonal: {', '.join(str(n) for n in secondary[::-1])}. Sum: {sum(map(int, secondary))}")
