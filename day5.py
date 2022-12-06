
with open("day5.txt") as f:
	lines = f.read().splitlines()
	for i, line in enumerate(lines):
		if "1" in line:
			n = int(line.strip(" ").split(" ")[-1])
			height = i
			break
	
	stacks = [[] for i in range(n)]
	for i in range(height-1, -1, -1):
		line = lines[i]
		for j in range(n):
			if line[j*4+1:j*4+2] != " ":
				stacks[j].append(line[j*4+1:j*4+2])

	# begin instructions for part A
	# for i in range(height+2, len(lines)):
	# 	line = lines[i].split(" ")[1::2]
	# 	# move a total of line[0] crates from line[1] to line[2]
	# 	for j in range(int(line[0])):
	# 		stacks[int(line[2])-1].append(stacks[int(line[1])-1].pop())

	# begin instructions for part B
	for i in range(height+2, len(lines)):
		line = lines[i].split(" ")[1::2]
		for j in range(int(line[0]), 0, -1):
			stacks[int(int(line[2])-1)].append(stacks[int(line[1])-1].pop(-j)) 
	
	message = "".join([stack[-1] for stack in stacks])
	print(message)