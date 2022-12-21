"""   --------Part 1---------   --------Part 2---------
Day       Time    Rank  Score       Time    Rank  Score
 21   00:10:58     896      0   00:36:19     867      0
"""
data = open("21.txt").read().strip()
lines = [x.split(": ") for x in data.split("\n")]
lines = {x[0]: x[1] for x in lines}


# Part 1
def dfs(exp):
	exp = lines[exp]
	if "+" in exp:
		a, b = exp.split(" + ")
		res_a, res_b = dfs(a), dfs(b)
		return res_a + res_b
	if "-" in exp:
		a, b = exp.split(" - ")
		return dfs(a) - dfs(b)
	if "*" in exp:
		a, b = exp.split(" * ")
		return dfs(a) * dfs(b)
	if "/" in exp:
		a, b = exp.split(" / ")
		return dfs(a) / dfs(b)
	return int(exp)

print(dfs("root"))

# Part 2

lines["root"] = lines["root"].replace("+", "-")
exp = dfs("root")
print(exp)

l, r = 0, 42083915370029
res = -1
# BS
while l < r:
	mid = (l + r) // 2
	lines["humn"] = str(mid)
	res = dfs("root")
	if res == 0:
		print(mid)
		break
	elif res > 0:
		l = mid + 1
	else:
		r = mid
