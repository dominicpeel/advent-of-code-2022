data = open("9.txt").read().strip()
instructions = [x.split(" ") for x in data.split("\n")]

translate = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

knots = [[0,0] for i in range(10)]
visited = [set(), set()] #part a, part b

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
		
		visited[0].add(tuple(knots[1]))
		visited[1].add(tuple(knots[-1]))
	
print(len(visited[0]))
print(len(visited[1]))