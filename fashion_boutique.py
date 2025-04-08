clothes_in_box = [int(n) for n in input().split()]
capacity_of_one_rack = int(input())

current_rack_space = capacity_of_one_rack
racks_num = 1

while clothes_in_box:
    current_item = clothes_in_box.pop()

    if current_rack_space - current_item >= 0:
        current_rack_space -= current_item
    else:
        racks_num += 1
        current_rack_space = capacity_of_one_rack - current_item

print(racks_num)