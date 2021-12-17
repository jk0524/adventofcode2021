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
	# for x in lst
	y_s = set()
	for y_0 in range(-123, 2000):
		t = 0
		m_y = 0
		found = False
		while True:
			y = f(y_0, t)
			m_y = max(m_y, y)
			if y >= -122 and y <= -74:
				y_s.add(y_0)
				break
			elif y < -122:
				break
			else:
				t += 1

	a = set()

	for y_0 in tqdm.tqdm(y_s):
		for x_0 in range(1, 300):
			t = 0
			while True:
				x = fx(x_0, t)
				y = f(y_0, t)
				if y >= -122 and y <= -74 and x >= 185 and x <= 221:
					a.add((x_0, y_0))
					r += 1
					break
				elif y < -122:
					break
				else:
					t += 1
	print(a)
	return r

def f(y_0, t):
	return (1 + t) * (2 * y_0 - t) / 2

def fx(x_0, t):
	if t > x_0:
		t = x_0
	return (1 + t) * (2 * x_0 - t) / 2	


cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
