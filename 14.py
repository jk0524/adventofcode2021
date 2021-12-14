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
	m = lst[0]
	d = dict()
		
	for x in lst[2:]:
		a = x.split(' -> ')
		c = a[0]
		b = a[1]
		d[c] = b
	
	ones = defaultdict(int)
	pairs = defaultdict(int)
	for i in range(len(m) - 1):
		pairs[m[i: i + 2]] += 1


	for _ in range(40):
		new_pairs = defaultdict(int)
		for p in pairs:
			if p in d:
				c = d[p]
				new_pairs[p[0] + c] += pairs[p]
				new_pairs[c + p[1]] += pairs[p]
			else:
				new_pairs[p] += pairs[p]
		pairs = new_pairs

	print(pairs)
	# for _ in tqdm.tqdm(range(5)):
	# 	n = []
	# 	for i in range(len(m)):
	# 		if m[i:i+2] in d:
	# 			n.append(m[i])
	# 			n.append(d[m[i:i + 2]])
	# 		else:
	# 			n.append(m[i])
	# 	m = ''.join(n)

	d = defaultdict(int)
	for p in pairs:
		d[p[0]] += pairs[p]
		d[p[1]] += pairs[p]
	
	d[m[0]] = (d[m[0]] - 1) // 2 + 1
	d[m[-1]] = (d[m[-1]] - 1) // 2 + 1
	for c in d:
		if c not in (m[0], m[-1]):
			d[c] = d[c] // 2

	return (max(d.values()) - min(d.values()))

cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
