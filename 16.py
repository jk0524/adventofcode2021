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
	m = {
	'0': '0000',
	'1': '0001',
	'2': '0010',
	'3': '0011',
	'4': '0100',
	'5': '0101',
	'6': '0110',
	'7': '0111',
	'8': '1000',
	'9': '1001',
	'A': '1010',
	'B': '1011',
	'C': '1100',
	'D': '1101',
	'E': '1110',
	'F': '1111',
	}
	s = ''.join([m[x] for x in lst[0]])

	nodes = e(s)
	root = nodes[0]
	parent = root
	for i in range(1, len(nodes)):

		n = nodes[i]
		n.parent = parent
		parent.children.append(n)
		parent = n

		while parent.complete() and not parent == root:
			parent = parent.parent

	# print(root.len_type, root.val, len(root.children), root.complete())
	# print(root)
	return eval_node(root)

def eval_node(root):
	if root.t == 4:
		return root.val
	vals = [eval_node(c) for c in root.children]
	if root.t == 0:
		return sum(vals)
	if root.t == 1:
		p = 1
		for v in vals:
			p *= v
		return p
	if root.t == 2:
		return min(vals)
	if root.t == 3:
		return max(vals)
	if root.t == 5:
		return int(vals[0] > vals[1])
	if root.t == 6:
		return int(vals[0] < vals[1])
	if root.t == 7:
		return int(vals[0] == vals[1])

class Node:
	def __init__(self, version, t):
		self.version = version
		self.t = t
		self.val = None
		self.children = []
		self.len_type = None
		self.parent = None
		self.size = None

	def __repr__(self, level=0):
		ret = "\t"*level+"Node " + repr((self.t, self.val, self.len_type, self.size))+"\n"
		for child in self.children:
			ret += child.__repr__(level+1)
		return ret

	def complete(self):
		if self.len_type == 0:
			complete = self.val == sum([c.total_size() for c in self.children])
		else:
			complete = self.val == len(self.children)

		return self.t == 4 or complete

	def total_size(self):
		return self.size + sum([c.total_size() for c in self.children])


def e(s):
	i = 0
	nodes = []
	while i < len(s) - 6:
		start = i
		version = int(s[i:i + 3], 2)
		t = int(s[i + 3:i + 6], 2)
		i += 6
		root = Node(version, t)
		if t == 4:
			r = ''
			while int(s[i]) == 1:
				r += s[i + 1: i + 5]
				i += 5
			r += s[i + 1: i + 5]
			i += 5
			root.val = int(r, 2)
		else:
			length_type = int(s[i])
			i += 1
			if length_type == 0:
				o = int(s[i:i + 15], 2)
				i += 15
				root.len_type = 0
				root.val = o
			else:
				o = int(s[i:i + 11], 2)
				i += 11
				root.len_type = 1
				root.val = o
				
		root.size = i - start
		nodes.append(root)	
	return nodes

			


cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
