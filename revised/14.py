data = open("14.txt").read().strip()
lines = [[[int(z) for z in y.split(",")] for y in x.split(" -> ")] for x in data.split("\n")] 

rocks = set()
max_rock = 0
for line in lines:
	for (x1, y1), (x2, y2) in zip(line, line[1:]):
		x1, x2 = sorted([x1, x2])
		y1, y2 = sorted([y1, y2])
		for x in range(x1, x2+1):
			for y in range(y1, y2+1):
				rocks.add(x + y*1j)
				if y > max_rock:
					max_rock = y

floor = max_rock + 2
blocked = abyss = False
i = 0
while True:
	x = 500
	while True:
		if not abyss and x.imag == max_rock:
			print(i) # Part 1
			abyss = True
		if x.imag + 1 == floor:
			break
		elif x + 1j not in rocks:
			x += 1j
		elif x-1 + 1j not in rocks:
			x += 1j - 1
		elif x+1 + 1j not in rocks:
			x += 1j + 1
		else:
			if x.imag == 0:
				blocked = True
			break
	rocks.add(x)
	i += 1
	if blocked:
		print(i) # Part 2
		break
