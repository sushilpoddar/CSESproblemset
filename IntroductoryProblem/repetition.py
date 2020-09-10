string = str(input()).upper()
res = 1
cur = 1
com = [string[0]]
for i in string[1:]:
	if i == com[-1]:
		cur += 1
		com.append(i)
		res = max(cur, res)

	else:
		com.clear()
		com.append(i)
		cur = 1
	res = max(cur, res)
print(res)