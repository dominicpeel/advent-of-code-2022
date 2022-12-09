data = open("9.txt").read().strip()
instructions = [x.split(" ") for x in data.split("\n")]

translate = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
H_pos, T_pos = [0, 0], [0, 0]
visited = set()

for instruction, move in instructions:
	for i in range(int(move)):
		H_pos[0] += translate[instruction][0]
		H_pos[1] += translate[instruction][1]
		
		if H_pos[0] == T_pos[0] and abs(H_pos[1] - T_pos[1]) > 1:
			T_pos[1] += 1 if H_pos[1] > T_pos[1] else -1
		elif H_pos[1] == T_pos[1] and abs(H_pos[0] - T_pos[0]) > 1:
			T_pos[0] += 1 if H_pos[0] > T_pos[0] else -1
		elif abs(H_pos[0] - T_pos[0]) > 1 or abs(H_pos[1] - T_pos[1]) > 1:
			T_pos[0] += 1 if H_pos[0] > T_pos[0] else -1
			T_pos[1] += 1 if H_pos[1] > T_pos[1] else -1
		
		visited.add(tuple(T_pos))

print(len(visited))

#part b
knots = [[0,0] for i in range(10)]
visited = set()

for instruction, move in instructions:
	for i in range(int(move)):
		knots[0][0] += translate[instruction][0]
		knots[0][1] += translate[instruction][1]

		for i in range(1, len(knots)):
			if knots[i][0] == knots[i-1][0] and abs(knots[i][1] - knots[i-1][1]) > 1:
				knots[i][1] += 1 if knots[i-1][1] > knots[i][1] else -1
			elif knots[i][1] == knots[i-1][1] and abs(knots[i][0] - knots[i-1][0]) > 1:
				knots[i][0] += 1 if knots[i-1][0] > knots[i][0] else -1
			elif abs(knots[i][0] - knots[i-1][0]) > 1 or abs(knots[i][1] - knots[i-1][1]) > 1:
				knots[i][0] += 1 if knots[i-1][0] > knots[i][0] else -1
				knots[i][1] += 1 if knots[i-1][1] > knots[i][1] else -1
		
		visited.add(tuple(knots[-1]))
	
print(len(visited))