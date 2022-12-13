import matplotlib.pyplot as plt
import numpy as np

data = open("12.txt").read().strip()
grid = [list(x) for x in data.split("\n")]

x = np.arange(0, len(grid), 1)
y = np.arange(0, len(grid[0]), 1)
xx, yy = np.meshgrid(x, y)
zz = np.zeros((len(grid), len(grid[0])))

for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] == "S":
			zz[i][j] = 0
		elif grid[i][j] == "E":
			zz[i][j] = 25
		else:
			zz[i][j] = ord(grid[i][j]) - ord('a')

fig, ax = plt.subplots()
ax.imshow(zz,interpolation='none', cmap='viridis')
plt.show()

