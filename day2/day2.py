def get_instruction(line):
    tok = line.split(" ")
    return tok[0], int(tok[1])
def get_location(instructions):
    h = 0
    d = 0
    for i in range(len(instructions)):
        direction, movement = get_instruction(instructions[i])
        if(direction == "forward"):
            h += movement
        else:
            if(direction == "up"):
                movement *= -1
            d += movement
    return h,d
h,d = get_location(open("day2_in.txt", "r").read().split("\n"))
print(h * d)

