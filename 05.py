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


def solve(lst):
	r = 0
	covered = defaultdict(int)
	for x in lst:
		lst = [int(i) for i in re.findall(r'\d+', x)]
		p1 = lst[:2]
		p2 = lst[2:]

		if p1[0] == p2[0] or p1[1] == p2[1]:
			if p1[0] == p2[0]:
				for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
					covered[(p1[0], y)] += 1
			else:
				for y in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
					covered[(y, p1[1])] += 1
		else:
			print(p1, p2)
			diff = max(p1[1], p2[1]) - min(p1[1], p2[1])
			

			if p1[0] < p2[0]:
				x_i = 1
			else:
				x_i = -1
			if p1[1] < p2[1]:
				y_i = 1
			else:
				y_i = -1

			for i in range(diff + 1):
				# print((min(p1[0], p2[0]) + i, min(p1[1], p2[1]) + i))
				covered[(p1[0] + i * x_i, p1[1]+ i * y_i)] += 1


	return len([x for x in covered if covered[x] > 1])

lst = process('input')
x = solve(lst)
pyperclip.copy(x)
