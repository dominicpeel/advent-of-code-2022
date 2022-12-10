data = open("10.txt").read().strip()
lines = [x.split(" ") for x in data.split("\n")]
#noop 1 cycle, do nothing
#addx = 3 takes 2 cycles add 3 to x at end of cycle
#addx = 5 takes 2 cycles add 5 to x at end of cycle

x = 1
cycle = 0

#consider 20th cycle and 40 cycles after that
#signal strength = cycle * x
#Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.
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

sprite_w = 3
dims = [40,6]

#If the sprite is positioned such that one of its three pixels is the pixel currently being drawn, 
# the screen produces a lit pixel (#); otherwise, the screen leaves the pixel dark (.).
canvas = [["." for i in range(dims[0])] for j in range(dims[1])]
# print(canvas)
#x is the x position of the sprite
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