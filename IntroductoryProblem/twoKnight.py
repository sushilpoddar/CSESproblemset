for n in range(1, int(input())+1):
	ans = n*n*(n*n-1)//2  # total number of ways
	print(ans - 4*(n-1)*(n-2))
