instr = open("Data/conversion_rules.txt")
print("\t...loading conversion rules.")
rules = []
for line in instr:
    rule = line.rstrip()
    subrule = []
    subrule = rule.split(">")
    rules.append(subrule)
instr.close()
#print(rules)
