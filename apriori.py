import csv
from copy import deepcopy

min_support = int(input("Minimum support: "))
iteration = 1
transactions = []
keys = set()
counts = {}


def read():
	global counts
	reader = csv.reader(open("input.csv", 'r'))
	for row in reader:
		transactions.append(row)
		for ele in row:
			keys.add(ele)
	print "Transactions: ", transactions
	counts = dict(zip(keys, [0] * len(keys)))


def counter():
	for key in counts.keys():
		key_list = list(key)
		for entry in transactions:
			c = True
			for k in key_list:
				if k not in entry:
					c = False
					break
			if c is True:
				counts[key] = counts[key] + 1
	print "After counting: ", counts


def prune():
	for key, value in counts.items():
		if value < min_support:
			counts.pop(key)
	print "After pruning: ", counts


def gen():
	global counts
	old_keys = set(counts.keys())
	new_keys = set()
	for key in old_keys:
		copy_old_keys = old_keys.copy()
		copy_old_keys.remove(key)

		if iteration == 1:
			for key1 in copy_old_keys:
				new_keys.add(key+key1)

		elif iteration > 1:
			for key1 in copy_old_keys:
				if key[:iteration-1] == key1[:iteration-1]:
					new_keys.add(key + key1[iteration-1:])

	new_keys = remove_reversed(new_keys)
	counts = dict(zip(new_keys, [0] * len(new_keys)))


def remove_reversed(new_keys):
	new_keys = sorted(list(new_keys))
	for key in new_keys:
		new_keys_copy = deepcopy(new_keys)
		new_keys_copy.remove(key)
		_key = key[iteration-1:]
		_key = _key[::-1]

		for k in new_keys_copy:
			if _key in k or _key == k:
				new_keys.remove(k)
	return set(new_keys)


read()
while len(counts) > 0:
	print "\n----------Iteration " + str(iteration) + "----------\n"
	counter()
	prune()
	gen()
	iteration += 1

