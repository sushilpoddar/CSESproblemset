"""this is a problem of print number whose adjacent value difference is never one"""


def main(n):
	if n == 1:
		print(1)
		return
	if n == 2 or n == 3:
		print('NO SOLUTION')
		return
	if n % 2 == 0:
		for i in range(2, n+1, 2):
			print(i, end=' ')
		for i in range(1, n, 2):
			print(i, end=' ')
	else:
		for i in range(n-1, 0, -2):
			print(i, end=' ')
		for i in range(n, 0, -2):
			print(i, end=' ')


n = int(input())
main(n)
