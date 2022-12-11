#      --------Part 1---------   --------Part 2---------
#Day       Time    Rank  Score       Time    Rank  Score
# 11   00:54:06    5112      0   01:03:38    2867      0

data = open("11.txt").read().strip()
lines = [x.strip() for x in data.split("\n")]

lines = [lines[i:i+6] for i in range(0, len(lines), 7)]
translated = []
item_locations = [[] for i in range(len(lines))]
for monkey, commands in enumerate(lines):
	for i, command in enumerate(commands):
		if command[0] == "S":
			item_locations[monkey] = command.split(": ")[1].split(", ")
		elif command[0] == "O":
			op = command.split(": ")[1].split(" = ")[1].split(" ")
		elif command[0] == "T":
			test = int(command.split(": ")[1].split(" ")[-1])
		elif command[3] == "t":
			truth = int(command.split(" ")[-1])
		elif command[3] == "f":
			false = int(command.split(" ")[-1])
	translated.append([op, test, truth, false])


modulo = 1
for command in translated:
	modulo *= command[1]

inspections = [0 for i in range(len(translated))]
for _ in range(10000):
	for idx, command in enumerate(translated):
		op, test, truth, false = command
		items = item_locations[idx]
		for worrylevel in items:
			inspections[idx] += 1
			new_op = []
			for i in range(0, 3, 2):
				if op[i] == "old":
					new_op.append(worrylevel)
				else:
					new_op.append(op[i])
			if op[1] == "+":
				worrylevel = int(new_op[0]) + int(new_op[1])
			else:
				worrylevel = int(new_op[0]) * int(new_op[1])
			worrylevel %= modulo #change to worrylevel //= 3 for part a
			if worrylevel % test == 0:
				item_locations[truth].append(worrylevel)
			else:
				item_locations[false].append(worrylevel)
		item_locations[idx] = []

inspections.sort()
print(inspections[-1]*inspections[-2])