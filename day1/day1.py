def get_increases(nums):
    prev = 10000000000000000
    count = 0
    for i in range(len(nums)):
        if (int(nums[i]) > prev):
            count += 1
        prev = int(nums[i])
    return count

print(get_increases(open("day1_in.txt", "r").read().split("\n")))



