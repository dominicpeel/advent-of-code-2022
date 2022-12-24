data = open("23.txt").read().strip()
# data = """..............
# ..............
# .......#......
# .....###.#....
# ...#...#.#....
# ....#...##....
# ...#.###......
# ...##.#.##....
# ....#..#......
# ..............
# ..............
# .............."""
lines = [x for x in data.split("\n")]
elves = set()
for i in range(len(lines)):
	for j in range(len(lines[i])):
		if lines[i][j] == "#":
			elves.add((i, j))

# print(len(elves))
dirs = {"N": [-1, 0], "NE": [-1, 1], "E": [0, 1], "SE": [1, 1], "S": [1, 0], "SW": [1, -1], "W": [0, -1], "NW": [-1, -1]}

def print_grid(elves):
	minx = min([x[0] for x in elves])
	maxx = max([x[0] for x in elves])
	miny = min([x[1] for x in elves])
	maxy = max([x[1] for x in elves])

	# print grid
	for i in range(minx, maxx+1):
		for j in range(miny, maxy+1):
			if (i,j) in elves:
				print("#", end="")
			else:
				print(".", end="")
		print()
	print()

# print_grid(elves)

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
	
	if r == 10:
		minx = min([x[0] for x in elves])
		maxx = max([x[0] for x in elves])
		miny = min([x[1] for x in elves])
		maxy = max([x[1] for x in elves])

		res = (maxx - minx + 1)*(maxy - miny + 1) - len(elves)
		print(res)
	if elves == prev_elves:
		print(r)
		break

	dir_q.append(dir_q.pop(0))
	r += 1


