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
	for i in range(len(m)):
		for j in range(len(m[i])):
			for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
				if i + dx < 0 or i + dx == len(m):
					continue
				if j + dy < 0 or j + dy == len(m[i]):
					continue


def solve(lst):
	r = 0
	
	# for x in lst[0].split(',')
	m = {')': 3, ']': 57, '}': 1197, '>': 25137}
	p = {')': '(', ']': '[', '}': '{', '>': '<'}
	s = {'(': 1, '[': 2, '{': 3, '<': 4}
	t = []

	for x in lst:
		q = []
		dead = False
		for i in range(len(x)):
			if x[i] in ['(', '[', '{', '<']:
				q.append(x[i])
			else:
				if p[x[i]] == q[-1]:
					q.pop()
				else:
					r += m[x[i]]
					dead = True
					break

		if q and not dead:
			total = 0
			for j in q[::-1]:
				total *= 5
				total += s[j]
			t.append(total)
	print(t)



	return sorted(t)[len(t) // 2]

cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
