for _ in range(int(input())):
	x, y = map(int, input().split())
	z = max(x, y)
	zz = int(((z*z)+1)-z)
	res = 0
	if x == y:
		res = zz
	elif z % 2 == 0:
		if x == z:
			res = zz + (z - y)
		else:
			res = zz - (y - x)
	else:
		if y == z:
			res = zz + (z - x)
		else:
			res = zz - (x - y)
	print(res)
