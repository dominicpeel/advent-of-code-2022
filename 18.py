"""   --------Part 1---------   --------Part 2---------
Day       Time    Rank  Score       Time    Rank  Score
 18   00:09:57    1298      0   00:56:52    1935      0
"""

from collections import deque

data = open("18.txt").read().strip()
lines = [tuple([int(y) for y in x.split(",")]) for x in data.split("\n")]
line_set = set(lines)

# Part 1
sa = len(lines)*6

for (x,y,z) in line_set:
	adjs = ((x+1,y,z), (x,y+1,z), (x,y,z+1), (x-1,y,z), (x,y-1,z), (x,y,z-1))
	for adj in adjs:
		if adj in line_set:
			sa -= 1

print(sa)
res1 = sa

# Part 2
minmax = [[lines[0][0], lines[0][0]], [lines[0][1], lines[0][1]], [lines[0][2], lines[0][2]]]
for line in line_set:
	for i in range(3):
		if line[i] < minmax[i][0]:
			minmax[i][0] = line[i]
		elif line[i] > minmax[i][1]:
			minmax[i][1] = line[i]
mx, my, mz = minmax[0], minmax[1], minmax[2]
maxr = max(mx[1]-mx[0], my[1]-my[0], mz[1]-mz[0])

#bfs to find all air pockets
adjs_dir = ((1,0,0), (0,1,0), (0,0,1), (-1,0,0), (0,-1,0), (0,0,-1))

def bfs(x,y,z): # if air pocket, then all other visited cubes are part of air pocket, return all
	visited = set()
	visited.add((x,y,z))

	q = deque()
	q.append((x,y,z))
	while q:
		x,y,z = q.popleft()

		# if no collision in x,y,z maxr, then not air pocket, return []		
		hit = False
		for idx, (dx,dy,dz) in enumerate(adjs_dir):
			for i in range(1, maxr+1):
				if (x+dx*i, y+dy*i, z+dz*i) in line_set:
					hit = True
					break
		if not hit:
			return []

		for dx, dy, dz in adjs_dir:
			adj = (x+dx, y+dy, z+dz)
			if adj not in line_set and adj not in visited:
				q.append(adj)
				visited.add(adj)

	return visited


air_pockets_set = set()
for x in range(mx[0], mx[1]+1):
	for y in range(my[0], my[1]+1):
		for z in range(mz[0], mz[1]+1):
			if (x,y,z) not in line_set:
				# check if air pocket
				for air in bfs(x,y,z):
					air_pockets_set.add(air)

#sub any adj air pockets from sa
sa = res1
for air in air_pockets_set:
	# check if adjacent to cube
	for adj in adjs_dir:
		if (air[0]+adj[0], air[1]+adj[1], air[2]+adj[2]) in line_set:
			sa -= 1

print(sa)
