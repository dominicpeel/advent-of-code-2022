import matplotlib.pyplot as plt
import numpy as np
from celluloid import Camera

data = open("24.txt").read().strip()
grid = [list(x) for x in data.split("\n")]
height, width = len(grid), len(grid[0])

def print_grid(grid, blizzards, curr):
	np_grid = np.zeros((len(grid), len(grid[0])))
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] == "#":
				np_grid[i][j] = 1
			elif (i, j) in blizzards:
				np_grid[i][j] = 2
			elif (i, j) in curr:
				np_grid[i][j] = 3
	plt.imshow(np_grid, cmap=cmap, vmin=0, vmax=3)
	plt.axis("off")
	camera.snap()

blizzards = {}
for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] in "<>^v":
			blizzards[(i, j)] = [grid[i][j]]

cvals = [0, 1, 2, 3]
colors = ["black", "grey", "white", "#00cc00"]
cmap = plt.cm.colors.ListedColormap(colors)
fig = plt.figure()
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
camera = Camera(fig)

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
t = 0
done = False
while True:
	print_grid(grid, blizzards, curr)
	new = []
	blizzards = move_blizzards(blizzards)
	for pos in curr:
		for d in dirs:
			new_pos = (pos[0] + d[0], pos[1] + d[1])
			if new_pos[0] < 0 or new_pos[0] >= len(grid): # out of bounds
				continue
			elif grid[new_pos[0]][new_pos[1]] == "#": # wall
				continue
			elif new_pos in blizzards: # blizzard
				continue
			elif new_pos == end:
				print(t+1) # Part 1
				new.append(new_pos)
				done = True
			new.append(new_pos)
		if done:
			break
		if pos not in blizzards:
			new.append(pos)
	curr = list(set(new))
	t += 1
	if done:
		break


print_grid(grid, blizzards, curr)
animation = camera.animate()
animation.save("24vis.mp4", fps=60, dpi=300, savefig_kwargs={"facecolor": "black"})
