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

class Region:
	def __init__(self, x, y, z, val):
		self.x = x
		self.y = y
		self.z = z
		self.val = val
		#self.children = [] # regions that are contained by this region

	def contain(self, region):
		return self.left <= region.left and self.right >= region.right

	def intersection(self, region):
		x = max(self.x[0], region.x[0]), min(self.x[1], region.x[1])
		y = max(self.y[0], region.y[0]), min(self.y[1], region.y[1])
		z = max(self.z[0], region.z[0]), min(self.z[1], region.z[1])
		
		if x[0] > x[1] or y[0] > y[1] or z[0] > z[1]:
			return None
		return Region(x, y, z, -self.val)

	def total(self):
		return (self.x[1] - self.x[0] + 1) * (self.y[1] - self.y[0] + 1) * (self.z[1] - self.z[0] + 1) * self.val


def find_regions(single_lst):
	lst = []



def solve(lst):
	result = 0
	region_lst = []
	m = defaultdict(int)
	# cut = 100000
	# for x in range(cut, cut):
	# 	for y in range(-cut, cut):
	# 		pass
	for l in lst:
		a = [eval(b) for b in re.findall(r'-?\d+', l)]

		if l[:2] == 'on':
			s = 1
		else:
			s = 0
		x = a[0], a[1]
		y = a[2], a[3]
		z = a[4], a[5]
		region = Region(x, y, z, s)
		new_lst = []
		for r in region_lst:
			i = r.intersection(region)
			if i:
				new_lst.append(i)
		if s:
			region_lst.append(region)
		for r in new_lst:
			region_lst.append(r)

	return sum([r.total() for r in region_lst])



cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
