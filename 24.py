data = open("24.txt").read().strip()
grid = [list(x) for x in data.split("\n")]
height, width = len(grid), len(grid[0])

blizzards = {}
for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] in "<>^v":
			blizzards[(i, j)] = [grid[i][j]]

start = (0, 1)
end = (len(grid)-1, len(grid[0])-2)

def move_blizzards(blizzards):
	new_blizzards = {}
	dirs = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
	for (i, j), ds in blizzards.items():
		for d in ds:
			new_pos = (i + dirs[d][0], j + dirs[d][1])
			if grid[new_pos[0]][new_pos[1]] == "#":
				new_pos = (i-(dirs[d][0]*(height-3)), j-(dirs[d][1]*(width-3)))
			if new_pos in new_blizzards:
				new_blizzards[new_pos].append(d)
			else:
				new_blizzards[new_pos] = [d]
	return new_blizzards

# bfs
curr = [start]
dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
t = epoch = 0
restart = False
while True:
	new = []
	blizzards = move_blizzards(blizzards)
	for pos  in curr:
		for d in dirs:
			new_pos = (pos[0] + d[0], pos[1] + d[1])
			if new_pos[0] < 0 or new_pos[0] >= len(grid): # out of bounds
				continue
			elif grid[new_pos[0]][new_pos[1]] == "#": # wall
				continue
			elif new_pos in blizzards: # blizzard
				continue
			elif new_pos == end:
				if epoch == 0:
					print(t+1) # Part 1
					new = [end]
					epoch += 1
					restart = True
					break
				elif epoch == 2:
					print(t+1) # Part 2
					exit()
			elif new_pos == start:
				if epoch == 1:
					new = [start]
					epoch += 1
					restart = True
					break
			new.append(new_pos)
		if restart:
			restart = False
			break
		if pos not in blizzards:
			new.append(pos)
	curr = list(set(new))
	t += 1
