from collections import deque

price_per_bullet = int(input())
size_gun_barrel = int(input())
bullets = [int(b) for b in input().split()]
locks = deque(int(l) for l in input().split())
value_of_intelligence = int(input())

bullets_shot = 0
bullets_cost = 0

while locks:
    if not bullets:
        break
    else:
        current_bullet = bullets.pop()
        current_lock = locks.popleft()
        bullets_shot += 1
        bullets_cost += price_per_bullet

        if current_lock >= current_bullet:
            print('Bang!')

        else:
            locks.insert(0, current_lock)
            print('Ping!')

        if bullets_shot == size_gun_barrel:
            if not bullets:
                pass
            else:
                bullets_shot = 0
                print('Reloading!')

earned_money = value_of_intelligence - bullets_cost
if len(locks) == 0:
    print(f"{len(bullets)} bullets left. Earned ${earned_money}")

else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
