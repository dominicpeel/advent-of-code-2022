from functools import cmp_to_key

data = open("13.txt").read().strip().split("\n\n")
pairs = []
for pair in data:
	pair = pair.split("\n")
	pairs.append((eval(pair[0]), eval(pair[1])))

def cmp(a, b):
	if isinstance(a, int) and isinstance(b, int):
		if a < b:
			return -1
		elif a == b:
			return 0
		else:
			return 1
	
	if isinstance(a, int):
		a = [a]
	elif isinstance(b, int):
		b = [b]
	
	for aa, bb in zip(a,b):
		comp = cmp(aa, bb)
		if comp != 0:
			return comp
	if len(a) > len(b):
		return 1
	elif len(a) == len(b):
		return 0
	else:
		return -1

# Part 1
res = 0
for i in range(len(pairs)):
	if cmp(*pairs[i]) == -1:
		res += i+1
print(res)

# Part 2
divider_packets = [[[2]], [[6]]]

packets = [*divider_packets]
for pair in pairs:
	packets.append(pair[0])
	packets.append(pair[1])

packets.sort(key=cmp_to_key(cmp))

res = 1
for i, packet in enumerate(packets):
	if packet in divider_packets:
		res *= i+1
print(res)