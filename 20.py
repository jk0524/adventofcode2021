import re
import pyperclip
from collections import defaultdict

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

def enhance(m, a, outside):
	output = defaultdict(int)
	min_i, min_j = 0, 0
	max_i, max_j = 0, 0
	for i, j in m:
		min_i = min(min_i, i)
		max_i = max(max_i, i)
		min_j = min(min_j, j)
		max_j = max(max_j, j)

	o = 1
	for i in range(min_i - o, max_i + o + 1):
		for j in range(min_j - o, max_j + o + 1):
			s = ''
			for dx in [-1, 0, 1]:
				for dy in [-1, 0, 1]:
					if (i + dx, j + dy) in m:
						s = s + str(m[(i + dx, j + dy)])
					else:
						s = s + outside
				
			index = int(s, 2)
		# print(index)
			output[(i, j)] = a[index]
	# 		if i == 0 and j == 1:
	# 			print(s)
	# 		print(index, a[index])
	# print(output)
	return output



def solve(lst):
	r = 0
	a = [int(x == '#') for x in lst[0]]
	# print(a)

	m = dict()

	lst = lst[2:]
	for i in range(len(lst)):
		for j in range(len(lst[i])):
			m[(i, j)] = int(lst[i][j] == '#')

	for _ in range(25):
		m = enhance(m, a, '0')
		m = enhance(m, a, '1')
	# print(m)
	return len([1 for k in m if m[k] == 1])

def p_m(m):
	for i in range(10):
		s = ''
		for j in range(10):
			s += '#' if m[(i, j)] else '.'
		# print(s)

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
