import re
import pyperclip
from collections import defaultdict, deque
import tqdm
import math
import heapq

def process(filename):
	f = open(filename, 'r')
	content = f.read()

	return content.splitlines()


def get_blocks(lst):
	blocks = []
	block = []
	for x in lst:
		if len(x) == 0:
			blocks.append(block)
			block = []
		else:
			block.append(x)

	return blocks

def grid(m):
	return

def solve(lst):
	r = 0

	# for x in lst[0].split(',')
	m = [[int(c) for c in x] for x in lst]

	M = [[0 for _ in range(5 * len(m[0]))] for _ in range(5 * len(m))]


	for i in range(5):
		for j in range(5):
			for x in range(len(m)):
				for y in range(len(m[0])):
					a = m[x][y] + i + j
					if a > 9:
						a = a % 9
					M[i * len(m) + x][j * len(m[0]) + y] = a

			

	


	fringe = []
	heapq.heappush(fringe, (0, (0, 0)))
	seen = set()
	while fringe:
		c, cur = heapq.heappop(fringe)
		if cur in seen:
			continue
		seen.add(cur)
		if cur == (len(M) - 1, len(M[len(M) - 1]) - 1):
			return c

		for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
			i, j = cur[0] + dx, cur[1] + dy
			if i < 0 or i == len(M):
				continue
			if j < 0 or j == len(M[0]):
				continue

			heapq.heappush(fringe, (c + M[i][j], (i, j)))

	return r

cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
