total_disk_space = 70000000
needed_disk_space = 30000000

def dir_size(files, total=0):
	res = 0
	for k, v in files.items():
		if k == "dirs":
			for dirname, _dir in v.items():
				size = dir_size(_dir, total)
				res += size[0]["size"]
				total = size[1]
		elif k == "files":
			for filename, _file in v.items():
				res += int(_file)
	files["size"] = res
	if res <= 100000:
		total += res
	return files, total

def find_smallest_dir(files, min_dir, need_to_delete):
	if need_to_delete <= files["size"] < min_dir:
		min_dir = files["size"]
	for k, v in files.items():
		if k == "dirs":
			for dirname, _dir in v.items():
				min_dir = find_smallest_dir(_dir, min_dir, need_to_delete)
	return min_dir

with open("day7.txt") as f:
	files = {"dirs": {}, "files": {}}
	files["dirs"]["/"] = {"dirs": {}, "files": {}}
	dir_stack = [files]
	curr_dir = files
	for line in f:
		line = line[:-1].split(" ")
		if line[0] == "$":
			if line[1] == "cd":
				if line[2] == "..":
					curr_dir = dir_stack.pop()
				else:
					dir_stack.append(curr_dir)
					curr_dir = curr_dir["dirs"][line[2]]
		elif len(line) == 2:
			if line[0] == "dir":
				curr_dir["dirs"][line[1]] = {"dirs": {}, "files": {}}
			else:
				curr_dir["files"][line[1]] = line[0]

	files, total = dir_size(files)
	print(total)

	current_disk_space = files["size"]
	need_to_delete = current_disk_space - total_disk_space + needed_disk_space
	print(find_smallest_dir(files, files["size"], need_to_delete))