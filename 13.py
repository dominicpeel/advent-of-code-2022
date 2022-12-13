from functools import cmp_to_key

data = open("13.txt").read().strip()
lines = [x for x in data.split("\n") if len(x)]

def compare(a, b):
	if isinstance(a, int) and isinstance(b, int):
		if a < b:
			return True
		elif a == b:
			return "cont"
		else:
			return False
	elif isinstance(a, list) and isinstance(b, list):
		for i in range(len(a)):
			if i >= len(b):
				return False
			comp = compare(a[i], b[i])
			if comp == True:
				return True
			elif comp == False:
				return False
		if len(a) == len(b):
			return "cont"
		return True
	elif isinstance(a, int):
		return compare([a], b)
	else:
		return compare(a, [b])

def parse_line(line):
	stack = [[]]
	for i in range(len(line)):
		if line[i] == "[":
			stack.append([])
		elif line[i] == "]":
			stack[-2].append(stack.pop())
		elif line[i] == ",":
			continue
		else:
			start = i
			while line[i+1] in "0123456789":
				i += 1
			stack[-1].append(int(line[start:i+1]))
	return stack[0][0]

for i, line in enumerate(lines):
	lines[i] = parse_line(line)

# Part A
res = 0
for i in range(0, len(lines), 2):
	if compare(lines[i], lines[i+1]):
		res += (i//2)+1
print(res)

# Part B
divider_packets = [[[2]], [[6]]]
for d in divider_packets:
	lines.append(d)

def cmp(a, b):
	if compare(a, b):
		return -1
	elif compare(b, a):
		return 1
	return 0
lines.sort(key=cmp_to_key(cmp))

res = 1
for i, line in enumerate(lines):
	if line in divider_packets:
		res *= i+1
print(res)