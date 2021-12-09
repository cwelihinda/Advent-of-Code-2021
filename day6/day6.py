def fish_to_buckets(fish):
    buckets = [0 for j in range(9)]
    for f in fish:
        buckets[int(f)] += 1
    return buckets

def run_day(buckets):
    new_day = [0 for j in range(len(buckets))]
    for i in range(len(buckets)):
        new_day[i - 1] = buckets[i]
    new_day[6] += new_day[8]
    return new_day

def run_simulation(days, buckets):  
    for i in range(days):
        buckets = run_day(buckets)
    return buckets

def count_buckets(buckets):
    count = 0
    for i in range(len(buckets)):
        count += buckets[i]
    return count

buckets = fish_to_buckets(open("day6_in.txt", "r").read().split(","))
print(count_buckets(run_simulation(80, buckets)))
print(count_buckets(run_simulation(256, buckets)))