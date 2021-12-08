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
	
	# for x in lst[0].split(',')
	for x in lst:
		a = x.split('|')
		mapping = dict()
		l = [None for _ in range(10)]
		for e in a[0].split():
			e = ''.join(sorted([c for c in e]))
			if len(e) == 2:
				mapping[e] = 1
				l[1] = e
			elif len(e) == 3:
				mapping[e] = 7
				l[7] = e
			elif len(e) == 7:
				mapping[e] = 8
				l[8] = e
			elif len(e) == 4:
				mapping[e] = 4
				l[4] = e

		top = (set([c for c in l[7]]) - set([c for c in l[1]])).pop()
		diff = (set([c for c in l[4]]) - set([c for c in l[1]]))
		L = set([diff.pop(), diff.pop()])
		for e in a[0].split():
			if len(e) not in [2, 3, 7, 4]:
				s = set([c for c in e])
				e = ''.join(sorted([c for c in e]))
				# e = set([c for c in e])
				if len(e) == 6: # 6 or 9 or 0
					if L.issubset(s):
						if set([c for c in l[1]]).issubset(s):
							mapping[e] = 9
							l[9] = e
						else:
							mapping[e] = 6
							l[9] = 6
					else:
						mapping[e] = 0
						l[0] = e

				elif len(e) == 5: # 2, 5, 3
					if set([c for c in l[1]]).issubset(s):
							mapping[e] = 3
							l[3] = e
					else:
						if L.issubset(s):
							mapping[e] = 5
							l[5] = e
						else:
							mapping[e] = 2
							l[2] = e

		r += int(''.join([str(y) for y in [mapping[''.join(sorted([c for c in e]))] for e in a[1].split()]]))

	return r

cache = dict()

lst = process('input')
x = solve(lst)
print(x, sorted('321'))
pyperclip.copy(x)
