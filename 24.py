import re
import pyperclip
from collections import defaultdict, deque
import tqdm
import math
import heapq
from itertools import permutations, product
import numpy as np
import copy
import random

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

def solve_block(block, i, z):
	m = defaultdict(int)
	m['z'] = z
	# print(block)
	for x in block:
		# print(x)
		# print(m)
		a = x[4]
		num = re.findall(r'-?\d+', x)

		if num:
			b = eval(num[0])
		elif len(x) > 5:
			b = m[x[6]]
		# print(a, b)
		if x[:3] == 'inp':
			m[a] = i
		elif x[:3] == 'add':
			m[a] += b
		elif x[:3] == 'mul':
			m[a] = m[a] * b
		elif x[:3] == 'div':
			m[a] = m[a] // b
		elif x[:3] == 'mod':
			m[a] = m[a] % b
		elif x[:3] == 'eql':
			m[a] = int(m[a] == b)
	return m['z']

def check_num(num, blocks):
	dig = [int(c) for c in str(num)]
	print(len(dig))
	if 0 in dig:
		return None
	z = 0
	for j in range(len(dig)):
		z = solve_block(blocks[j], dig[j], z)
	return z

def solve(lst):
	result = 0
	
	blocks = []
	block = []
	for x in lst:
		if x[:3] == 'inp':
			if block:
				blocks.append(block)
			block = []
			block.append(x)
		else:
			block.append(x)
	blocks.append(block)
	
	# lst = []
	# for i in range(len(blocks)):
	# 	for input_w in range(9, 0, -1):
	# 		# print(i, input_w)
	# 		if solve_block(blocks[i], input_w) == 0:
	# 			lst.append(input_w)
	# 			break
	# x = int(''.join([str(9) for _ in range(14)]))



	# for i in tqdm.tqdm(range(x, 0, -1)):
	# 	dig = [int(c) for c in str(i)]
	# 	if 0 in dig:
	# 		continue
	# 	m = defaultdict(int)
	# 	for j in range(len(blocks)):
	# 		m = solve_block(blocks[j], dig[j], m)
	# 	if m['z'] == 0:
	# 		return i

	# for i in range(1, 10):
	# 	m = defaultdict(int)
	# 	m = solve_block(blocks[0], i, m)
	# 	for j in range(1, 10):
	# 		m = solve_block(blocks[1], j, m)
	# 		print(i, j, m)
	# return int(''.join([str(x) for x in lst]))
	right = int(''.join([str(9) for _ in range(14)]))
	left = int(''.join([str(2) for _ in range(14)]))

	# result = []
	# while left < right:
	# 	print(left, right)
	# 	while check_num(left, blocks) is None:
	# 		left += 1
	# 	while check_num(right, blocks) is None:
	# 		right -= 1

	# 	mid = (left + right) // 2
	# 	l = check_num(left, blocks)
	# 	r = check_num(right, blocks)
	# 	m = check_num(mid, blocks)
	# 	if l == 0:
	# 		result.append(left)
	# 	if r == 0:
	# 		result.append(right)
	# 	if m == 0:
	# 		result.append(m)
	# 	if l < r:
	# 		right = mid
	# 	else:
	# 		left = mid

	# for i in range(100):
	# 	print(i + left, check_num(i + left, blocks))
	start = 0
	print(check_num(999269959719, blocks))
	# for i in range(1, 9):
	# 	for j in range(1, 9):
	# 		for k in range(1, 9):
				# lst = [i, j, k]
				# m = defaultdict(int)
				# for l in range(len(lst)):
				# 	m = solve_block(blocks[start + l], lst[l])
	r = []
	for p1 in product([i for i in range(1, 10)], repeat = 3):
		print(p1)
		z = 0
		for l in range(len(p1)):
			z = solve_block(blocks[start + l], p1[l], z)

		w1 = force_w(blocks[start + len(p1)], z)
		if not w1:
			continue
		z = solve_block(blocks[len(p1)], w1, z)
		# return p1, f

		for p2 in product([i for i in range(1, 10)], repeat = 3):
			z_p2 = z
			for j in range(len(p2)):
				z_p2 = solve_block(blocks[len(p1) + 1 + j], p2[j], z_p2)
			w2 = force_w(blocks[1 + len(p1) + len(p2)], z_p2)
			if not w2:
				continue
			z_p2 = solve_block(blocks[1 + len(p1) + len(p2)], w2, z_p2)
			# return (p1, p2, f)
			
			
			for p3 in range(1, 10):
				z_p3 = z_p2
				z_p3 = solve_block(blocks[len(p1) + len(p2) + 2], p3, z_p3)

				# w = force_w(blocks[len(p1) + len(p2) + 3], z_p3)
				# if not w:
				# 	continue
				# z_p3 = solve_block(blocks[len(p1) + len(p2) + 3], w, z_p3)
				# f.append(w)
				
				# w = force_w(blocks[len(p1) + len(p2) + 4], z_p3)
				# if not w:
				# 	continue
				# f.append(w)
				# z_p3 = solve_block(blocks[len(p1) + len(p2) + 4], w, z_p3)

				# w = force_w(blocks[len(p1) + len(p2) + 5], z_p3)
				# print('force 3', p1, p2, p3, z_p3, w)
				# # return (p1, p2, p3, f, w)
				# if not w:
				# 	continue
				# f.append(w)
				# z_p3 = solve_block(blocks[len(p1) + len(p2) + 5], w, z_p3)
				# print('fyee', p1, p2, p3, z_p3)
				# return (p1, p2, p3, f)
				last_w = []
				for k in range(5):
					w = force_w(blocks[len(p1) + len(p2) + 3 + k], z_p3)
					if not w:
						break
					z_p3 = solve_block(blocks[len(p1) + len(p2) + 3 + k], w, z_p3)
					last_w.append(w)

				if len(last_w) == 5:
					r.append((p1, p2, p3, [w1, w2] + last_w))
					return r
	print(force_w(blocks[11], {'w': 1, 'x': 0, 'z': 16654, 'y': 0}))
	# 	# print(p, m['z'])
	# 	# if m['z'] == 0:
	# 	r.append(m['z'])
	# print(sorted(r)[::-1])
	# z = 1
	# block_index = 5
	# for i in range(1, 9):
	# 	m = defaultdict(int)
	# 	m['z'] = z
	# 	print(z, i, solve_block(blocks[block_index], i, m)['z'])

	return result

def force_w(block, z):
	for i in range(1, 10):
		if solve_block(block, i, z) <= z // 26:
			return i



cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
