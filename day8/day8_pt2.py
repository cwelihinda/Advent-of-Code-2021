lines = open("day8_in.txt", "r").read().split("\n")

def to_rules(lines):
    rules = []
    for line in lines:
        tok = line.split("|")
        rules.append([tok[0].strip().split(" "), tok[1].strip().split(" ")])
    return rules

def get_six(candidates, one):
    rejects = []
    final = ''
    for candidate in candidates:
        temp = candidate
        for char in one:
            temp = temp.replace(char, "")
        
        if(len(temp) == 5):
            final = candidate
        else:    
            rejects.append(candidate)
    return final, rejects
        
def get_three(candidates, one):
    rejects = []
    final = ''
    for candidate in candidates:
        temp = candidate
        for char in one:
            temp = temp.replace(char, "")
        
        if(len(temp) == 3):
            final = candidate
        else:
            rejects.append(candidate)
    return final, rejects

def magic_method_it_was_duplicated_at_refactor(candidates, three):
    rejects = []
    final = ''
    for candidate in candidates:
        temp = candidate
        for char in three:
            temp = temp.replace(char, "")
        
        if(len(temp) == 1):
            final = candidate
        else:
            rejects.append(candidate)
    return final, rejects[0]

def decode(lines):
    score = 0    
    for rule in lines:
        rules = [''] * 10
        length_6 = [] 
        length_5 = [] 
        for clue in rule[0]:
            length = len(clue)
            if(length == 2):
                rules[1] = clue
            elif(length == 3):
                rules[7] = clue
            elif(length == 4):
                rules[4] = clue
            elif(length == 5):
                length_5.append(clue)
            elif(length == 6):
                length_6.append(clue)
            elif(length == 7):
                rules[8] = clue
        rules[6], length_6 = get_six(length_6, rules[1])
        rules[3], length_5 = get_three(length_5, rules[1])
        rules[9], rules[0] = magic_method_it_was_duplicated_at_refactor(length_6, rules[3])
        rules[2], rules[5] = magic_method_it_was_duplicated_at_refactor(length_5, rules[6])
        
        decoded = ''
      
        for encoded in rule[1]:
            for i in range(len(rules)):
                if(sorted(encoded) == sorted(rules[i])):
                    decoded += str(i)
        score += int(decoded)
    return score

print(decode(to_rules(lines)))