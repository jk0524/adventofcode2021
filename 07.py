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
	r = 99999999999999999
	lst = [int(x)for x in lst[0].split(',')]

	for i in range(min(lst), max(lst)+ 1):
		y = [abs(x - i) * (1 + abs(x - i)) // 2 for x in lst]
		c = sum(y)
		if c < r:
			print(lst[i])
			print(y)
		r = min(r, c)


	return r

cache = dict()

lst = process('input')
x = solve(lst)
pyperclip.copy(x)
