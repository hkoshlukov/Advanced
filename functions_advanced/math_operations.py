from collections_exercise import deque


def math_operations(*values, **keys):
    list_values = deque(el for el in values)
    iteration = 0
    while True:
        if len(list_values) == 0:
            break

        if iteration == 4:
            iteration = 0

        current_el = list_values.popleft()
        if iteration == 0:
            keys['a'] += current_el
        elif iteration == 1:
            keys['s'] -= current_el
        elif iteration == 2:
            if keys['d'] != 0 and current_el != 0:
                keys['d'] /= current_el
        elif iteration == 3:
            keys['m'] *= current_el

        iteration += 1

    sorted_dict = sorted(keys.items(), key=lambda x: (-x[1],x[0]))
    return '\n'.join(f'{key}: {value:.1f}' for (key, value) in sorted_dict)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
