numbers = tuple(map(float, input().split()))
my_dict = {}

for n in numbers:
    if n not in my_dict.keys():
        my_dict[n] = 1
    else:
        my_dict[n] += 1

for key, value in my_dict.items():
    print(f"{key} - {value} times")
