from collections import deque

cups_capacity = deque(int(c) for c in input().split())
bottles_capacity = [int(b) for b in input().split()]

wasted_water = 0

while cups_capacity:
    if not bottles_capacity:
        cups = [str(j) for j in cups_capacity]
        print(f"Cups: {' '.join(cups)}")
        print(f"Wasted litters of water: {wasted_water}")
        break
    else:
        current_cup = cups_capacity.popleft()
        current_bottle = bottles_capacity.pop()

        if current_cup > current_bottle:
            while current_cup > current_bottle:
                current_bottle += bottles_capacity.pop()
            result = current_bottle - current_cup
            wasted_water += result
        else:
            result = current_bottle - current_cup
            wasted_water += result

else:
    bottles = [str(k) for k in bottles_capacity]
    print(f"Bottles: {' '.join(bottles)}")
    print(f"Wasted litters of water: {wasted_water}")
