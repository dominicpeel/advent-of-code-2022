"""   --------Part 1---------   --------Part 2---------
Day       Time    Rank  Score       Time    Rank  Score
 19   10:33:40    5032      0   16:00:31    5996      0
"""
import re
from functools import cache

data = open("19.txt").read().strip()
# data = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
# Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""

nums = re.compile(r"-?\d+")
costs = [[int(x) for x in nums.findall(line)] for line in data.split("\n")]
for i, line in enumerate(costs):
	costs[i] = tuple([line[1], line[2], (line[3], line[4]), (line[5], line[6])])

# print(costs) #ore r cost, clay r cost, obsidian cost (ore, clay), geode cost (ore, obsidian)

T = 24

best = 0
@cache
def dfs(t, bp, bal=bytes((0,0,0,0)), rs=bytes((1,0,0,0))):
	global best

	ub = bal[3] + t*rs[3] + ((t*(t+1))//2)
	if ub < best:
		return 0
	
	if t == 0:
		if bal[3] > best:
			best = bal[3]
		return bal[3]
	
	if t < 2:
		if bal[3]+rs[3] > best:
			best = bal[3]+rs[3]
		return bal[3]+rs[3]

	if rs[0] >= costs[bp][3][0] and rs[2] >= costs[bp][3][1]:
		print(t, bp, bal, rs, "max geode output")
		bal = list(bal)
		rs = list(rs)
		while t > 0:
			bal[3] += rs[3]
			rs[3] += 1
			t -= 1
		return bal[3]

	new_bal = list(bal)
	for i, r in enumerate(rs):
		new_bal[i] += r

	if bal[0] >= costs[bp][3][0] and bal[2] >= costs[bp][3][1]:
		return dfs(t-1, bp, (new_bal[0]-costs[bp][3][0], new_bal[1], new_bal[2]-costs[bp][3][1], new_bal[3]), (rs[0], rs[1], rs[2], rs[3]+1))


	if not (bal[0] >= costs[bp][0] or bal[0] >= costs[bp][1] or (bal[0] >= costs[bp][2][0] and bal[1] >= costs[bp][2][1])): # can't 
		return dfs(t-1, bp, (new_bal[0], new_bal[1], new_bal[2], new_bal[3]), (rs[0], rs[1], rs[2], rs[3]))
	
	max_geodes = bal[3]
	if rs[2] < costs[bp][3][1]: # if no. of obsidian r's < obsidian cost of geode r
		if bal[0] >= costs[bp][2][0] and bal[1] >= costs[bp][2][1]: # if can afford obsidian r
			max_geodes = max(max_geodes, dfs(t-1, bp, (new_bal[0]-costs[bp][2][0], new_bal[1]-costs[bp][2][1], new_bal[2], new_bal[3]), (rs[0], rs[1], rs[2]+1, rs[3])))
	if rs[1] < costs[bp][2][1]: # if no. of clay r's < clay cost of obsidian r
		if bal[0] >= costs[bp][1]: # if can afford clay r
			max_geodes = max(max_geodes, dfs(t-1, bp, (new_bal[0]-costs[bp][1], new_bal[1], new_bal[2], new_bal[3]), (rs[0], rs[1]+1, rs[2], rs[3])))
	if rs[0] < max((costs[bp][0], costs[bp][1], costs[bp][2][0], costs[bp][3][0])): # if no. of ore r's < ore cost of any r
		if bal[0] >= costs[bp][0]:
			max_geodes = max(max_geodes, dfs(t-1, bp, (new_bal[0]-costs[bp][0], new_bal[1], new_bal[2], new_bal[3]), (rs[0]+1, rs[1], rs[2], rs[3])))
	if not (bal[0] >= costs[bp][0] and bal[0] >= costs[bp][1] and (bal[0] >= costs[bp][2][0] and bal[1] >= costs[bp][2][1])): # if 
		max_geodes = max(max_geodes, dfs(t-1, bp, (new_bal[0], new_bal[1], new_bal[2], new_bal[3]), (rs[0], rs[1], rs[2], rs[3])))
	return max_geodes

# Part 1
res = 0
for i in range(len(costs)):
	geodes = dfs(T, i)
	res += (i+1)*geodes
	# print(f'{(i+1)/len(costs) * 100 :.2f} %', i+1, geodes, (i+1)*geodes)
	dfs.cache_clear()
	best = 0

print(res)

# Part 2
T = 32
costs = costs[:3]
res = 1	
for i in range(len(costs)):
	geodes = dfs(T, i)
	res *= geodes
	# print(f'{(i+1)/len(costs) * 100 :.2f} %', i+1, geodes, res)
	dfs.cache_clear()
	best = 0

print(res)