def printf():
    print(len(regular_set))
    for e in sorted(regular_set):
        print(e)


number_of_guests = int(input())
regular_set = set()
COMMAND_END = 'END'
guests = []

for _ in range(number_of_guests):
    guest = input()
    regular_set.add(guest)

while True:
    lines = input()
    if lines == COMMAND_END:
        break

    else:
        if lines in regular_set:
            regular_set.remove(lines)

printf()
