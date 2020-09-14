"""this is a chessboard and queen problem in which we have to place queen in the chessboard
so that no queen attack each other"""


def search(y):
	global ans
	if y == 8:
		ans += 1
		return
	for x in range(8):
		if col[x] or diag1[x + y] or diag2[x - y + 7] or reserved[y][x]:
			continue
		col[x] = diag1[x + y] = diag2[x - y + 7] = 1
		search(y + 1)
		col[x] = diag1[x + y] = diag2[x - y + 7] = 0


reserved = [[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0]]

diag1 = [0] * 16
diag2 = [0] * 16
col = [0] * 8
ans = 0

for i in range(8):
	st = input()
	for j in range(8):
		if st[j] != '.':
			reserved[i][j] = True
		else:
			reserved[i][j] = False
search(0)
print(ans)
