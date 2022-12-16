import re

data = open("15.txt").read().strip()
sensors = [[int(x) for x in re.findall(r"-?\d+", y)] for y in data.split("\n")]

md = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])

# Part 1
y = 2000000
intervals = []
beacons = set()
for line in sensors:
	sx, sy, bx, by = line
	if md((sx, sy), (bx, by)) >= abs(sy - y):
		diff = md((sx, sy), (bx, by)) - abs(sy - y)
		intervals.append((sx - diff, sx + diff))
	if by == y:
		beacons.add(bx)

intervals.sort()
q = []
for l, r in intervals:
	if q and l-1 <= q[-1][1]:
		q[-1][1] = max(q[-1][1], r)
	else:
		q.append([l, r])

cannot = set()
for l, r in q:
	for i in range(l, r + 1):
		if i not in beacons:
			cannot.add(i)

print(len(cannot))

# Part 2 no z3
bound = 4_000_000

pos, neg = set(), set()
for line in sensors:
	sx, sy, bx, by = line
	r = abs(sx - bx) + abs(sy - by)
	pos.add(sy-sx+r+1)
	pos.add(sy-sx-r-1)
	neg.add(sy+sx+r+1)
	neg.add(sy+sx-r-1)

res = []
for a in pos:
	for b in neg:
		p = ((b-a)//2, (b+a)//2)
		if all(0 < c < bound for c in p):
			if all(md(p, (sx,sy)) > md((sx,sy),(bx,by)) for sx, sy, bx, by in sensors):
				res = p
				break
	if res:
		break

print(res[0] * bound + res[1])


# Part 2 using z3
from z3 import *

r = {}
for sx, sy, bx, by in sensors:
	r[(sx, sy)] = md((sx, sy), (bx, by))

s = Solver()
x, y = Int('x'), Int('y')

s.add(x >= 0)
s.add(x <= bound)
s.add(y >= 0)
s.add(y <= bound)

for sx, sy, bx, by in sensors:
	s.add(Abs(sx-x)+Abs(sy-y) > r[(sx, sy)])

a = s.check()
m = s.model()
res = m[x].as_long(), m[y].as_long()

print(res[0] * bound + res[1])
