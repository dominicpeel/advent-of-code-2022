import matplotlib.pyplot as plt
import numpy as np
from celluloid import Camera

data = open("23.txt").read().strip()
lines = [x for x in data.split("\n")]
elves = set()
for i in range(len(lines)):
	for j in range(len(lines[i])):
		if lines[i][j] == "#":
			elves.add((i, j))

def print_grid(elves):
	minx, maxx, miny, maxy = -13, 122, -12, 119

	grid = np.zeros((maxx-minx+1, maxy-miny+1))

	for i in range(minx, maxx+1):
		for j in range(miny, maxy+1):
			if (i,j) in elves:
				grid[i-minx, j-miny] = 1
			
	plt.imshow(grid, cmap=cmap)
	camera.snap()

cvals = [0, 1]
colors = ["#0F0F23", "#00cc00"]
cmap = plt.cm.colors.ListedColormap(colors)
fig = plt.figure()
camera = Camera(fig)
print_grid(elves)

def getDir(check, elf):
	i, j = elf
	N, NE, NW = (i-1, j), (i-1, j+1), (i-1, j-1)
	S, SE, SW = (i+1, j), (i+1, j+1), (i+1, j-1)
	E, W = (i, j+1), (i, j-1)
	if N not in elves and NE not in elves and NW not in elves and S not in elves and SE not in elves and SW not in elves and W not in elves and E not in elves:
		return elf
	if check == "N" and N not in elves and NE not in elves and NW not in elves:
		return N
	elif check == "S" and S not in elves and SE not in elves and SW not in elves:
		return S
	elif check == "W" and W not in elves and NW not in elves and SW not in elves:
		return W
	elif check == "E" and E not in elves and NE not in elves and SE not in elves:
		return E
	return elf

dir_q = ["N", "S", "W", "E"]

r = 1
while True:
	# round 1
	new_elves = {}
	for elf in elves:
		for d in dir_q:
			new_dir = getDir(d, elf)
			if new_dir != elf:
				break

		if new_dir not in new_elves:
			new_elves[new_dir] = [elf]
		else:
			new_elves[new_dir].append(elf)
	
	# round 2
	prev_elves = elves
	elves = set()
	for elf in new_elves:
		if len(new_elves[elf]) == 1:
			elves.add(elf)
		else:
			for k in range(len(new_elves[elf])):
				elves.add(new_elves[elf][k])
	
	print_grid(elves)
	if elves == prev_elves:
		print(r)
		break

	dir_q.append(dir_q.pop(0))
	r += 1

animation = camera.animate()
animation.save("23vis.mp4", fps=60, dpi=200)
