import matplotlib.pyplot as plt
import numpy as np

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
width = (min(rock[0] for rock in rocksArr), max(rock[0] for rock in rocksArr))

solid = {(x,y): 1 for x,y in rocksArr}
plt.figure()
plt.imshow(np.array([[1 if (x,y) in solid else 0 for x in range(width[0]-1, width[1]+2)] for y in range(-1,max_rock+3)]), cmap='gray', interpolation='nearest')
plt.savefig("14rocks.png", dpi=300)

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
			solid[(x, y)] = 2
			break
	if abyss:
		break
	i += 1

print(i)

plt.figure()
plt.imshow(np.array([[solid[(x,y)] if (x,y) in solid else 0 for x in range(width[0]-1, width[1]+2)] for y in range(-1,max_rock+3)]), cmap='gray', interpolation='nearest')
# plt.show()
plt.savefig("14part1.png", dpi=300)

# Part 2
solid = {(x,y): 1 for x,y in rocksArr}
floor = max_rock + 2
blocked = False
i = 0
while True:
	x, y = sand
	while True:
		if y+1 == floor:
			solid[(x, y)] = 2
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
				break
			else:
				solid[(x, y)] = 2
				break
	if blocked:
		break
	i += 1

print(i)

width = (min(obj[0] for obj in solid), max(obj[0] for obj in solid))
plt.figure()
plt.imshow(np.array([[solid[(x,y)] if (x,y) in solid else 0 for x in range(width[0]-1, width[1]+2)] for y in range(-1,max_rock+3)]), cmap='gray', interpolation='nearest')
# plt.show()
plt.savefig("14part2.png", dpi=300)
