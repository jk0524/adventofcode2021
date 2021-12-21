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

dice = 0
def roll():
	global dice
	dice = (dice % 100) + 1
	return dice

def neighbors(p1_score, p2_score, p1_pos, p2_pos, turn, track):
	lst = []
	for r, cnt in [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]:
		if turn == 0:
			old_p2_score = p2_score - track[p2_pos]
			old_p2_pos = (p2_pos - r) % len(track)
			lst.append((p1_score, old_p2_score, p1_pos, old_p2_pos, 1 - turn, cnt))
		else:
			old_p1_score = p1_score - track[p1_pos]
			old_p1_pos = (p1_pos - r) % len(track)
			lst.append((old_p1_score, p2_score, old_p1_pos, p2_pos, 1 - turn, cnt))
	return lst

def combs():
	s = defaultdict(int)
	for i in range(1, 4):
		for j in range(1,4):
			for k in range(1, 4):
				s[i + j + k] += 1
	return [(k, s[k]) for k in s]

def num(state, start, track):
	if state == start:
		return 1
	p1_score, p2_score, p1_pos, p2_pos, turn = state
	return sum([num((p1_s, p2_s, p1_p, p2_p, t), start, track) * cnt for p1_s, p2_s, p1_p, p2_p, t, cnt in neighbors(p1_score, p2_score, p1_pos, p2_pos, turn, track)])


def solve(lst):
	result = 0

	scores = [0, 0]
	players = [7, 6]
	turn = 0
	track = [i + 1 for i in range(10)]
	# cnt = 0

	# while max(scores) < 1000:
	# 	r = sum([roll() for _ in range(3)])
	# 	print(r)
	# 	players[turn] = (players[turn] + r) % len(track)
	# 	scores[turn] += track[players[turn]]
	# 	turn = 1 - turn
	# 	cnt += 3


	# print(scores, cnt)
	# return cnt * min(scores)
	m = defaultdict(int) # player 1 score, player 2 score, player 1 pos, player 2 pos, turn
	start = (0, 0, 7, 6, 0)
	m[start] = 1
	for p1_score in range(1, 31):
		for p2_score in range(1, 31):
			for p1_pos in range(10):
				for p2_pos in range(10):
					for turn in [0, 1]:
						for p1_s, p2_s, p1_p, p2_p, t, _ in neighbors(p1_score, p2_score, p1_pos, p2_pos, turn, track):
							if (p1_s, p2_s, p1_p, p2_p, t) == (0, 0, 7, 6, 0):
								print(p1_score, p2_score, p1_pos, p2_pos, turn)
						m[(p1_score, p2_score, p1_pos, p2_pos, turn)] = sum([m[p1_s, p2_s, p1_p, p2_p, t] * cnt for p1_s, p2_s, p1_p, p2_p, t, cnt in neighbors(p1_score, p2_score, p1_pos, p2_pos, turn, track)])


	# print(neighbors(12, 13, 2, 3, 0, track))
	# seen = set()
	# fringe = [(0, 0, 7, 6, 0)]
	# m[(0, 0, 7, 6, 0)] = 1
	# while fringe:
	# 	x = fringe.pop()
	# 	p1_score, p2_score, p1_pos, p2_pos, turn = x
	# 	# if x in seen:
	# 	# 	continue

	# 	if p1_score >= 21 or p2_score >= 21:
	# 		continue
	# 	# seen.add(x)

	# 	for r, cnt in [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]:
	# 		if turn == 1:
	# 			new_p2_pos = (p2_pos + r) % len(track)
	# 			new_p2_score = p2_score + track[new_p2_pos]
	# 			y = (p1_score, new_p2_score, p1_pos, new_p2_pos, 1 - turn)
	# 		else:
	# 			new_p1_pos = (p1_pos + r) % len(track)
	# 			new_p1_score = p1_score + track[new_p1_pos]
	# 			y = (new_p1_score, p2_score, new_p1_pos, p2_pos, 1 - turn)
	# 		fringe.append(y)
	# 		m[y] += m[x] * cnt

	print(set(m.values()))
	# scores = [0, 0]
	# for p1_score, p2_score, p1_pos, p2_pos, turn in m:
	# 	k = m[(p1_score, p2_score, p1_pos, p2_pos, turn)]
	# 	if p1_score >= 21 and p2_score >- 21:
	# 		continue
	# 	if p1_score >= 21 and turn == 1:
	# 		scores[0] += k
	# 	if p2_score >= 21 and turn == 0:
	# 		scores[1] += k
	# return max(scores)

	
	return 0



cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
