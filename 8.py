data = open("8.txt").read().strip()
lines = [x for x in data.split("\n")]

res = 2*len(lines[0]) + 2*len(lines) - 4
max_score = 0

#slow and too much code but works
for i in range(1,len(lines)-1):
	for j in range(1,len(lines[i])-1):
		tree = lines[i][j]

		k = i-1
		visible = True
		while k >= 0:
			if lines[k][j] >= tree:
				visible = False
				break
			k -= 1
		if visible:
			res += 1
			continue
		k = i+1
		visible = True
		while k < len(lines):
			if lines[k][j] >= tree:
				visible = False
				break
			k += 1
		if visible:
			res += 1
			continue
		k = j-1
		visible = True
		while k >= 0:
			if lines[i][k] >= tree:
				visible = False
				break
			k -= 1
		if visible:
			res += 1
			continue
		k = j+1
		visible = True
		while k < len(lines[i]):
			if lines[i][k] >= tree:
				visible = False
				break
			k += 1
		if visible:
			res += 1
			continue
		
print(res)

for i in range(1,len(lines)-1):
	for j in range(1,len(lines[i])-1):
		tree = lines[i][j]
		curr_score = 1

		k = i-1
		while k >= 0:
			if lines[k][j] >= tree:
				k -= 1
				break
			k -= 1
		curr_score *= (k+1)-i

		k = i+1
		while k < len(lines):
			if lines[k][j] >= tree:
				k += 1
				break
			k += 1
		curr_score *= i-(k-1)

		k = j-1
		while k >= 0:
			if lines[i][k] >= tree:
				k -= 1
				break
			k -= 1
		curr_score *= (k+1)-j

		k = j+1
		while k < len(lines[i]):
			if lines[i][k] >= tree:
				k += 1
				break
			k += 1
		curr_score *= j-(k-1)

		max_score = max(max_score,curr_score)

print(max_score)