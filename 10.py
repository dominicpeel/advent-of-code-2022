#      --------Part 1---------   --------Part 2---------
#Day       Time    Rank  Score       Time    Rank  Score
# 10   00:12:28    1699      0   00:40:51    3893      0

data = open("10.txt").read().strip()
lines = [x.split(" ") for x in data.split("\n")]

x = 1
cycle = 0
res = 0
for line in lines:
	if line[0] == "noop":
		cycle += 1
		if cycle % 40 == 20:
			res += cycle * x
	elif line[0] == "addx":
		for i in range(2):
			cycle += 1
			if cycle % 40 == 20:
				res += cycle * x
		x += int(line[1])
print(res)


dims = [40,6]
canvas = [["." for i in range(dims[0])] for j in range(dims[1])]

x = 1
cycle = 0 #crt pos
for line in lines:
	if line[0] == "noop":
		if abs(x-cycle) < 2:
			canvas[-1][cycle] = "#"

		cycle += 1

		if cycle == 40:
			canvas += [["." for i in range(dims[0])]]
			cycle = 0
		
	elif line[0] == "addx":
		for i in range(2):
			if abs(x-cycle) < 2:
				canvas[-1][cycle] = "#"

			cycle += 1

			if cycle == 40:
				canvas += [["." for i in range(dims[0])]]
				cycle = 0

		x += int(line[1])

for row in canvas[-8:]:
	print("".join(row))