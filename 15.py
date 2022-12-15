"""   --------Part 1---------   --------Part 2---------
Day       Time    Rank  Score       Time    Rank  Score
 15   00:56:36    3830      0   03:00:23    4790      0

Execution time:
Part 1:  2.0536 seconds
Part 2: 44.7720 seconds
"""
data = open("15.txt").read().strip()
lines = [[y for y in x.split(": ")] for x in data.split("\n")]

for i, (sensor, beacon) in enumerate(lines):
	lines[i][0] = (int(sensor.split(", ")[0].split("=")[1]), int(sensor.split(", ")[1].split("=")[1]))
	lines[i][1] = (int(beacon.split(", ")[0].split("=")[1]), int(beacon.split(", ")[1].split("=")[1]))

beacons_set = set()
for sensor, beacon in lines:
	beacons_set.add(beacon)

# Part 1
y = 2000000
res = 0
grid = set()
x_seen = set()
for s, b in lines:
	manhattan = abs(s[0] - b[0]) + abs(s[1] - b[1])
	if abs(s[1] - y) <= manhattan:
		diff = manhattan - abs(s[1] - y)
		for i in range(s[0] - diff, s[0] + diff + 1):
			if (i, y) not in grid and (i, y) not in beacons_set:
				grid.add((i, y))
				res += 1

print(res)

# Part 2
x_min, x_max = y_min, y_max = (0, 4000000)
res = 0
for y in range(y_min, y_max + 1):
	x_hit = []
	for s, b in lines:
		manhattan = abs(s[0] - b[0]) + abs(s[1] - b[1])
		if abs(s[1] - y) <= manhattan:
			diff = manhattan - abs(s[1] - y)
			x_hit.append((max(s[0] - diff, x_min), min(s[0] + diff, x_max)))
	# find union of x_hit (discrete)
	x_hit.sort()
	for i in range(len(x_hit) - 1):
		if x_hit[i][1] >= x_hit[i + 1][0] - 1: # -1 because discrete eg 8],[9 intersect
			x_hit[i + 1] = (x_hit[i][0], max(x_hit[i][1], x_hit[i + 1][1]))
			x_hit[i] = None
		else:
			# no intersection with next interval so point missed by all sensors
			res = (x_hit[i][1]+1, y)
			break
	if res:
		break
	
print(4000000*res[0] + res[1])
