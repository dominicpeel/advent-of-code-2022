import matplotlib.pyplot as plt
import numpy as np

data = open("18.txt").read().strip()
lines = [tuple([int(y) for y in x.split(",")]) for x in data.split("\n")]

minmax = [[lines[0][0], lines[0][0]], [lines[0][1], lines[0][1]], [lines[0][2], lines[0][2]]]
for line in lines:
	for i in range(3):
		if line[i] < minmax[i][0]:
			minmax[i][0] = line[i]
		elif line[i] > minmax[i][1]:
			minmax[i][1] = line[i]
mx, my, mz = minmax[0], minmax[1], minmax[2]
maxr = max(mx[1]-mx[0], my[1]-my[0], mz[1]-mz[0])

# 3d voxel plot
voxels = np.zeros((maxr+1, maxr+1, maxr+1), dtype=bool)
for x,y,z in lines:
	voxels[x-mx[0], y-my[0], z-mz[0]] = True

ax = plt.figure().add_subplot(projection='3d')
ax.voxels(voxels, facecolors='purple', edgecolor='k')
ax.set_aspect('equal')

plt.savefig("18vis.png", bbox_inches='tight', pad_inches=0, dpi=300)