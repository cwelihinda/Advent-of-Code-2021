def convert_to_nums(str_nums):
    nums = []
    total = 0
    for i in str_nums:
        i = int(i)
        nums.append(i)
        total += i
    return nums, int(total / len(nums))

def get_fuel(nums, median):
    fuel = 0
    for i in nums:
        diff = abs(i - median)
        fuel += sum(range(0, diff + 1))
    return fuel

nums, mean = convert_to_nums(open("day7_in.txt", "r").read().split(","))
print(get_fuel(nums, mean))