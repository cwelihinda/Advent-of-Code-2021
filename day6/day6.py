fish = open("day6_in.txt", "r").read().split(",")
for i in range(256):
    print("DAY " + str(i))
    next_gen = []
    new_fish = []
    for f in fish:
        days_till_repro = int(f) - 1;
        if(days_till_repro == -1):
            days_till_repro = 6
            new_fish.append(8)
        next_gen.append(days_till_repro)
    fish = next_gen + new_fish
print(len(fish))
        