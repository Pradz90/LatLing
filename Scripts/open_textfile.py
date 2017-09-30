source = open("Data/source.txt")
for line in source:
    str = line.rstrip()
    print(str)
source.close()
