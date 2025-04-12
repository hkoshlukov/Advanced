number_of_students = int(input())
my_dict = {}

for _ in range(number_of_students):
    name, grade = input().split()
    if name not in my_dict:
        my_dict[name] = []

    my_dict[name].append(float(grade))

for key, value in my_dict.items():
    result = ' '.join(map(lambda v: f'{v:.2f}', value))
    print(f"{key} -> {result} (avg: {sum(value) / len(value):.2f})")
