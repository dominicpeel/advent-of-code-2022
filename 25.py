data = open("25.txt").read().strip()
translate = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
res = sum([sum([translate[y] * (5**i) for i, y in enumerate(x[::-1])]) for x in data.split("\n")])

SNAFU = ""
for i in range (25, 0, -1):
	if 5**i <= res:
		break

for j in range(i, -1, -1):
	smallest_diff = (0, 1e20)
	for k, v in translate.items():
		if abs(res - v*(5**j)) < smallest_diff[1]:
			smallest_diff = (k, abs(res - v*(5**j)))
	res -= translate[smallest_diff[0]]*(5**j)
	SNAFU += str(smallest_diff[0])
	
print("".join(SNAFU))
