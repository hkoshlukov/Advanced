from collections_exercise import deque


def fill_the_box(height, length, width, *cubes):
    box_size = height * length * width
    cubes_copy = deque(cubes)
    box = []
    while box_size > 0:
        current_el = cubes_copy.popleft()
        if current_el == 'Finish':
            break
        box_size -= current_el

    if box_size > 0:
        return f"There is free space in the box. You could put {box_size} more cubes."
    else:
        result = abs(box_size) + sum(list(filter(lambda x: isinstance(x, int), cubes_copy)))
        return f"No more free space! You have {result} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
