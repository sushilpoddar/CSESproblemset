"""  n = 50
	res = 0, i = 5
	res += 50//5 -->  res = 10
	res = 10, i = 5*5
	res += 50//25 --> res = 12
"""
# 1st method
res = 0
n = int(input())
j = 5
while j <= n+1:
	res += n//j
	j *= 5
print(res)

# 2nd method
res = 0
n = int(input())
while n >= 5:
	n //= 5
	res += n
print(res)
