# Part 1 and 2: 50m21s73
data = open("14.txt").read().strip()
rock_shape = [[[int(z) for z in y.split(",")] for y in x.split(" -> ")] for x in data.split("\n")] 

rocksArr = []
for rock_form in rock_shape:
	for i in range(len(rock_form)-1):
		if rock_form[i][0] != rock_form[i+1][0]:
			if rock_form[i][0] > rock_form[i+1][0]:
				for j in range(rock_form[i+1][0], rock_form[i][0]+1):
					rocksArr.append((j, rock_form[i][1]))
			else:
				for j in range(rock_form[i][0], rock_form[i+1][0]+1):
					rocksArr.append((j, rock_form[i][1]))
		else:
			if rock_form[i][1] > rock_form[i+1][1]:
				for j in range(rock_form[i+1][1], rock_form[i][1]+1):
					rocksArr.append((rock_form[i][0], j))
			else:
				for j in range(rock_form[i][1], rock_form[i+1][1]+1):
					rocksArr.append((rock_form[i][0], j))

max_rock = max([y for x, y in rocksArr])

rocks = set(rocksArr)
sand = (500,0)

i = 0
abyss = False
while True:
	x, y = sand
	while True:
		if y == max_rock:
			abyss = True
			break
		elif (x, y+1) not in rocks:
			x, y = x, y+1
		elif (x-1, y+1) not in rocks:
			x, y = x-1, y+1
		elif (x+1, y+1) not in rocks:
			x, y = x+1, y+1
		else:
			rocks.add((x, y))
			break
	if abyss:
		break
	i += 1

print(i)

#Part 2
rocks = set(rocksArr)
floor = max_rock + 2
i = 0
blocked = False
while True:
	x, y = sand
	while True:
		if y+1 == floor:
			rocks.add((x, y))
			break
		elif (x, y+1) not in rocks:
			x, y = x, y+1
		elif (x-1, y+1) not in rocks:
			x, y = x-1, y+1
		elif (x+1, y+1) not in rocks:
			x, y = x+1, y+1
		else:
			if y == 0:
				blocked = True
			rocks.add((x, y))
			break
	i += 1
	if blocked:
		break

print(i)