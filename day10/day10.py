lines = open("day10_sample.txt", "r").read().split("\n")

def init_lookup():
    lookup = {}
    lookup[")"] = 3
    lookup["]"] = 57
    lookup["}"] = 1197
    lookup[">"] = 25137
    return lookup

def is_opening(char):
    return char == "{" or char == "(" or char == "[" or char == "<"

def is_match(closer, potential_opener):
    if(closer == ")"):
        return chr(ord(closer) - 1) == potential_opener
    return chr(ord(closer) - 2) == potential_opener
def check_line(line):
    stack = []
    for char in line:
        if(is_opening(char)):
            stack.append(char)
        elif(is_match(char,stack[-1])):
            stack.pop()
        else:
            return init_lookup()[char]
    return 0

count = 0
for line in lines:
    count += check_line(line)
    
print(count)