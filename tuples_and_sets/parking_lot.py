def print_f():
    if not cars:
        print('Parking Lot is Empty')
    else:
        for p in cars:
            print(''.join(p))


lines = int(input())
COMMAND_IN = 'IN'
COMMAND_OUT = 'OUT'
cars = set()

for _ in range(lines):
    command, plate = input().split(', ')
    if command == COMMAND_IN:
        cars.add(plate)
    elif command == COMMAND_OUT:
        cars.remove(plate)
print_f()
