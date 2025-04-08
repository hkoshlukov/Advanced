from collections import deque

food = int(input())
orders = deque([int(n) for n in input().split()])

print(max(orders))

for order in orders.copy():
    if food - order >= 0:
        orders.popleft()
        food -= order
    else:
        print(f"Orders left: {' '.join([str(n) for n in orders])}")
        break
else:
    print('Orders complete')
