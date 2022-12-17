from functools import cache
from collections import deque
import re
import bisect

data = open("16.txt").read().strip()
lines = [x for x in data.split("\n")]

valves = {x[0].split(" ")[1]: {"fr":int(x[0].split("=")[1]), "next": re.findall(r"[A-Z]{2}", x[1])} for line in lines for x in [line.split("; ")]}
for valve, obj in valves.items():
	valves[valve]["next"] = [(x, 1) for x in obj["next"]]
print(valves, "\n\n")

# #draw graph
import networkx as nx
import matplotlib.pyplot as plt

# G = nx.Graph()
# for valve in valves:
# 	G.add_node(valve, fr=valves[valve]["fr"])
# 	for next_valve in valves[valve]["next"]:
# 		G.add_edge(valve, next_valve[0], weight=next_valve[1])

# pos = nx.spring_layout(G, seed=3)
# nx.draw(G, pos, node_size=1000, node_color="w")

# nx.draw_networkx_labels(G, pos, font_size=10, verticalalignment="top", horizontalalignment="right")
# fr_labels = nx.get_node_attributes(G, "fr")
# nx.draw_networkx_labels(G, pos, fr_labels, font_size=10, verticalalignment="bottom", horizontalalignment="left")
# edge_labels = nx.get_edge_attributes(G, "weight")
# nx.draw_networkx_edge_labels(G, pos, edge_labels)

# ax = plt.gca()
# ax.margins(0.08)
# plt.show()
# plt.clf()

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
print(len(valves), "\n\n")

#draw graph
H = nx.Graph()
for valve in valves:
	H.add_node(valve, fr=valves[valve]["fr"])
	for next_valve in valves[valve]["next"]:
		H.add_edge(valve, next_valve[0], weight=next_valve[1])

pos = nx.spring_layout(H, seed=3)
nx.draw(H, pos, node_size=1000, node_color="w")

nx.draw_networkx_labels(H, pos, font_size=10, verticalalignment="top", horizontalalignment="right")
fr_labels = nx.get_node_attributes(H, "fr")
nx.draw_networkx_labels(H, pos, fr_labels, font_size=10, verticalalignment="bottom", horizontalalignment="left")
edge_labels = nx.get_edge_attributes(H, "weight")
nx.draw_networkx_edge_labels(H, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.show()

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

	if valve not in opened:
		new = list(opened)
		bisect.insort(new, valve)
		new = tuple(new)
		for (v, w) in nextv:
			vol = fr*(time_left-1)
			vol += dp(v, time_left-w-1, new)
			max_vol = max(vol, max_vol)
			
	return max_vol

print(dp("AA", time_left, ("AA")))


# Part 2
time_left = 26

# pv, ev, pt, et, opened
# create 1

@cache
def dpB(pv, ev, pt, et, opened=()):
	pfr, pnextv = valves[pv]["fr"], valves[pv]["next"]
	efr, enextv = valves[ev]["fr"], valves[ev]["next"]

	if pt <= 0 and et <= 0:
		return 0

	max_vol = 0
	if pt <= 0 or et <= 0:
		pt = pt if pt > 0 else et
		for (vp, wp) in pnextv:
			max_vol = max(dpB(vp, ev, pt-wp, 0, opened), max_vol)

		if pv not in opened:
			new = list(opened)
			bisect.insort(new, pv)
			new = tuple(new)
			for (vp, wp) in pnextv:
				vol = pfr*(pt-1)
				vol += dpB(vp, ev, pt-wp-1, 0, new)
				max_vol = max(vol, max_vol)
		

	else:
		for (vp, wp) in pnextv:
			for (ve, we) in enextv:
				max_vol = max(dpB(vp, ve, pt-wp, et-we, opened), max_vol)

		if pv not in opened:
			new = list(opened)
			bisect.insort(new, pv)
			new = tuple(new)
			for (vp, wp) in pnextv:
				for (ve, we) in enextv:
					vol = pfr*(pt-1)
					vol += dpB(vp, ve, pt-wp-1, et-we, new)
					max_vol = max(vol, max_vol)

		if ev not in opened:
			new = list(opened)
			bisect.insort(new, ev)
			new = tuple(new)
			for (vp, wp) in pnextv:
				for (ve, we) in enextv:
					vol = efr*(et-1)
					vol += dpB(vp, ve, pt-wp, et-we-1, new)
					max_vol = max(vol, max_vol)
		
		if pv not in opened and ev not in opened and pv != ev:
			new = list(opened)
			bisect.insort(new, pv)
			bisect.insort(new, ev)
			new = tuple(new)
			for (vp, wp) in pnextv:
					for (ve, we) in enextv:
						vol = pfr*(pt-1)
						vol += efr*(et-1)
						vol += dpB(vp, ve, pt-wp-1, et-we-1, new)
						max_vol = max(vol, max_vol)
				
	return max_vol

print(dpB("AA", "AA", time_left, time_left, ("AA", "AA")))

# @cache
# def dp(valve, time_left, opened=()): # need to sort opened
# 	fr, nextv = valves[valve]["fr"], valves[valve]["next"]

# 	if time_left <= 0:
# 		return 0, opened

# 	max_vol, max_new = 0, opened
# 	for (v, w) in nextv:
# 		dp_res = dp(v, time_left-w, opened)
# 		if dp_res[0] > max_vol:
# 			max_vol = dp_res[0]
# 			max_new = dp_res[1]
			

# 	if valve not in opened:
# 		new = list(opened)
# 		bisect.insort(new, valve)
# 		new = tuple(new)
# 		for (v, w) in nextv:
# 			vol = fr*(time_left-1)
# 			dp_res = dp(v, time_left-w-1, new)
# 			vol += dp_res[0]
# 			if vol > max_vol:
# 				max_vol = vol
# 				max_new = dp_res[1]
			
# 	return max_vol, max_new

# res1 = dp("AA", time_left, ("AA"))

# for valve in res1[1]:
# 	if valve != "A":
# 		valves[valve]["fr"] = 0
# reduce_graph(valves)

# res2 = dp("AA", time_left, res1[1])
# print(res1, res2)
# print(res1[0]+res2[0])
# print(res[0])

# for v in valves["AA"]["next"]:
# 	if v[0] not in res[1]:
# 		print(v[0], v[1])

# I = nx.Graph()
# for valve in valves:
# 	I.add_node(valve, fr=valves[valve]["fr"])
# 	for next_valve in valves[valve]["next"]:
# 		I.add_edge(valve, next_valve[0], weight=next_valve[1])


# vistied_nodes = []
# unvisited_nodes = []
# for valve in valves:
# 	if valve in res[1]:
# 		vistied_nodes.append(valve)
# 	else:
# 		unvisited_nodes.append(valve)

# pos = nx.spring_layout(I, seed=3)
# nx.draw_networkx_nodes(I, pos, nodelist=vistied_nodes, node_color='r', alpha=0.5)
# nx.draw_networkx_nodes(I, pos, nodelist=unvisited_nodes, node_color='b', alpha=0.5)
# nx.draw_networkx_edges(I, pos, width=1.0, alpha=0.5)
# # nx.draw_networkx_labels(I, pos, font_size=16)

# nx.draw_networkx_labels(H, pos, font_size=10, verticalalignment="top", horizontalalignment="right")
# fr_labels = nx.get_node_attributes(H, "fr")
# nx.draw_networkx_labels(H, pos, fr_labels, font_size=10, verticalalignment="bottom", horizontalalignment="left")
# edge_labels = nx.get_edge_attributes(H, "weight")
# nx.draw_networkx_edge_labels(H, pos, edge_labels)

# plt.axis('off')
# plt.show()
