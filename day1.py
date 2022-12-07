f = open("1.txt", "r")

cals = [0]
currelf = 0

for line in f.readlines():
	if line == "\n":
		currelf += 1
		cals.append(0)
		continue
	cals[currelf] += int(line[:-1])

cals.sort()
print(sum(cals[-3:]))