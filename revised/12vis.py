import matplotlib.pyplot as plt
from collections import deque, defaultdict
import math
import numpy as np


data = open("12.txt").read().strip()
grid = [list(x) for x in data.split("\n")]

x = np.arange(0, len(grid))
y = np.arange(0, len(grid[0]))
z = np.zeros((len(grid), len(grid[0])))

for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] == "S":
			z[i][j] = 0
			start = (i,j)
			grid[i][j] = "a"
		elif grid[i][j] == "E":
			z[i][j] = 25
			goal = (i,j)
			grid[i][j] = "z"
		else:
			z[i][j] = ord(grid[i][j]) - ord('a')

dirs = ((-1,0),(1,0),(0,-1),(0,1))

def bfs(start, goal):
	Q = deque()
	Q.append(start)

	prev = defaultdict(lambda: None)
	dist = defaultdict(lambda: math.inf)
	dist[start] = 0

	while Q:
		u = Q.popleft()

		if u == goal:
			curr = u
			
			fig, ax = plt.subplots()
			cmap = plt.cm.viridis
			norm = plt.Normalize(vmin=0, vmax=25)
			rgba = cmap(norm(z))

			while curr != start:
				rgba[curr[0]][curr[1]] += np.array([0.1, 0.1, 0.5, 0])
				curr = prev[curr]
			
			ax.imshow(rgba)
			plt.axis('off')
			plt.savefig("12path.png")
			return dist[u]
			
		for di, dj in dirs:
			x, y = u[0]+di, u[1]+dj
			if 0 <= x < len(grid) and 0 <= y < len(grid[x]):
				if ord(grid[x][y]) <= ord(grid[u[0]][u[1]])+1:
					update = dist[u] + 1
					if update < dist[(x,y)]:
						dist[(x,y)] = update
						prev[(x,y)] = u
						Q.append((x,y))
	return math.inf

print(bfs(start, goal))