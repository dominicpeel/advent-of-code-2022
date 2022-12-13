import math

data = open("12.txt").read().strip()
grid = [list(x) for x in data.split("\n")]

def djikstra(start, goal):
	Q = set()
	dist = {}
	prev = {}

	for i in range(len(grid)):
		for j in range(len(grid[i])):
			dist[(i,j)] = math.inf
			prev[(i,j)] = None
			Q.add((i,j))

	dist[start] = 0

	while Q:
		u = min(Q, key=lambda x: dist[x])
		if u == goal:
			return dist[u]
		Q.remove(u)

		for x, y in ((u[0]-1,u[1]),(u[0]+1,u[1]),(u[0],u[1]-1),(u[0],u[1]+1)):
			if (x,y) in Q:
				if ord(grid[x][y]) < ord(grid[u[0]][u[1]]) or ord(grid[x][y])-ord(grid[u[0]][u[1]]) < 2:
					alt = dist[u] + 1
					if alt < dist[(x,y)]:
						dist[(x,y)] = alt
						prev[(x,y)] = u

# Find the start
for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] == "S":
			start = (i,j)
			grid[i][j] = "a"
		elif grid[i][j] == "E":
			goal = (i,j)
			grid[i][j] = "z"
	
# Part A
print(djikstra(start, goal))

# Part B
min_dist = math.inf
for i in range(len(grid)):
	for j in range(0, 3):
		if grid[i][j] == "a":
			min_dist = min(min_dist, djikstra((i,j), goal))

print(min_dist)
