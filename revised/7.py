from collections import defaultdict

data = open("7.txt").read().strip()
lines = [x for x in data.split("\n")]

size = defaultdict(int)
path = []
for line in lines:
	line = line.split()
	if line[1] == "cd":
		if line[2] == "..":
			path.pop()
		else:
			path.append(line[2])
	elif line[1] == "ls":
		continue
	elif line[0] == "dir":
		continue
	else:
		file_size = int(line[0])
		for i in range(1,len(path)+1):
			size["/".join(path[:i])] += file_size

print(sum([v for k,v in size.items() if v <= 100000]))
 
max_space = 70000000 - 30000000
curr_space = size["/"]
min_path = curr_space
for k,v in size.items():
	if curr_space - v <= max_space:
		min_path = min(min_path, v)
print(min_path)