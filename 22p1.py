"""   --------Part 1---------   --------Part 2---------
Day       Time    Rank  Score       Time    Rank  Score
 22   08:44:41    8110      0   11:30:16    4082      0
slept in 
"""

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

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
rotate = {"L": -1, "R": 1}

curr_dir = 0
curr_pos = None

for i, row in enumerate(board):
	for j, col in enumerate(row):
		if col == ".":
			curr_pos = (i, j)
			break
	if curr_pos is not None:
		break

dir_chars = ">v<^"

y, x = curr_pos
dy, dx = dirs[curr_dir]
for i, ins in enumerate(instructions):
	if i % 2 == 0: # move
		for _ in range(ins):
			if 0 <= y+dy < len(board) and 0 <= x+dx < len(board[y+dy]):
				if board[y+dy][x+dx] == "." or board[y+dy][x+dx] in dir_chars:
					x += dx
					y += dy
					board[y][x] = dir_chars[curr_dir]
					continue
				elif board[y+dy][x+dx] == "#":
					break
			orig_pos = (y, x)
			curr_dir = (curr_dir + 2)%4 # 180
			dy, dx = dirs[curr_dir]
			while True:
				if y+dy < 0 or y+dy >= len(board) or x+dx < 0 or x+dx >= len(board[y+dy]) or board[y+dy][x+dx] == " ":
					if board[y][x] == "#":
						# wall blocking path
						y, x = orig_pos
					curr_dir = (curr_dir + 2)%4
					dy, dx = dirs[curr_dir]
					break
				y += dy
				x += dx

	else: # rotate
		curr_dir = (curr_dir + rotate[ins])%4
		dy, dx = dirs[curr_dir]

with open("path.txt", "w") as f:
	for row in board:
		f.write("".join(row) + "\n")

facing = {(0,1): 0, (-1,0): 1, (0,-1): 2, (1,0): 3}
print(y+1, x+1, facing[dy, dx])
res = 1000*(y+1) + 4*(x+1) + facing[dy, dx]
print(res)
