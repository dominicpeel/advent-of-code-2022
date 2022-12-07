import requests
import sys

session = open("session.txt").read()

day = sys.argv[1]
cookie = {"session": session}
inp = requests.get(f"https://adventofcode.com/2022/day/{day}/input", cookies=cookie).text
with open(f"{day}.txt", "w") as f:
	f.write(inp)