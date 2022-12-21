

data = open("20.txt").read().strip()
# data = """1
# 2
# -3
# 3
# -2
# 0
# 4"""
lines = [int(x) for i, x in enumerate(data.split("\n"))]
dkey = 811589153
N = len(lines)

class Node: # doubly linked list
	def __init__(self, val, prev=None, next=None):
		self.val = val
		self.prev = prev
		self.next = next

linkedlist = [Node(dkey*x) for x in lines]
for a, b in zip(linkedlist, linkedlist[1:]):
	a.next = b
	b.prev = a

for i in range(N):
	linkedlist[i].next = linkedlist[(i+1) % N]
	linkedlist[(i+1) % N].prev = linkedlist[i]

linkedlist[0].prev = linkedlist[-1] # make it circular
linkedlist[-1].next = linkedlist[0]

for _ in range(10):
	for x in linkedlist:
		#del at current
		x.prev.next = x.next
		x.next.prev = x.prev

		a = x.prev
		b = x.next
		move = x.val % (N-1)
		for _ in range(move):
			a = a.next
			b = b.next
		
		#insert between a and b
		x.prev = a
		x.next = b
		a.next = x
		b.prev = x

	# print(x.val, x.prev.val, x.next.val)

# find 0 index
curr = linkedlist[0]
while curr.val != 0:
	curr = curr.next

res = 0
for _ in range(3):
	for _ in range(1000):
		curr = curr.next
	res += curr.val
print(res)