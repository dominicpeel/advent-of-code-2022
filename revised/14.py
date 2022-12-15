# Part 1 and 2: 50m21s73
data = open("14.txt").read().strip()
rock_shape = [[[int(z) for z in y.split(",")] for y in x.split(" -> ")] for x in data.split("\n")] 

rocksArr = []
max_rock = 0
for rock_form in rock_shape:
	for i in range(len(rock_form)-1):
		a, b = rock_form[i], rock_form[i+1]
		for k in range(min(a[0], b[0]), max(a[0], b[0])+1):
			rocksArr.append((k, a[1]))
		for k in range(min(a[1], b[1]), max(a[1], b[1])+1):
			rocksArr.append((a[0], k))
		max_rock = max(max_rock, a[1], b[1])

solid = set(rocksArr)

# Part 1
sand = (500,0)
abyss = False
i = 0
while True:
	x, y = sand
	while True:
		if y == max_rock:
			abyss = True
			break
		elif (x, y+1) not in solid:
			x, y = x, y+1
		elif (x-1, y+1) not in solid:
			x, y = x-1, y+1
		elif (x+1, y+1) not in solid:
			x, y = x+1, y+1
		else:
			solid.add((x, y))
			break
	if abyss:
		break
	i += 1

print(i)

# Part 2
solid = set(rocksArr)
floor = max_rock + 2
blocked = False
i = 0
while True:
	x, y = sand
	while True:
		if y+1 == floor:
			solid.add((x, y))
			break
		elif (x, y+1) not in solid:
			x, y = x, y+1
		elif (x-1, y+1) not in solid:
			x, y = x-1, y+1
		elif (x+1, y+1) not in solid:
			x, y = x+1, y+1
		else:
			if y == 0:
				blocked = True
			solid.add((x, y))
			break
	i += 1
	if blocked:
		break

print(i)
