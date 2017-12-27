#!/usr/bin/env python
# -*- coding: utf-8 -*-

instr = open("Data/conversion_rules.txt","r", 1, "utf_8")
print("\t...loading conversion rules...")
rules = {}
for line in instr:
    rule = line.rstrip()
    subrule = []
    subrule = rule.split(">")
    tuple = {subrule[0]:subrule[1]}
    rules.update(tuple)
instr.close()
#print(rules)

def convert_ipa_to_class(instring):
    stringA = instring.split(' ')
    stringB = instring.split(' ')
    length = len(stringA)
    for i in range(length):
        suchkey = stringB[i]
        if suchkey in rules:
            stringA[i] = rules[suchkey]
    return stringA, stringB

def convert_class_to_ipa(instring):
    #TODO: Braucht man diese Funktion überhaupt?
    return
