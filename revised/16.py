"""   --------Part 1---------   --------Part 2---------
Day       Time    Rank  Score       Time    Rank  Score
 16   17:16:41   12087      0   22:58:27    8985      0
"""

from functools import cache
import re
import bisect
from time import time

now = time()

data = open("16.txt").read().strip()
lines = [x for x in data.split("\n")]

valves = {x[0].split(" ")[1]: {"fr":int(x[0].split("=")[1]), "next": re.findall(r"[A-Z]{2}", x[1])} for line in lines for x in [line.split("; ")]}
for valve, obj in valves.items():
	valves[valve]["next"] = [(x, 1) for x in obj["next"]]
# print(valves, "\n\n")

# compress graph by removing fr 0 nodes
def reduce_graph(graph):
	to_remove = []
	for valve, obj in graph.items():
		fr, nextv = obj["fr"], obj["next"]
		if valve != "AA" and fr == 0:
			for i, (v, w) in enumerate(nextv):
				for j, (v2, w2) in enumerate(nextv):
					if v2 != v:
						graph[v]["next"].append((v2, w2+w))
				graph[v]["next"].remove((valve, w))

			to_remove.append(valve)
	for valve in to_remove:
		del graph[valve]
	return graph


valves = reduce_graph(valves)

# Part 1
time_left = 30

# use opened valves as a tuple for memoization
# but store a set of opened valves for quick lookup

@cache
def dp(valve, time_left, opened=()):
	fr, nextv = valves[valve]["fr"], valves[valve]["next"]

	if time_left <= 0:
		return 0

	max_vol = 0
	for (v, w) in nextv:
		max_vol = max(dp(v, time_left-w, opened), max_vol)

	if valve not in opened and fr > 0:
		new = list(opened)
		bisect.insort(new, valve)
		new = tuple(new)
		for (v, w) in nextv:
			vol = fr*(time_left-1)
			vol += dp(v, time_left-w-1, new)
			max_vol = max(vol, max_vol)
			
	return max_vol

print(dp("AA", time_left))


# Part 2
time_left = 26

@cache
def dp2(valve, timer, opened=tuple(["AA"]), E=False):
	fr, nextv = valves[valve]["fr"], valves[valve]["next"]

	if timer <= 0:
		if not E:
			# once player stops, do search for elephant
			res = dp2("AA", time_left, opened, True)
			
			return res
		else:
			return 0

	max_vol = 0
	for (v, w) in nextv:
		max_vol = max(dp2(v, timer-w, opened, E), max_vol)

	if valve not in opened:
		new = list(opened)
		bisect.insort(new, valve)
		new = tuple(new)
		for (v, w) in nextv:
			vol = fr*(timer-1)
			vol += dp2(v, timer-w-1, new, E)
			max_vol = max(vol, max_vol)
			
	return max_vol

print(dp2("AA", time_left))

print(time()-now)
