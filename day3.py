res = 0
badges = 0

with open("day3.txt", "r") as f:
	j = 0
	for line in f.readlines():
		line = line[:-1]
		if j % 3 == 0:
			seen_chars = set(line)
			print(seen_chars)
		elif j % 3 == 1:
			seen_chars = seen_chars.intersection(set(line))
			print(seen_chars)
		else:
			for i in range(len(line)):
				if line[i] in seen_chars:
					if line[i].isupper():
						badges += ord(line[i]) - ord('A') + 27
					else:
						badges += ord(line[i]) - ord('a') + 1
					break

		j += 1

		half = len(line) // 2
		seen = set(line[:half])

		for i in range(half, len(line)):
			if line[i] in seen:
				common = line[i]
				break

		if common.isupper():
			res += ord(common) - ord('A') + 27
		else:
			res += ord(common) - ord('a') + 1

print(res, badges)