from collections_exercise import deque

rows, cols = list(map(int, input().split()))
word = list(input())

word_copy = deque(word)

for row in range(rows):
    while len(word_copy) < cols:
        word_copy.extend(word)

    if row % 2 == 0:
        print(*[word_copy.popleft() for _ in range(cols)], sep='')
    else:
        print(*[word_copy.popleft() for _ in range(cols)][::-1], sep='')
