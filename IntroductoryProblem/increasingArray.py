n = int(input())
val = list(map(int, input().split()))
res = 0
for i in range(1, len(val)):
	j = int(val[i-1])
	if val[i]-j < 0:
		cur = abs(val[i]-j)
		val[i] += cur
		res += cur
print(res)