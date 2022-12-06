res = [0,0]

with open("day4.txt", "r") as f:
	for line in f.readlines():
		#split line at "," and "-"
		first, second = line.split(",")

		first = first.split("-")
		second = second.split("-")

		#if second if contained in first or first is contained in second
		if int(first[0]) <= int(second[0]) <= int(second[1]) <= int(first[1]) or int(second[0]) <= int(first[0]) <= int(first[1]) <= int(second[1]):
			res[0] += 1

		#if overlap at all
		if int(first[0]) <= int(second[0]) <= int(first[1]) or int(second[0]) <= int(first[0]) <= int(second[1]):
			res[1] += 1

print(res)