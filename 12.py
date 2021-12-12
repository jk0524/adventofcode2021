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

	neighbor = defaultdict(lambda: [])
	# for x in lst[0].split(',')
	for x in lst:
		l = x.split('-')
		neighbor[l[0]].append(l[1])
		neighbor[l[1]].append(l[0])

	seen = set()
	fringe = [('start', ['start'], False)] # state, path
	while fringe:
		state, path, twice = fringe.pop()

		if tuple(path) in seen:
			continue
		seen.add(tuple(path))
		if state == 'end':
			r += 1
			continue

		for n in neighbor[state]:
			p = path[:]
			p.append(n)
			if n == 'start':
				continue
			if twice:
				if n.islower() and n in path:
					continue
				fringe.append((n, p, twice))
			else:
				if n.islower() and n in path:
					fringe.append((n, p, True))
				else:
					fringe.append((n, p, twice))
			
			
	return r

cache = dict()

lst = process('input')
x = solve(lst)
print(x, tuple([1,2]))
pyperclip.copy(x)
