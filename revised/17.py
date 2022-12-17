data = open("17.txt").read().strip()
instructions = [1 if x==">" else -1 for x in data]

rockfalls = """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##""".split("\n\n")

rockfalls = [x.split("\n")[::-1] for x in rockfalls]
rockfalls = [[(x, y) for y, row in enumerate(rock) for x, c in enumerate(row) if c == "#"] for rock in rockfalls]

width = 7
maxrocks = 1000000000000

grid = [["."]*width for _ in range(2022*10)]
grid[0] = ["#"]*width

startX, maxY = 2, [0]*width
seen = {}

cycle, height = 0, 0
ffheight = 0

i = j = 0
while i < maxrocks:
	if i == 2022:
		print(max(maxY)) # part 1

	maxmaxY = max(maxY)
	maxYrel = (tuple([y-maxmaxY for y in maxY]), i%len(rockfalls), j%len(instructions)) # relative shape
	if i > 2022 and maxYrel in seen:
		cycle, height = i - seen[maxYrel][0], maxmaxY - seen[maxYrel][1]

		remaining = maxrocks - i
		i += cycle * (remaining//cycle)
		ffheight += height*(remaining//cycle)
		seen = {}

	seen[maxYrel] = (i, maxmaxY)

	rock = rockfalls[i%len(rockfalls)]
	i += 1

	x, y = startX, max(maxY)+4
	while True:
		ins = instructions[j%len(instructions)]
		execute = True
		for rx, ry in rock:
			if x+rx+ins < 0 or x+rx+ins >= width:
				execute = False
				break
			if grid[y+ry][x+rx+ins] == "#":
				execute = False
				break
		if execute:
			x += ins
		j += 1

		execute = True
		for rx, ry in rock:
			if grid[y+ry-1][x+rx] == "#":
				execute = False
				break
		if not execute:
			for rx, ry in rock:
				if y+ry >= len(grid):
					grid += [["."]*width for _ in range(10)]
				grid[y+ry][x+rx] = "#"
				if y+ry > maxY[x+rx]:
					maxY[x+rx] = y+ry
			break
		y -= 1

print(max(maxY)+ffheight) # part 2