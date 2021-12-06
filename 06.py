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
	d = defaultdict(int)

	l = []
	for x in lst[0].split(','):
		l.append(int(x))


	k = 256
	for x in set(l):
		d[x] = one(x, k)
		# for j in tqdm.tqdm(range(k)):
		# 	add = []
		# 	for i in range(len(l)):
		# 		if l[i] == 0:
		# 			l[i] = 6
		# 			add.append(8)
		# 		else:
		# 			l[i] -= 1
		# 	l.extend(add)

		# d[x] = len(l)
	cnt = 0
	for x in l:
		cnt += d[x]
	return cnt

cache = dict()
def one(x, time):
	global cache
	if (x, time) in cache:
		return cache[(x, time)]
	if time < 0:
		return 0
	cnt = math.ceil(max(0, time - x) / 7)
	s = 0
	for i in range(0, cnt):
		s += one(8, time - x - i * 7 - 1)

	cache[(x, time)] = s + 1
	return s + 1

lst = process('input')
x = solve(lst)
pyperclip.copy(x)
