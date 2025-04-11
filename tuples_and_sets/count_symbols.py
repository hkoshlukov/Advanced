text = input()
my_dict = {}
for l in text:
    if l not in my_dict.keys():
        my_dict[l] = 1
    else:
        my_dict[l] += 1

for l, t in sorted(my_dict.items()):
    print(f"{l}: {t} time/s")
