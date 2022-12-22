data = open("22.txt").read()
board, instructions = data.split("\n\n")
board = [list(row) for row in board.split("\n")]

new = [int(instructions[0])]
for char in instructions[1:]:
	if char in "LR":
		new.append(char)
		new.append(0)
	else:
		new[-1] = new[-1] * 10 + int(char)
instructions = new

curr_pos = None

for i, row in enumerate(board):
	for j, col in enumerate(row):
		if col == ".":
			curr_pos = (i, j)
			break
	if curr_pos is not None:
		break

y, x = curr_pos
dy, dx = 0, 1
for i, ins in enumerate(instructions):
	if i % 2 == 0:
		for _ in range(ins):
			ny, nx = y+dy, x+dx
			old_dy, old_dx = dy, dx
			#traverse net of cube
			if ny < 0 and 50 <= nx < 100 and dy == -1:
				dy, dx = 0, 1
				ny, nx = nx + 100, 0
			elif nx < 0 and 150 <= ny < 200 and dx == -1:
				dy, dx = 1, 0
				ny, nx = 0, ny - 100
			elif ny < 0 and 100 <= nx < 150 and dy == -1:
				ny, nx = 199, nx - 100
			elif ny >= 200 and 0 <= nx < 50 and dy == 1:
				ny, nx = 0, nx + 100
			elif nx >= 150 and 0 <= ny < 50 and dx == 1:
				dx = -1
				ny, nx = 149 - ny, 99
			elif nx == 100 and 100 <= ny < 150 and dx == 1:
				dx = -1
				ny, nx = 149 - ny, 149
			elif ny == 50 and 100 <= nx < 150 and dy == 1:
				dy, dx = 0, -1
				ny, nx = nx - 50, 99
			elif nx == 100 and 50 <= ny < 100 and dx == 1:
				dy, dx = -1, 0
				ny, nx = 49, ny + 50
			elif ny == 150 and 50 <= nx < 100 and dy == 1:
				dy, dx = 0, -1
				ny, nx = nx + 100, 49
			elif nx == 50 and 150 <= ny < 200 and dx == 1:
				dy, dx = -1, 0
				ny, nx = 149, ny - 100
			elif ny == 99 and 0 <= nx < 50 and dy == -1:
				dy, dx = 0, 1
				ny, nx = nx + 50, 50
			elif nx == 49 and 50 <= ny < 100 and dx == -1:
				dy, dx = 1, 0
				ny, nx = 100, ny - 50
			elif nx == 49 and 0 <= ny < 50 and dx == -1:
				dx = 1
				ny, nx = 149 - ny, 0
			elif nx < 0 and 100 <= ny < 150 and dx == -1:
				dx = 1
				ny, nx = 149 - ny, 50

			if board[ny][nx] == "#":
				dy, dx = old_dy, old_dx
				break
			y, x = ny, nx
	else: # rotate
		if ins == "L":
			dy, dx = -dx, dy
		else:
			dy, dx = dx, -dy

facing = {(0,1): 0, (-1,0): 1, (0,-1): 2, (1,0): 3}
print(y+1, x+1, facing[dy, dx])
res = 1000*(y+1) + 4*(x+1) + facing[dy, dx]
print(res)
