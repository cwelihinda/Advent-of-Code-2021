def get_rates(lines):
    return get_msb_n(lines, 0), get_lsb_n(lines, 0)

def get_msb_n(numbers, index):
    if(len(numbers) == 1):
        return list(numbers[0])
    ones, zeros = construct_lists(numbers, index)
    if(len(ones) < len(zeros)):
        return get_msb_n(zeros, index + 1)
    else:
        return get_msb_n(ones, index + 1) 
    
def get_lsb_n(numbers, index):
    if(len(numbers) == 1):
        return list(numbers[0])
    ones, zeros = construct_lists(numbers, index)
    if(len(ones) >= len(zeros)):
        return get_lsb_n(zeros, index + 1)
    else:
        return get_lsb_n(ones, index + 1)
    
def construct_lists(numbers, index):
    ones = []
    zeros = []
    for number in numbers:
        if(number[index] == "1"):
            ones.append(number)
        else:
            zeros.append(number)
    return ones, zeros
    
msb, lsb = get_rates(open("day3_in.txt", "r").read().split("\n"))
print(int("".join(msb), 2) * int("".join(lsb), 2))

