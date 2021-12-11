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

def grid(m):
	return


def solve(lst):
	r = 0
	
	# for x in lst[0].split(',')
	m = [[int(c) for c in x] for x in lst]
	print(m)

	for t in range(10000):
		f = [[False for _ in m[0]] for j in m]

		flash = False
		for i in range(len(m)):
			for j in range(len(m[i])):
				m[i][j] += 1
				if m[i][j] > 9:
					flash = True
		while flash:

			flash = False
			for i in range(len(m)):
				for j in range(len(m[i])):
					if m[i][j] > 9 and not f[i][j]:
						f[i][j] = True
						r += 1
						for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
							if i + dx < 0 or i + dx == len(m):
								continue
							if j + dy < 0 or j + dy == len(m[i]):
								continue

							m[i + dx][j + dy] += 1
							if m[i + dx][j + dy] > 9 and not f[i + dx][j + dy]:
								flash = True

		c = 0
		for i in range(len(m)):
			for j in range(len(m[i])):
				if f[i][j]:
					m[i][j] = 0
					c += 1
		if c == 100:
			return t + 1

	return r

cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
