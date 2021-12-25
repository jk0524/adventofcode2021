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

def move_right(m):
	move = dict()
	for i in range(len(m)):
		for j in range(len(m[i])):
			if m[i][j] == '>':
				next_j = (j + 1) % len(m[i])
				if m[i][next_j] == '.':
					move[(i, j)] = (i, next_j)


	for i, j in move:
		i, next_j = move[(i, j)]
		m[i][j] = '.'
		m[i][next_j] = '>'

	return len(move) > 0

def move_down(m):
	move = dict()
	for i in range(len(m)):
		for j in range(len(m[i])):
			if m[i][j] == 'v':
				next_i = (i + 1) % len(m)
				if m[next_i][j] == '.':
					move[(i, j)] = (next_i, j)


	for i, j in move:
		next_i, j = move[(i, j)]
		m[i][j] = '.'
		m[next_i][j] = 'v'

	return len(move) > 0


def solve(lst):
	result = 0
	
	m = [[c for c in l] for l in lst]
	for i in range(1000):
		r = move_right(m)
		d = move_down(m)
		if not r and not d:
			return i + 1

	return result

cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
