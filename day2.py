score = 0

with open("day2.txt", "r") as f:
	
	for line in f.readlines():
		elf, player = line[:-1].split(" ")

		if player == "X":
			score += 1
			if elf == "A":
				score += 3
			elif elf == "C":
				score += 6
		elif player == "Y":
			score += 2
			if elf == "B":
				score += 3
			elif elf == "A":
				score += 6
		elif player == "Z":
			score += 3
			if elf == "C":
				score += 3
			elif elf == "B":
				score += 6
	
print(score)

# part b
score = 0

with open("day2.txt", "r") as f:
	# rock = 1, paper = 2, scissors = 3
	for line in f.readlines():
		elf, outcome = line[:-1].split(" ")

		if outcome == "X":
			#0 score for loss
			if elf == "A":
				# elf chooses rock so choose sissors
				score += 3
			elif elf == "B":
				# elf chooses paper so choose rock
				score += 1
			elif elf == "C":
				# elf chooses scissors so choose paper
				score += 2
		elif outcome == "Y":
			# 3 score for draw
			score += 3
			if elf == "A":
				# elf chooses rock so choose rock
				score += 1
			elif elf == "B":
				# elf chooses paper so choose paper
				score += 2
			elif elf == "C":
				# elf chooses scissors so choose scissors
				score += 3
		else:
			# 6 score for win
			score += 6
			if elf == "A":
				# elf chooses rock so choose paper
				score += 2
			elif elf == "B":
				# elf chooses paper so choose scissors
				score += 3
			else:
				# elf chooses scissors so choose rock
				score += 1
	
print(score)