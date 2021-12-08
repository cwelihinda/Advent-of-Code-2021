def get_instruction(line):
    tok = line.split(" ")
    return tok[0], int(tok[1])

def get_location(instructions):
    h = 0
    d = 0
    aim = 0
    for i in range(len(instructions)):
        direction, movement = get_instruction(instructions[i])
        if(direction == "forward"):
            h += movement
            d += aim * movement
        else:
            if(direction == "up"):
                movement *= -1
            aim += movement
    return h,d

h,d = get_location(open("day2_in.txt", "r").read().split("\n"))

print(h * d)

