from collections import deque

kids = input().split(' ')
leave_integer = int(input())
counter = 0
deque_players = deque(kids)

while len(deque_players) > 1:
    counter += 1
    current_player = deque_players.popleft()

    if counter == leave_integer:
        print(f'Removed {current_player}')
        counter = 0
    else:
        deque_players.append(current_player)

print(f'Last is {deque_players[0]}')
