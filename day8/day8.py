lines = open("day8_in.txt", "r").read().split("\n")

def to_rules(lines):
    rules = []
    for line in lines:
        tok = line.split("|")
        rules.append([tok[0].strip().split(" "), tok[1].strip().split(" ")])
    return rules

def get_segs(rules):
    count = 0
    for rule in rules:
        for mix in rule[1]:
            length = len(mix)
            if(length == 2 or length == 3 or length == 4 or length == 7):
                count +=1
    return count
        
print(get_segs(to_rules(lines)))