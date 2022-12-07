from collections import deque

with open("6.txt") as f:
	line = f.readline()
	
	#part A
	q = deque(line[:3]) 
	for i in range(3, len(line)):
		q.append(line[i])
		if len(set(q)) == 4:
			start_of_packet = i+1
			break
		
		q.popleft()

	print(start_of_packet)

	#part B
	q = deque(line[:13])
	for i in range(13, len(line)):
		q.append(line[i])
		if len(set(q)) == 14:
			start_of_message = i+1
			break
		
		q.popleft()
	
	print(start_of_message)