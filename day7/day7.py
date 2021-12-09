def convert_to_nums(str_nums):
    nums = []
    for i in str_nums:
        nums.append(int(i))
    return sorted(nums)

def get_fuel(nums, median):
    fuel = 0
    for i in nums:
        fuel += abs(i - median)
    return fuel

def get_median(nums):
    median_index = 0
    if(len(nums)%2 == 1):
        median_index  = (len(nums) + 1) / 2
    else:
        median_index = len(nums) / 2
    return nums[int(median_index)]

nums = convert_to_nums(open("day7_in.txt", "r").read().split(","))
print(get_fuel(nums, get_median(nums)))