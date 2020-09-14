"""this is a problem of make pair of one or two element from list whose sum is not exceed than x find number of pair
will be made.
"""
n, x = map(int, input().split())
val = sorted(list(map(int, input().split())), reverse=True)
ans = 0
lef = 0
r = n - 1
while lef <= r:
	if val[lef] + val[r] <= x:
		ans += 1
		lef += 1
		r -= 1
	else:
		ans += 1
		lef += 1

print(ans)
