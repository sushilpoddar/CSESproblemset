n = int(input())
total = sum(range(n+1))    # total =  n*(n+1)/2
if total % 2 != 0:
	print('NO')
else:
	seta = set()
	setb = set()
	j = 2
	seta.add(n)
	for i in range(n-1, 0, -2):
		if j % 2 == 0:
			setb.add(i)
			setb.add(i-1)
		else:
			seta.add(i)
			seta.add(i-1)
		j += 1
	print('YES')
	print(len(seta) if 0 not in seta else len(seta)-1)
	if 0 in seta:
		seta.remove(0)
		print(*seta)
	else:
		print(*seta)
	print(len(setb) if 0 not in setb else len(setb)-1)
	if 0 in setb:
		setb.remove(0)
		print(*setb)
	else:
		print(*setb)
