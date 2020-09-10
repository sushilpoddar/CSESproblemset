"""this program check the given index value is set or not ..set means it is set to one(1)
"""
for _ in range(int(input())):
	n = int(input())
	index = int(input())
	f = 1
	f <<= index
	res = n & f
	if res == 0:
		print('ith index is not a set')
	else:
		print('ith index is a set')
