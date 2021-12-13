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
	i = lst.index('')

	m = set([(int(x.split(',')[0]), int(x.split(',')[1])) for x in lst[:i]])

	for f in lst[i + 1:]:
		f = f.split()[-1]
		z = int(f[2:])
		new_m = set()
		if f[0] == 'x':
			for x, y in m:
				if x < z:
					new_m.add((x, y))
				else:
					new_m.add((z - (x - z), y))
		else:
			for x, y in m:
				if y < z:
					new_m.add((x, y))
				else:
					new_m.add((x, 2 * z - y))

		m = new_m
	
	for i in range(100, -1, -1):
		s = ''
		for j in range(10):
			if (i, j) in m:
				s += '*'
			else:
				s += '_'
		print(s)


	return len(m)

cache = dict()

lst = process('input')
x = solve(lst)
print(x, tuple([]))
pyperclip.copy(x)
