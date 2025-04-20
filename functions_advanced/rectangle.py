def rectangle(*nums):
    def area():
        return nums[0] * nums[1]

    def perimeter():
        return 2 * (nums[0] + nums[1])

    if type(nums[0]) is not int or type(nums[1]) is not int:
        return "Enter valid values!"
    else:
        return f'''Rectangle area: {area()}
Rectangle perimeter: {perimeter()}'''


print(rectangle(2, 10))
