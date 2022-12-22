import sympy

with open("21.txt") as f:
	data = f.read().strip()

lines = [x.split(": ") for x in data.split("\n")]
lines = {x[0]: x[1] for x in lines}

def dfs(exp, p=1):
	if p == 2 and exp == "humn":
		return sympy.Symbol("humn")
	exp = lines[exp]
	if "+" in exp:
		a, b = exp.split(" + ")
		return dfs(a, p) + dfs(b, p)
	elif "-" in exp:
		a, b = exp.split(" - ")
		return dfs(a, p) - dfs(b, p)
	elif "*" in exp:
		a, b = exp.split(" * ")
		return dfs(a, p) * dfs(b, p)
	elif "/" in exp:
		a, b = exp.split(" / ")
		return dfs(a, p) / dfs(b, p)
	return int(exp)

print(dfs("root"))

lhs, rhs = lines["root"].split(" + ")
lhs, rhs = dfs(lhs, p=2), dfs(rhs, p=2)
res = sympy.solve(lhs - rhs, sympy.Symbol("humn"))
print(res[0])
