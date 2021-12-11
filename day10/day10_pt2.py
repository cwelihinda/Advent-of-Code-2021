lines = open("day10_sample.txt", "r").read().split("\n")

def init_lookup():
    lookup = {}
    lookup[")"] = 1
    lookup["]"] = 2
    lookup["}"] = 3
    lookup[">"] = 4
    return lookup

def is_opening(char):
    return char == "{" or char == "(" or char == "[" or char == "<"

def is_match(closer, potential_opener):
    if(closer == ")"):
        return chr(ord(closer) - 1) == potential_opener
    return chr(ord(closer) - 2) == potential_opener

def get_match(opener):
    if(opener == "("):
        return chr(ord(opener) + 1)
    return chr(ord(opener) + 2)

def check_line(line):
    stack = []
    string = ""
    for char in line:
        if(is_opening(char)):
            stack.append(char)
        elif(is_match(char,stack[-1])):
            stack.pop()
        else:
            return ""

    for i in range(len(stack) - 1, 0 - 1, -1):
        string += get_match(stack[i])
    return string


def get_score(tail, lookup):
    score = 0
    for t in tail:
        score *= 5
        score += lookup[t]
    return score

tails = []
for line in lines:
    tail = check_line(line)
    if(tail != ""):
        tails.append(tail)

scores = []
for tail in tails:
    scores.append(get_score(tail, init_lookup()))

print(sorted(scores)[int(len(scores) / 2)])