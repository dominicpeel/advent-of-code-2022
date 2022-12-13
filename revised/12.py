from collections import deque, defaultdict
import math

data = open("12.txt").read().strip()
grid = [list(x) for x in data.split("\n")]

dirs = ((-1,0),(1,0),(0,-1),(0,1))
def bfs(start, goal):
	Q = deque()
	Q.append(start)
	
	dist = defaultdict(lambda: math.inf)
	dist[start] = 0

	while Q:
		u = Q.popleft()
		if u == goal:
			return dist[u]
			
		for di, dj in dirs:
			x, y = u[0]+di, u[1]+dj
			if 0 <= x < len(grid) and 0 <= y < len(grid[x]):
				if ord(grid[x][y]) <= ord(grid[u[0]][u[1]])+1:
					update = dist[u] + 1
					if update < dist[(x,y)]:
						dist[(x,y)] = update
						Q.append((x,y))
	return math.inf

for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] == "S":
			start = (i,j)
			grid[i][j] = "a"
		elif grid[i][j] == "E":
			goal = (i,j)
			grid[i][j] = "z"

# Part A
print(bfs(start, goal))

def bfs_b(start):
	Q = deque()
	Q.append(start)
	
	dist = defaultdict(lambda: math.inf)
	dist[start] = 0

	while Q:
		u = Q.popleft()
		if grid[u[0]][u[1]] == "a":
			return dist[u]

		for x, y in dirs:
			x, y = u[0]+x, u[1]+y
			if 0 <= x < len(grid) and 0 <= y < len(grid[x]):
				if ord(grid[x][y]) >= ord(grid[u[0]][u[1]])-1:
					update = dist[u] + 1
					if update < dist[(x,y)]:
						dist[(x,y)] = update
						Q.append((x,y))
	return math.inf

# Part B, start from end
print(bfs_b(goal))