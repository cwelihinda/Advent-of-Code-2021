def sum_slice(num_slice):
    return int(num_slice[0]) + int(num_slice[1]) + int(num_slice[2])
def get_increases(nums):
    prev = 10000000000000000
    count = 0
    for i in range(len(nums) - 2):
        if (sum_slice(nums[i:i+3]) > prev):
            count += 1
        prev = sum_slice(nums[i:i+3])
    return count
print(get_increases(open("day1_in.txt", "r").read().split("\n")))



