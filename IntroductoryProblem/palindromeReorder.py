string = input()
res = 0
result = ""
result1 = ""
single = ""
for i in sorted(set(string)):
	tmp = string.count(i)%1000000007
	if tmp % 2 == 0:
		result += i*int(tmp//2)
		result1 += i*int(tmp//2)
		continue
	elif tmp % 2 == 1 and res == 0:
		single += i*int(tmp)
		res += 1
	elif tmp % 2 == 1 and res == 1:
		res += 1
if res == 2:
	print("NO SOLUTION")
else:
	print(result+single+result1[-1::-1])
