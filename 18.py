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

def solve(lst):
	r = 0

	# for x in lst[0].split(',')
	lst = [eval(x) for x in lst]

	r = lst[0]
	# f = flatten(r)
	# m = dict()
	# n, _ = parse(r, m)
	# # nn, s = explode(n, f, m)
	# print(split(n))
	# print(recreate(n))
	for i in range(1, len(lst)):
		l = lst[i]
		r = [r, l]

		red = True
		while red:
			print(r)
			f = flatten(r)
			m = dict()
			n, _ = parse(r, m)
			n, s = explode(n, f, m)
			if s:
				print("explode")
				r = recreate(n)
				continue
			red = split(n)
			if red:
				print("split")
			r = recreate(n)

		print(r)

	m = dict()
	print(r)
	n, _ = parse(r,m)
	

	
	return final_sum(n)

def final_sum(root):
	s = 0
	if root.isRegLeft():
		s += root.left[0] * 3
	else:
		s += 3 * final_sum(root.left)
	if root.isRegRight():
		s += root.right[0] * 2
	else:
		s += 2 * final_sum(root.right)
	return s


class Node:
	def __init__(self, level):
		self.level = level
		self.left = None
		self.right = None
		self.parent = None

	def isRegular(self):
		return type(self.left) == tuple and type(self.right) == tuple

	def isRegLeft(self):
		return type(self.left) == tuple

	def isRegRight(self):
		return type(self.right) == tuple

	def __repr__(self, level=0):
		ret = "\t"*level+ f'node level:{self.level}'
		if self.isRegLeft():
			ret += f' left: {self.left}'
		if self.isRegRight():
			ret += f' right: {self.right}'
		
		ret += "\n"
		for child in [self.left, self.right]:
			if not type(child) == tuple:
				ret += child.__repr__(level+1)
		return ret

def parse(pair, mapping, level=0, i=0):
	root = Node(level)
	if type(pair[0]) == int:
		mapping[i] = root
		root.left = (pair[0], i)
		i += 1
	else:
		root.left, i = parse(pair[0], mapping, level=level + 1, i=i)
		root.left.parent = root
		
	if type(pair[1]) == int:
		mapping[i] = root
		root.right = (pair[1], i)
		i += 1
	else:
		root.right, i = parse(pair[1], mapping, level=level + 1, i=i)
		root.right.parent = root

	return root, i

def split(root):
	if root.isRegLeft() and root.left[0] >= 10:
		n = Node(root.level + 1)
		n.left = root.left[0] // 2, 0
		n.right = root.left[0] // 2 + root.left[0] % 2, 0
		root.left = n
		return True

	if root.isRegRight() and root.right[0] >= 10:
		n = Node(root.level + 1)
		n.left = root.right[0] // 2, 0
		n.right = root.right[0] // 2 + root.right[0] % 2, 0
		root.right = n
		return True

	if not root.isRegLeft():
		s = split(root.left)
		if s:
			return True
	if not root.isRegRight():
		return split(root.right)

	return False



def recreate(root):
	lst = []
	if root.isRegLeft():
		lst.append(root.left[0])
	else:
		lst.append(recreate(root.left))
	if root.isRegRight():
		lst.append(root.right[0])
	else:
		lst.append(recreate(root.right))
	return lst

def flatten(lst):
	a = []
	for i in lst:
		if type(i) == list:
			a.extend(flatten(i))
		else:
			a.append(i)
	return a

def explode(root, flatten_lst, mapping):
	if root.level == 4:
		l, i = root.left
		if i > 0:
			n = mapping[i - 1]
			if n.isRegLeft() and n.left[1] == i - 1:
				n.left = (n.left[0] + l, i)
				
			elif n.isRegRight() and n.right[1] == i - 1:
				n.right = (n.right[0] + l, i)


		r, i = root.right
		if i < len(flatten_lst) - 1:
			n = mapping[i + 1]

			if n.isRegLeft() and n.left[1] == i + 1:
				n.left = (n.left[0] + r, i)

			elif n.isRegRight() and n.right[1] == i + 1:
				n.right = (n.right[0] + r, i)
		return (0, 0), True

	if root.isRegular():
		return root, False
	if not root.isRegLeft():
		# print("YEYE", root.left)
		l, s = explode(root.left, flatten_lst, mapping)
		root.left = l
		if s:
			return root, s
		# if not root.isRegRight():
		# 	r, s = explode(root.right, flatten_lst, mapping)
		# 	root.right = r
		# 	return root, s

	if not root.isRegRight():
		# print("YEYYE", root.right)
		r, s = explode(root.right, flatten_lst, mapping)
		root.right = r
		return root, s

	return root, False






cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
