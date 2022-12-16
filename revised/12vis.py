import matplotlib.pyplot as plt
from collections import deque, defaultdict
import math
import numpy as np


data = open("12.txt").read().strip()
grid = [list(x) for x in data.split("\n")]

X = np.arange(0, len(grid))
Y = np.arange(0, len(grid[0]))
z = np.zeros((len(grid), len(grid[0])))
X, Y = np.meshgrid(X, Y)

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

			path = [(*curr, z[curr[0]][curr[1]])]
			while curr != start:
				rgba[curr[0]][curr[1]] += np.array([0.1, 0.1, 0.5, 0])
				curr = prev[curr]
				path.append((*curr, z[curr[0]][curr[1]]))
			
			ax.imshow(rgba)
			plt.axis('off')
			plt.savefig("12path.png", bbox_inches='tight', pad_inches=0)
			return dist[u], path
			
		for di, dj in dirs:
			x, y = u[0]+di, u[1]+dj
			if 0 <= x < len(grid) and 0 <= y < len(grid[x]):
				if ord(grid[x][y]) <= ord(grid[u[0]][u[1]])+1:
					update = dist[u] + 1
					if update < dist[(x,y)]:
						dist[(x,y)] = update
						prev[(x,y)] = u
						Q.append((x,y))
	return math.inf, []

res, path = bfs(start, goal)
print(res)

Z = z.T
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

ax.set_zlim(0, 25)
ax.set_xlim(0, len(grid))
ax.set_ylim(0, len(grid[0]))
ax.view_init(30, -45)
ax.set_box_aspect((np.ptp(X), np.ptp(Y), np.ptp(Z)))

path = np.array(path)
surf = ax.plot_surface(X, Y, Z, cmap=plt.cm.viridis, linewidth=0, antialiased=False, zorder=1)
plt.savefig("12_3D.png", bbox_inches='tight', pad_inches=0)
ax.plot(path[:,0], path[:,1], path[:,2], color='red', linewidth=1, zorder=4)
plt.savefig("12_3Dpath.png", bbox_inches='tight', pad_inches=0)