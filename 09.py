import re
import pyperclip
from collections import defaultdict, deque
import tqdm
import math

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


def solve(lst):
	r = 0
	
	# for x in lst[0].split(',')
	m = [[int(c) for c in x] for x in lst]
	lows = []
	# print(m)

	for i in range(len(m)):
		for j in range(len(m[i])):
			low = True
			for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
				if i + dx < 0 or i + dx == len(m):
					continue
				if j + dy < 0 or j + dy == len(m[i]):
					continue
				if m[i + dx][j + dy] <= m[i][j]:
					low = False
					break
			if low:
				r += m[i][j] + 1
				lows.append((i, j))

	sizes = []
	for i, j in lows:
		size = 0
		fringe = [(i, j)]
		seen = set()
		while fringe:
			cur = fringe.pop()

			x, y = cur
			print(x, y)
			if cur in seen:
				continue
			seen.add(cur)
			size += 1
			for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
				if x + dx < 0 or x + dx == len(m):
					continue
				if y + dy < 0 or y + dy == len(m[x]):
					continue
				if m[x + dx][y + dy] < 9:
					fringe.append((x + dx, y + dy))

		sizes.append(size)

	r = 1
	for x in sorted(sizes)[-3:]:
		r *= x

	return r

cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
