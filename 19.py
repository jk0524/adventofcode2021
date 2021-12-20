import re
import pyperclip
from collections import defaultdict, deque
import tqdm
import math
import heapq
from itertools import permutations, product
import numpy as np

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
	blocks.append(block)
	return blocks

def sub(x, y):
	return tuple(map(lambda i, j: i - j, x, y))

def add(x, y):
	return tuple(map(lambda i, j: i + j, x, y))

def orientations():
	lst = []
	for p in permutations([0, 1, 2]):
		for sign in product([1, -1], repeat=3):
			lst.append((sign, p))

	return lst

def apply_orient(x, orientation):
	sign, permutation = orientation
	r = [x[i] * sign[i] for i in range(len(x))]

	return tuple([r[i] for i in permutation])

def merge(left_scanner, right_scanner):
	left_scanner = sorted(left_scanner)
	l_set = set(left_scanner)
	m_cnt = 0
	for o in orientations():
		right = sorted([apply_orient(x, o) for x in right_scanner])
		for i in range(len(left_scanner)):
			for j in range(len(right)):
				cnt = 0
				left_x = left_scanner[i]
				right_x = right[j]
				offset = sub(left_x, right_x)
				for x in right:
					if add(x, offset) in l_set:
						cnt += 1
						m_cnt = max(m_cnt, cnt)

				if cnt >= 12:
					return left_scanner + [add(r, offset) for r in right if add(r, offset) not in l_set]
	# print(m_cnt)
	return None

def solve(lst):
	result = 0

	# for x in lst[0].split(',')

	lst = get_blocks(lst)
	for i in range(len(lst)):
		l = lst[i]
		l = l[1:]
		l = [eval(x) for x in l]
		lst[i] = l



	
	mapping = dict()
	for i in range(len(lst)):
		for j in tqdm.tqdm(range(len(lst))):
			if i == j:
				continue
			m = merge2(lst[i], lst[j])
			if m:
				if i not in mapping:
					mapping[i] = dict()
				mapping[i][j] = m

	r = set(lst[0])

	for i in range(1, len(lst)):
		p = path(i, mapping)

		l = lst[i]
		for j in range(len(p) - 1):
			from_index, to_index = p[j], p[j + 1]
			offset, o = mapping[to_index][from_index]
			l = [add(offset, apply_orient(x, o)) for x in l]
		for x in l:
			r.add(x)

	max_d = 0
	scanners = []
	for i in range(1, len(lst)):
		p = path(i, mapping)
		l = [(0,0,0)]
		for j in range(len(p) - 1):
			from_index, to_index = p[j], p[j + 1]
			offset, o = mapping[to_index][from_index]
			l = [add(offset, apply_orient(x, o)) for x in l]
		scanners.append(l[0])

	for s in scanners:
		for c in scanners:
			max_d = max(max_d, sum([abs(s[i] - c[i]) for i in range(3)]))
	return max_d


	# d = dict() # from scan i to scan j
	# for i, j in mapping:
	# 	offset, orient = mapping[(i, j)]
	# 	if i not in d:
	# 		d[i] = dict()
	# 	if j not in d:
	# 		d[j] = dict()
	# 	d[j][i] = offset, orient
	# 	d[i][j] = apply_orient(tuple(np.subtract((0, 0, 0), offset)), orient), orient

	# print(mapping)
	# r = set(lst[0])

	# for i in range(1, len(lst)):
	# 	p = path(i, d)
	# 	print(p)
	# 	l = lst[i]
	# 	for j in range(len(p) - 1):
	# 		from_index, to_index = p[j], p[j + 1]
	# 		offset, o = d[from_index][to_index]
	# 		l = [add(offset, apply_orient(x, o)) for x in l]

	# 	for x in l:
	# 		r.add(x)
	# print(d)
	# print(path(1, d))
	return len(r)
	# return 0

def path(start, mapping, end=0):
	fringe = [[start]]
	seen = set()
	while True:
		cur = fringe.pop()
		if cur[-1] in seen:
			continue
		seen.add(cur[-1])
		if cur[-1] == end:
			return cur
		for k in mapping[cur[-1]]:
			c = cur[:]
			c.append(k)
			fringe.append(c)


def merge2(left_scanner, right_scanner):
	left_scanner = sorted(left_scanner)
	l_set = set(left_scanner)
	m_cnt = 0
	for o in orientations():
		right = sorted([apply_orient(x, o) for x in right_scanner])
		for i in range(len(left_scanner)):
			for j in range(len(right)):
				cnt = 0
				left_x = left_scanner[i]
				right_x = right[j]
				offset = sub(left_x, right_x)
				for x in right:
					l = add(x, offset)
					if l in l_set and l[0] <= 1000 and l[1] <= 1000 and l[2] <= 1000:
						cnt += 1
						m_cnt = max(m_cnt, cnt)

				if cnt >= 12:
					return offset, o
	# print(m_cnt)
	return None

def merge_lists(lst1, lst2):
	return lst1 + [x for x in lst2 if x not in lst1]


cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
