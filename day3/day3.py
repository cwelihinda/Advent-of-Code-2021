def sum_lists(high_low, line):
    for i in range(len(high_low)):
        high_low[i] = int(high_low[i]) + int(line[i])
    return high_low
def get_rates(lines):
    high_low = []
    for i in range(len(lines)):
        if(i==0):
            high_low = list(lines[i])
        high_low = sum_lists(high_low, lines[i])
        print(high_low)
        
    return get_msb(high_low, len(lines))
def get_msb(high_low, total):
    msb = [0 for x in range(len(high_low))]
    for i in range(len(high_low)):
        msb[i] = str(round(high_low[i] / total))
        print(msb[i])
    return msb
msb = get_rates(open("day3_in.txt", "r").read().split("\n"))
num = int("".join(msb), 2)
ep = ~num + 2**12
print(num * ep)

