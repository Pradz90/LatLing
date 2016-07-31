lines = 0
with open('../Data/unicode.txt', encoding='utf-8') as f:
	line_count = len(f.readlines())
	data = [0 for i in range(line_count)]
	for line in f:
		print(repr(line))
with open('../Data/unicode.txt', encoding='utf-8') as f:
	for line in f:
		s = repr(line)
		rawdata = s.split("\\t")
		latter = str(rawdata[3])
		newlatter = latter[0:-3]
		rawdata[3] = newlatter
		data[lines] = rawdata
		lines += 1
	print(data)
	print("Lines: "+str(lines))
