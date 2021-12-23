import re
import pyperclip
from collections import defaultdict, deque
import tqdm
import math
import heapq
from itertools import permutations, product
import numpy as np
import copy

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



def solve(lst):
	result = 0
	walls = set()
	hallway = set()
	pos = defaultdict(lambda : [])
	costs = [1, 10, 100, 1000]
	for i in range(len(lst)):
		for j in range(len(lst[i])):
			if lst[i][j] == '#' or lst[i][j] == ' ':
				walls.add((i, j))
			elif not lst[i][j] == '.':
				pos[lst[i][j]].append((i, j))
			else:
				hallway.add((i, j))
	for y in [3, 5, 7, 9]:
		hallway.remove((1, y))
	

	target = tuple([((2, y), (3, y), (4, y), (5, y)) for y in [3, 5, 7, 9]])
	start = tuple([tuple(sorted(pos[k])) for k in sorted(pos)])

	# fringe = [(0, start, [start])]
	fringe = [(0, start)]
	seen = set()
	cnt = 0
	while fringe:
		cnt += 1

		# cost, state, past = heapq.heappop(fringe)
		cost, state = heapq.heappop(fringe)
		if cnt % 10000 == 0:
			print(cost)
		# print(cost, state, past)
		occupied = set([pos for x in state for pos in x]).union(walls)
		# print(bfs((2, 3), occupied))
		# print(state)
		# print(list(state))
		if state == target:
			return cost
		if state in seen:
			continue
		seen.add(state)

		state_lst = [list(s) for s in state]
		for am_type in range(len(state)):
			for i in range(len(state[am_type])):
				
				# print(state_lst)
				pos = state[am_type][i]
				paths = neighbors(am_type, pos, state, target, hallway, occupied, costs)

				for dest, c in paths:
					next_state_lst = copy.deepcopy(state_lst)
					next_state_lst[am_type][i] = dest
					next_state = tuple([tuple(sorted(s)) for s in next_state_lst])
					# n_p = past[:]
					# n_p.append(next_state)
					# heapq.heappush(fringe, (c + cost, next_state, n_p))
					heapq.heappush(fringe, (c + cost, next_state))

	return result

def neighbors(am_type, pos, state, target, hallway, occupied, costs):
	assert pos in state[am_type]
	lst = []
	paths = bfs(pos, occupied)
	if pos in hallway:
		# check other pods in target room
		for a_t in range(len(state)):
			if am_type == a_t:
				continue
			for p in state[a_t]:
				if p in target[am_type]:
					# other pods are in it
					return []

		# no other pods in target room
		for dest, cost in paths:
			if dest in target[am_type]:
				lst.append((dest, cost * costs[am_type]))

	# already in destination
	# elif pos in target[am_type]:
	# 	for dest, cost in paths:
	# 		if dest in target[am_type]:
	# 			lst.append((dest, cost * costs[am_type]))
	else:
		for dest, cost in paths:
			if dest in hallway:
				lst.append((dest, cost * costs[am_type]))
	return lst

def bfs(pos, occupied):
	# global cache
	# if (pos, occupied) in cache:
	# 	return cache[(pos, occupied)]
	fringe = deque()
	fringe.append((pos, 0))
	seen = set()
	result = []
	while fringe:
		state, cost = fringe.popleft()
		if (state in seen or state in occupied) and seen:
			continue
		seen.add(state)
		if not state == pos:
			result.append((state, cost))

		x, y = state
		for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
			fringe.append(((x + dx, y + dy), cost + 1))

	return result


cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
